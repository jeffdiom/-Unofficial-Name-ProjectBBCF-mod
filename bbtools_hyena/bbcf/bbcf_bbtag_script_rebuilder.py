import os, struct, json, pac, fnmatch
import traceback
import sys
from ast import *
from astor import *
from collections import defaultdict, OrderedDict
import new_bbcf_bbtag_script_parser
json_data = open("static_db/bbcf/commandsDB.json").read()
commandDB = json.loads(json_data)
json_data = open("static_db/bbcf/characters.json").read()
moveInputs = json.loads(
    open("static_db/bbcf/named_values/move_inputs.json").read())
normalInputs = json.loads(
    open("static_db/bbcf/named_values/normal_inputs.json").read())

commandDBLookup = {}
namedValueLookup = {}
namedButtonLookup = {}
namedDirectionLookup = {}
new_bbcf_bbtag_script_parser.commandDB = commandDB
for key, data in commandDB.items():
    data["id"] = int(key)
    if "name" in data:
        commandDBLookup[data["name"]] = data
    else:
        commandDBLookup["Unknown" + key] = data
uponLookup = {v: k for k, v in new_bbcf_bbtag_script_parser.uponLookup.items()}
slotLookup = {v: k for k, v in new_bbcf_bbtag_script_parser.slotLookup.items()}
for k, v in moveInputs.items():
    namedValueLookup[v] = k
for k, v in normalInputs['grouped_values'].items():
    namedValueLookup[v] = k
for k, v in normalInputs['buttonbyte'].items():
    namedButtonLookup[v] = k
for k, v in normalInputs['directionbyte'].items():
    namedDirectionLookup[v] = k
commandCounts = defaultdict(int)
commandCalls = defaultdict(list)
output = ""

def decodeUpon(node):
    if node.name.replace("upon_", "") in uponLookup:
        return uponLookup[node.name.replace("upon_", "")]
    else:
        return int(node.name.replace("upon_", ""))


def decodeVar(node):

    retval = 0
    if isinstance(node, Num):
        retval= [0, node.n]
    elif hasattr(node, "id") and node.id.replace("SLOT_", "") in slotLookup:
        retval= [2, slotLookup[node.id.replace("SLOT_", "")]]
    elif isinstance(node, UnaryOp) and isinstance(node.op, USub):
        retval= [0, -node.operand.value]
    else:
        try:
            retval= [2, int(node.id.replace("SLOT_", ""))]
        except:
            #print(dump_tree(node))
            pass

    return retval


def writeCommandByName(name, params):
    cmdData = commandDBLookup[name]
    writeCommandByID(cmdData["id"], params)


def writeCommandByID(id, params):
    global output
    cmdData = commandDB[str(id)]
    myParams = list(params)
    for index, oValue in enumerate(myParams):
        if isinstance(oValue, str):
            myParams[index] = bytes(oValue, encoding="latin1")
        elif isinstance(oValue, int):
            pass
        elif isinstance(oValue, float):
            pass
        elif isinstance(oValue, Str):
            myParams[index] = bytes(oValue.s, encoding="latin1")
        elif isinstance(oValue, Num):
            myParams[index] = oValue.n
        elif isinstance(oValue, Name):
            temp = namedValueLookup.get(oValue.id)
            if temp is not None:
                myParams[index] = int(temp)
            else:
                buttonstr = oValue.id[-1]
                directionstr = oValue.id[:-1]
                myParams[index] = (int(namedButtonLookup[buttonstr]) <<
                                   8) + int(namedDirectionLookup[directionstr])
        elif isinstance(oValue, UnaryOp):
            if (isinstance(oValue.op, USub)):
                myParams[index] = -oValue.operand.value
            else:
                raise Exception("Unhandled Op" + str(type(oValue)))
        elif isinstance(oValue, Constant):
            myParams[index] = oValue.value
        else:
            raise Exception("Unknown Type" + str(type(oValue)))
    output.write(struct.pack("<I", id))
    if "format" in cmdData:
        output.write(struct.pack("<" + cmdData["format"], *myParams))
    elif cmdData["size"] > 4:
        output.write(myParams[0])


class Rebuilder(ExplicitNodeVisitor):
    def visit_Module(self, node):
        global output
        global root
        root = node
        stateCount = 0
        output.write(struct.pack("<I", stateCount))
        
        global dbg_currentFunction
        dbg_currentFunction = ""

        for function in node.body:
            if type(function) != FunctionDef:
                raise Exception("Root level elements must be functions")
            if function.decorator_list[0].id != "State":
                continue
            function._index = stateCount
            stateCount += 1
            if function.name.startswith('__') and function.name[2].isdigit():
                function.name = function.name[2:]
            if '__sp__' in function.name:
                function.name.replace('__sp__', ' ')
            if '__qu__' in function.name:
                function.name.replace('__qu__', '?')
            if '__at__' in function.name:
                function.name.replace('__at__', '@')
            output.write(struct.pack("<32sI", bytes(function.name, encoding="latin1"), 0xDEAFBEEF))
        node._dataStart = output.tell()
        output.seek(0)
        output.write(struct.pack("<I", stateCount))
        for childNode in node.body:
            self.visit_RootFunctionDef(childNode)

    def visit_Str(self, node):
        pass

    def visit_RootFunctionDef(self, node):
        global output, root
        output.seek(0, 2)

        global dbg_currentFunction
        dbg_currentFunction = node.name

        if len(node.decorator_list) == 1:
            if node.decorator_list[0].id == "State":
                #Write offset into state table
                startOffset = output.tell() - root._dataStart
                output.seek(4 + 36 * node._index + 32)
                output.write(struct.pack("<I", startOffset))
                output.seek(0, 2)
                if node.name.startswith('__') and node.name[2].isdigit():
                    node.name = node.name[2:]
                if '__sp__' in node.name:
                    node.name.replace('__sp__', ' ')
                if '__qu__' in node.name:
                    node.name.replace('__qu__', '?')
                if '__at__' in node.name:
                    node.name.replace('__at__', '@')
                writeCommandByName("startState", [node.name])
                self.visit_body(node.body)
            else:
                if node.name.startswith('__') and node.name[2].isdigit():
                    node.name = node.name[2:]
                if '__sp__' in node.name:
                    node.name.replace('__sp__', ' ')
                if '__qu__' in node.name:
                    node.name.replace('__qu__', '?')
                if '__at__' in node.name:
                    node.name.replace('__at__', '@')
                writeCommandByName("startSubroutine", [node.name])
                self.visit_body(node.body)
                writeCommandByName("endSubroutine", [])
        else:
            raise Exception("haven't implemented this")

    def visit_Pass(self, node):
        pass

    def visit_Call(self, node):
        # We have a function call. Is it a named function or is it UnknownXXXXX
        if "Unknown" in node.func.id:
            cmdId = int(node.func.id.replace("Unknown", ""))
        elif node.func.id in commandDBLookup:
            cmdId = commandDBLookup[node.func.id]["id"]      
        else:
            print(dump_tree(node))
            raise Exception("Unknown Command " + node.func.id)
        writeCommandByID(cmdId, node.args)

    def visit_FunctionDef(self, node):
        if "upon" not in node.name:
            raise Exception("inner functions are used for upon handlers only")
        writeCommandByName("upon", [decodeUpon(node)])
        self.visit_body(node.body)

    def visit_If(self, node):
        find = False

        try:
            find = node.body[0].value.func.id == "_gotolabel"
        except:
            pass

        if ((isinstance(node.test, Name)) and find):
            writeCommandByID(18, [node.body[0].value.args[0]] + decodeVar(node.test))
        
        elif (
                isinstance(node.test, UnaryOp)
            and isinstance(node.test.operand, Name)
            and isinstance(node.test.op, Not)
            and find
            ):
                writeCommandByID(19, [node.body[0].value.args[0]] + decodeVar(node.test.operand))

        elif (      isinstance(node.test, Call) 
                or  isinstance(node.test, Compare)):
            self.visit(node.test)
            writeCommandByName("if", [2, 0])
            self.visit_body(node.body)
            writeCommandByName("endIf", [])
            if len(node.orelse) > 0:
                writeCommandByName("else", [])
                self.visit_body(node.orelse)
                writeCommandByName("endElse", [])

        elif isinstance(node.test, Name):
            #This is if(SLOT) we need to find out slot index and write it as param of if
            writeCommandByName("if", decodeVar(node.test))
            self.visit_body(node.body)
            writeCommandByName("endIf", [])
            if len(node.orelse) > 0:
                writeCommandByName("else", [])
                self.visit_body(node.orelse)
                writeCommandByName("endElse", [])
        elif isinstance(node.test, UnaryOp) and isinstance(
                node.test.operand, Name):
            #This is if(SLOT) we need to find out slot index and write it as param of if
            writeCommandByName("ifNot", decodeVar(node.test.operand))
            self.visit_body(node.body)
            writeCommandByName("endIfNot", [])
            if len(node.orelse) > 0:
                writeCommandByName("else", [])
                self.visit_body(node.orelse)
                writeCommandByName("endElse", [])
        elif (isinstance(node.test, Call)
              or isinstance(node.test, Compare)) and find:
            self.visit(node.test)
            writeCommandByID(18, [node.body[0].value.args[0], 2, 0])

        elif isinstance(node.test,
                        UnaryOp) and (isinstance(node.test.operand, Call) or
                                      isinstance(node.test.operand, Compare)):
            self.visit(node.test.operand)
            writeCommandByName("ifNot", [2, 0])
            self.visit_body(node.body)
            writeCommandByName("endIfNot", [])
            if len(node.orelse) > 0:
                writeCommandByName("else", [])
                self.visit_body(node.orelse)
                writeCommandByName("endElse", [])
        else:
            print("UNHANDLED IF", dump(node))
        #If(SLOT)
        #If(Expr)
        #If(UnaryOp(Expr))
    def visit_Assign(self, node):
        if (    isinstance(node.value, BinOp)
            and not (isinstance(node.value.op, BitAnd))):
            params = []
            if isinstance(node.value.op, Add):
                params.append(0)
            elif isinstance(node.value.op, Sub):
                params.append(1)
            elif isinstance(node.value.op, Mult):
                params.append(2)
            elif isinstance(node.value.op, Div):
                params.append(3)
            else:
                print("UNIMPLEMENTED BINOP", dump(node))
                raise Exception("Unknown Operation!")
            writeCommandByName(
                "ModifyVar_", params + decodeVar(node.targets[0]) +
                decodeVar(node.value.right))
        
        elif    (   isinstance(node.value, Compare)
                or  (
                        isinstance(node.value, BinOp)
                    and isinstance(node.value.op, BitAnd)
                    )
                ):
            self.visit_Compare(node.value)
        
        else:
            writeCommandByName(
                "StoreValue",
                decodeVar(node.targets[0]) + decodeVar(node.value))

    def visit_Compare(self, node):
        params = []
        if isinstance(node, BinOp) and isinstance(node.op, BitAnd):
            params.append(7)
            node.comparators = [node.right]
        elif isinstance(node.ops[0], Eq):
            params.append(9)
        elif isinstance(node.ops[0], Gt):
            params.append(10)
        elif isinstance(node.ops[0], Lt):
            params.append(11)
        elif isinstance(node.ops[0], GtE):
            params.append(12)
        elif isinstance(node.ops[0], LtE):
            params.append(13)
        else:
            print("UNIMPLEMENTED BINOP", dump(node))
            raise Exception("Unknown Compare")
        writeCommandByName(
            "op",
            params + decodeVar(node.left) + decodeVar(node.comparators[0]))

    def visit_body(self, nodebody):
        try:
            for childNode in nodebody:
                self.visit(childNode)
        except AttributeError as e:
            traceback.print_exc()
            print(e, dump(childNode))

    def visit_Expr(self, node):
        self.visit(node.value)

    def generic_visit(self, node):
        print(type(node).__name__)


def rebuild_bbscript(sourceFilename, outPath):
    global output
    global dbg_currentFunction
    outFilename = os.path.split(sourceFilename)[1].replace(".py", ".bin")
    sourceAST = parsefile(sourceFilename)
    output = open(os.path.join(outPath, outFilename), "wb")
    try:
        Rebuilder().visit(sourceAST)
    except:
        print(traceback.print_exc())
        print("Last function visited was :")
        print(dbg_currentFunction)
    output.close()
    #output = open(outFilename, "rb")
    #output.seek(0, 2)
    #filesize = output.tell()
    #output.seek(0)
    #bbcpex_script_parser.parse_bbscript(output, "", "../../"+ outFilename, filesize)
    #output.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: bbcf_script_rebuilder.py infile.py outfile.bin")
    elif not (fnmatch.fnmatch(sys.argv[1], '*.py')
              and fnmatch.fnmatch(sys.argv[2], '*.bin')):
        print("Usage: bbcf_script_rebuilder.py infile.py outfile.bin")
        print("Check your extensions!")
    else:
        rebuild_bbscript(sys.argv[1], sys.argv[2])
        print("complete")
