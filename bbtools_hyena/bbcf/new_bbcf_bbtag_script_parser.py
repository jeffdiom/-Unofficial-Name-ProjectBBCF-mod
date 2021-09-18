import os, struct, json, sys
from astor import *
from ast import *
from collections import defaultdict, OrderedDict

json_data = open("static_db/bbcf/commandsDB.json").read()
commandDB = json.loads(json_data)
json_data = open("static_db/bbcf/characters.json").read()
characters = json.loads(json_data)
json_data = open("static_db/bbcf/named_values/move_inputs.json").read()
moveInputs = json.loads(json_data)
json_data = open("static_db/bbcf/named_values/normal_inputs.json").read()
normalInputs = json.loads(json_data)
commandCounts = defaultdict(int)
commandCalls = defaultdict(list)

uponLookup = {
    0: "IMMEDIATE",
    1: "STATE_END",
    2: "LANDING",
    3: "FRAME_STEP",
    11: "HIT_OR_BLOCK",
    12: "HIT_CONNECT",
    16: "INPUT_RECEIVED",
    23: "A_RELEASED",
    24: "B_RELEASED",
    25: "C_RELEASED",
    26: "D_RELEASED",
    42: "GUARDPOINT_ACTIVATION",
    60: "COUNTERHIT"
}

slotLookup = {
    0: "Result",
    15: "BackwardJump",
    16: "ForwardJump",
    18: "FrameCounter",
    47: "CheckReturnVal",
    110: "IsInOverdrive",
    116: "IsUnlimitedCharacter"
}

CMD_START_STATE         = 0
CMD_END_STATE           = 1
CMD_IF_STATEMENT        = 4
CMD_END_IF_STATEMENT    = 5
CMD_START_SUB           = 8
CMD_END_SUB             = 9
CMD_UPON_HANDLER        = 15
CMD_END_UPON_STATEMENT  = 16
CMD_GOTO_LABEL          = 18
CMD_GOTO_LABEL_IF_NOT   = 19
CMD_OP_COMPARE          = 40
CMD_OP_ASSIGN           = 41
CMD_OP_BINOP            = 49
CMD_IF_NOT_STATEMENT    = 54
CMD_END_IF_NOT_STATEMENT= 55
CMD_ELSE_STATEMENT      = 56
CMD_END_ELSE_STATEMENT  = 57

def findNamedValue(command, value):
    if commandDB[str(command)]['name'] == 'Move_Input_' or commandDB[str(
            command)]['name'] == 'CheckInput':
        if str(value) in moveInputs:
            return moveInputs[str(value)]
        return hex(value)
    elif commandDB[str(command)]['name'] == 'Move_Register' and isinstance(
            value, int):
        decstr = str(value)
        if decstr in normalInputs['grouped_values']:
            return normalInputs['grouped_values'][decstr]
        s = struct.pack('>H', value)
        button_byte, dir_byte = struct.unpack('>BB', s)
        if str(button_byte) in normalInputs['buttonbyte'] and str(
                dir_byte) in normalInputs['directionbyte']:
            return normalInputs['directionbyte'][str(
                dir_byte)] + normalInputs['buttonbyte'][str(button_byte)]
        return hex(value)
    elif commandDB[str(command)]['name'] == 'Move_Register' and isinstance(
            value, str):
        return value


def getUponName(cmdData):
    return uponLookup.get(cmdData, str(cmdData))


def getSlotName(cmdData):
    return slotLookup.get(cmdData, str(cmdData))

def getCurrentIndicator(cmdData):
    currentIndicator = cmdData[0]

    try:
        if currentIndicator[0].isdigit():
            currentIndicator = "__" + currentIndicator
        if " " in currentIndicator:
            currentIndicator = currentIndicator.replace(" ", "__sp__")
        if '?' in currentIndicator:
            currentIndicator = currentIndicator.replace("?", "__qu__")
        if '@' in currentIndicator:
            currentIndicator = currentIndicator.replace("@", "__at__")
    except:
        pass

    return currentIndicator

def sanitizer(command):
    def sanitize(s):
        # ew why
        if command in [43, 14012, 14001] and isinstance(s, int):
            s = findNamedValue(command, s)
        elif isinstance(s, str):
            s = "'{0}'".format(s.strip())
        elif command and "hex" in commandDB[str(command)]:
            s = hex(s)
        return str(s).strip("\x00")

    return sanitize


def pysanitizer(command):
    def sanitize(s):
        if isinstance(s, str):
            s = "{0}".format(s.strip())
        elif command and "hex" in commandDB[str(command)]:
            s = repr(s)
        return str(s).strip()

    return sanitize


def parse_bbscript_routine(f, end=-1):
    global astRoot
    currentCMD = -1
    currentIndicator = "_PRE"
    currentFrame = 1
    astStack = [astRoot.body]

    # Atrocious workaround for some stray endElses in some char scripts
    # There's probably a more elegant way to check that we're in an else
    # statement but I don't know it
    currentlyNestedElses = 0

    #Same thing but for stray endUpons
    currentlyNestedUpons = 0

    while f.tell() != end:

        loc = f.tell()
        try:
            currentCMD, = struct.unpack("<I", f.read(4))
        except:
            return
        commandCounts[currentCMD] += 1

        try :
            dbData = commandDB[str(currentCMD)]
        except :
            commandDB[str(currentCMD)] = { "format" : "" }
            dbData = commandDB[str(currentCMD)]

        if "name" not in dbData:
            dbData["name"] = f"Unknown{currentCMD}"
        if "format" not in dbData:
            cmdData = [ f.read(commandDB[str(currentCMD)]["size"] - 4) ]
        else:
            cmdData = list(
                struct.unpack("<" + dbData["format"],
                              f.read(struct.calcsize(dbData["format"]))))
            
        try:
            for i in range(len(cmdData)):
                if isinstance(cmdData[i], bytes):

                    cmdData[i] = cmdData[i].decode("latin1").strip("\x00")

                    if "format" not in dbData:
                        print(currentCMD + " not in db")
        except:
            pass

        if ((currentCMD == 0) or (dbData["name"] == "startSubroutine")):
            while (len(astStack) > 1):
                astStack.pop()

        #commandCalls[currentCMD].append((characters[charName],currentIndicator,currentFrame,"{0}({1})".format(dbData["name"],",".join(map(sanitizer(currentCMD),cmdData)))))
        if currentCMD == 0:
            currentIndicator = getCurrentIndicator(cmdData)

            if ("-" in str(currentIndicator)):
                cmdData[0] = str(cmdData[0]).replace('-', '_')

            currentContainer = []

        elif dbData["name"] == "startSubroutine":
            currentIndicator = getCurrentIndicator(cmdData)

            # Replace potential dashes in function names
            currentIndicator = currentIndicator.replace("-", "_")
            currentContainer = []

        elif dbData["name"] in ["endFunction", "endSubroutine"]:
            pass
        else:
            currentContainer.append({
                'id':
                currentCMD,
                'params':
                list(map(pysanitizer(currentCMD), cmdData))
            })
        comment = None

        #AST STUFF
        if currentCMD == CMD_START_STATE:
            currentIndicator = getCurrentIndicator(cmdData)

            astStack[-1].append(
                FunctionDef(currentIndicator, 
                            args=arguments(args=[], defaults=[None], vararg=None, kwarg=None), 
                            body=[], 
                            decorator_list=[Name(id="State")]
                            ))
            astStack.append(astStack[-1][-1].body)
        elif currentCMD == CMD_START_SUB:
            currentIndicator = getCurrentIndicator(cmdData)

            astStack[-1].append(
                FunctionDef(currentIndicator,
                            args=arguments(args=[], defaults=[None], vararg=None, kwarg=None), 
                            body=[], 
                            decorator_list=[Name(id="Subroutine")]
                            ))
            astStack.append(astStack[-1][-1].body)
        elif currentCMD == CMD_UPON_HANDLER:
            astStack[-1].append(
                FunctionDef(dbData['name'] + "_" + getUponName(cmdData[0]), 
                            args=arguments(args=[], defaults=[None], vararg=None, kwarg=None), 
                            body=[], 
                            decorator_list=[]
                            ))
  
            astStack.append(astStack[-1][-1].body)

            currentlyNestedUpons += 1
        
        elif currentCMD == CMD_IF_STATEMENT:
            tmp = Name(id="SLOT_" + getSlotName(cmdData[1]))
            astStack[-1].append(If(tmp, [], []))
            astStack.append(astStack[-1][-1].body)

        elif currentCMD == CMD_GOTO_LABEL and cmdData[1] == 0:
            if astStack[-1] == []:
                tmp = Name(id="SLOT_" + getSlotName(cmdData[1]))
                astStack[-1].append(If(tmp, [], []))
            else:
                tmp = astStack[-1].pop()
                if not hasattr(tmp, "value"):
                    tmp = Expr(tmp)
                astStack[-1].append(If(tmp.value, [], []))

            astStack[-1][-1].body = [
                Expr(Call(  Name(id="_gotolabel"), 
                            [arg(str(cmdData[0]), annotation=None)], 
                            []))
            ]

        elif currentCMD == CMD_GOTO_LABEL:

            tmp = Name(id="SLOT_" + getSlotName(cmdData[2]))
            astStack[-1].append(If(tmp, [], []))

            astStack[-1][-1].body = [
                Expr(Call(  Name(id="_gotolabel"), 
                            [arg(str(cmdData[0]), annotation=None)], 
                            []))
            ]

        elif currentCMD == CMD_GOTO_LABEL_IF_NOT:

            tmp = Name(id="SLOT_" + getSlotName(cmdData[2]))
            astStack[-1].append(If(UnaryOp(Not(), tmp), [], []))

            astStack[-1][-1].body = [
                Expr(Call(  Name(id="_gotolabel"), 
                            [arg(str(cmdData[0]), annotation=None)], 
                            []))
            ]

        elif currentCMD == CMD_OP_COMPARE and cmdData[0] in [7, 9, 10, 11, 12, 13]:
            if (cmdData[1] == 2):
                lval = Name(id="SLOT_" + getSlotName(cmdData[2]))
            else:
                lval = Num(cmdData[2])

            if (cmdData[3] == 2):
                rval = Name(id="SLOT_" + getSlotName(cmdData[4]))
            else:
                rval = Num(cmdData[4])

            if cmdData[0] == 7:
                op = BitAnd()
            if cmdData[0] == 9:
                op = Eq()
            if cmdData[0] == 10:
                op = Gt()
            if cmdData[0] == 11:
                op = Lt()
            if cmdData[0] == 12:
                op = GtE()
            if cmdData[0] == 13:
                op = LtE()

            tmp = Assign([Name(id="SLOT_Result")], Compare(lval, [op], [rval]))
            astStack[-1].append(tmp)

        elif currentCMD == CMD_OP_ASSIGN:
            if (cmdData[0] == 2):
                lval = Name(id="SLOT_" + getSlotName(cmdData[1]))
            else:
                lval = Num(cmdData[1])
            if (cmdData[2] == 2):
                rval = Name(id="SLOT_" + getSlotName(cmdData[3]))
            else:
                rval = Num(cmdData[3])
            tmp = Assign([lval], rval)
            astStack[-1].append(tmp)

        elif currentCMD == CMD_OP_BINOP and cmdData[0] in [0, 1, 2, 3]:
            if (cmdData[1] == 2):
                lval = Name(id="SLOT_" + getSlotName(cmdData[2]))
            else:
                lval = Num(cmdData[2])
            if (cmdData[3] == 2):
                rval = Name(id="SLOT_" + getSlotName(cmdData[4]))
            else:
                rval = Num(cmdData[4])
            if cmdData[0] == 0:
                op = Add()
            if cmdData[0] == 1:
                op = Sub()
            if cmdData[0] == 2:
                op = Mult()
            if cmdData[0] == 3:
                op = Div()
            tmp = Assign([lval], BinOp(lval, op, rval))
            astStack[-1].append(tmp)

        elif currentCMD == CMD_IF_NOT_STATEMENT:
            tmp = Name(id="SLOT_" + getSlotName(cmdData[1]))
            astStack[-1].append(If(UnaryOp(Not(), tmp), [], []))
            astStack.append(astStack[-1][-1].body)

        elif currentCMD == CMD_ELSE_STATEMENT:

            try:
                ifnode = astStack[-1][-1]
                if (isinstance(ifnode, If)):
                    astStack.append(ifnode.orelse)
                else:
                    astStack.append([])
            except:
                astStack.append([])

            currentlyNestedElses += 1

        elif currentCMD == CMD_END_ELSE_STATEMENT:

            if (currentlyNestedElses > 0):

                if len(astStack) > 1:
                    astStack.pop()
                    currentlyNestedElses -= 1

        elif currentCMD == CMD_END_IF_STATEMENT:

            if len(astStack[-1]) == 0:
                astStack[-1].append(Pass())
            
            if len(astStack) > 1:
                astStack.pop()

        elif currentCMD == CMD_END_UPON_STATEMENT:

            if (currentlyNestedUpons > 0):
                # print("1", dbData["name"], list(map(sanitizer(currentCMD), cmdData)))
                astStack[-1].append(
                        Expr(
                            Call(Name(id=dbData["name"]),
                                 [arg(item, annotation=None) for item in list(map(sanitizer(currentCMD), cmdData))], 
                                 [])))
                astStack.pop()
                currentlyNestedUpons -= 1

        elif currentCMD == CMD_END_STATE:

            try:
                astStack[-1].append(
                    Expr(
                        Call(Name(id=dbData["name"]),
                             [arg(item, annotation=None) for item in list(map(sanitizer(currentCMD), cmdData))], 
                             [])))
            except:
                traceback.print_exc()

        elif currentCMD in [CMD_END_IF_STATEMENT, CMD_END_SUB, CMD_END_IF_NOT_STATEMENT]:
            
            if len(astStack) > 0:
                if len(astStack[-1]) == 0:
                    astStack[-1].append(Pass())
                if len(astStack) > 1:
                    astStack.pop()
                else:
                    try:
                        # print("2", dbData["name"], list(map(sanitizer(currentCMD), cmdData)))
                        astStack[-1][-1].body.append(
                            Expr(
                                Call(Name(id=dbData["name"]),
                                     [arg(item, annotation=None) for item in list(map(sanitizer(currentCMD), cmdData))], 
                                     [])))
                    except:
                        print("\tasterror", currentIndicator, len(astStack))
                        print(dbData)
                        # print(astor.dump(astStack[-1]))
                        # print(map(sanitizer(currentCMD), cmdData))
                        # print("3", dbData["name"], list(map(sanitizer(currentCMD), cmdData)))
                        astStack[-1].append(
                            Expr(
                                Call(Name(id=dbData["name"]),
                                     [arg(item, annotation=None) for item in list(map(sanitizer(currentCMD), cmdData))], 
                                     [])))
        else:
            try:
                # print("4", dbData["name"], arg(list(map(sanitizer(currentCMD), cmdData))))
                astStack[-1].append(
                    Expr(
                        Call(Name(id=dbData["name"]),
                             [arg(item, annotation=None) for item in list(map(sanitizer(currentCMD), cmdData))], 
                             [])))
            except:
                print(currentIndicator, currentCMD, cmdData)
                traceback.print_exc()



def parse_bbscript(filepath, outpath):
    global commandDB, astRoot
    astRoot = Module(body=[])
    
    f = open(filepath, 'rb')
    BASE = f.tell()
    size = os.path.getsize(filepath)

    filename = os.path.split(filepath)[1]
    output_file = os.path.join(outpath, filename[:-4] + ".py")

    FUNCTION_COUNT, = struct.unpack("<I", f.read(4))

    f.seek(BASE + 4 + 0x24 * (FUNCTION_COUNT))
    parse_bbscript_routine(f, os.path.getsize(f.name))

    py = open(output_file, "w")
    # print(dump_tree(astRoot))
    # content=dump_tree(astRoot)
    content=to_source(astRoot)
    py.write(content)
    py.close()

if __name__ == '__main__':
    if len(sys.argv) != 3 and len(sys.argv) != 2:
        print("Usage:bbcf_script_parser.py scr_xx.bin outdir")
        print("Default output directory if left blank is the current script directory.")
    else:
        filepath = sys.argv[1]

        if len(sys.argv) == 3:
            outpath = sys.argv[2]
        else:
            outpath = ""

        parse_bbscript(filepath, outpath)
