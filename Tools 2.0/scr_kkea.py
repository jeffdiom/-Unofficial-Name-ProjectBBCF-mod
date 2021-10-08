@State
def EMB_KK():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(256000)
        Unknown2054(1)
        IsInvisibility(1)
        Unknown4003('ef_emb_KK.DIG', '')
        Unknown23015(5)
        GFX_Scale(1400)
        GFX_OffsetY(16000)
    sprite('null', 10)
    Unknown3026(4278190080)
    Unknown3025(4278190335, 10)
    sprite('null', 10)
    Unknown3025(4286625023, 10)
    sprite('null', 10)
    Unknown3025(4294967295, 10)
    sprite('null', 10)
    Unknown3025(4286625023, 10)
    sprite('null', 30)
    sprite('null', 50)
    Unknown3001(0)

@State
def EMB_KK_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(256000)
        Unknown2054(1)
        IsInvisibility(1)
        Unknown4003('ef_emb_KK.DIG', '')
        Unknown23015(5)
        GFX_Scale(1400)
        GFX_OffsetY(16000)
    sprite('null', 8)
    Unknown3026(4278190080)
    Unknown3025(4294967295, 10)
    sprite('null', 8)
    Unknown3025(4286625023, 10)
    sprite('null', 8)
    Unknown3025(4278223103, 10)
    sprite('null', 8)
    Unknown3025(4278223103, 10)
    sprite('null', 80)

@State
def EMB_KK_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(256000)
        Unknown2054(1)
        Unknown4003('ef_emb_KK.DIG', '')
        GFX_Scale(1400)
        GFX_OffsetY(16000)
        Unknown23015(5)
    sprite('null', 10)
    Unknown3026(4278190080)
    Unknown3025(4294901760, 10)
    sprite('null', 10)
    Unknown3025(4294912040, 10)
    sprite('null', 10)
    Unknown3025(4294948020, 10)
    sprite('null', 10)
    Unknown3025(4294901760, 10)
    sprite('null', 80)

@State
def __3Dtest():

    def upon_IMMEDIATE():
        Unknown4003('kkef_gate.DIG', '')
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        Unknown23015(2)
        Unknown2019(100)
        Unknown4015()
        Unknown13044(1)
        GFX_OffsetY(192000)
        GFX_OffsetX(-64000)
    GFX_0('3Dtest_b', -1)
    sprite('null', 8)
    GFX_Scale(100)
    Unknown1099(100)
    sprite('null', 10)
    Unknown1099(0)
    sprite('null', 20)
    Unknown4010(0)
    Unknown4007(0)
    Unknown4009(0)
    sprite('null', 9)
    Unknown1099(-100)
    sprite('null', 0)

@State
def __3Dtest_b():

    def upon_IMMEDIATE():
        Unknown4003('kkef_gate_b.DIG', '')
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        Unknown2019(100)
        Unknown4015()
        Unknown13044(1)
    sprite('null', 8)
    GFX_Scale(100)
    Unknown1099(100)
    sprite('null', 10)
    Unknown1099(0)
    sprite('null', 20)
    Unknown4010(0)
    Unknown4007(0)
    Unknown4009(0)
    sprite('null', 9)
    Unknown1099(-100)
    sprite('null', 0)

@State
def test_gate():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        GFX_SetPalette(3)
        Unknown3032()
        Unknown3001(255)
        Unknown2019(100)
        Unknown13044(1)
    sprite('vrkkef_hole_a00', 8)
    GFX_Scale(100)
    Unknown1099(50)
    sprite('vrkkef_hole_a00', 10)
    Unknown1064(550)
    Unknown1056(700)
    Unknown1099(0)
    sprite('vrkkef_hole_a00', 11)
    Unknown4010(0)
    Unknown4007(0)
    Unknown4009(0)
    sprite('vrkkef_hole_a01', 3)
    sprite('vrkkef_hole_a02', 3)
    sprite('vrkkef_hole_a03', 3)
    sprite('vrkkef_hole_a03', 9)
    Unknown1099(-100)

@State
def efkk_210():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        GFX_SetPalette(2)
        Unknown3033()
        Unknown3001(255)
    sprite('null', 32767)
    GFX_2('kkef_210')

@State
def efkk_202_smoke():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        GFX_SetPalette(2)
        Unknown3033()
        Unknown3001(255)
    sprite('null', 32767)
    GFX_1('kkef_202_fire', -1)
    GFX_1('kkef_202', -1)

@State
def efkk_202_hole():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4024(3)
        Unknown4009(3)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown2019(500)
        GFX_OffsetX(-80000)
        GFX_OffsetY(176000)
        GFX_Scale(800)
    sprite('vrkkef_hole_a10', 2)
    sprite('vrkkef_hole_a11', 4)
    Unknown4007(0)
    Unknown4009(0)
    sprite('vrkkef_hole_a00', 12)
    GFX_0('efkk_202_electric', -1)
    sprite('vrkkef_hole_a01', 4)
    sprite('vrkkef_hole_a02', 4)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 4)
    GFX_Unload('efkk_202_electric')
    sprite('vrkkef_hole_a21', 4)

@State
def efkk_202_electric():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4024(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown3033()
        Unknown2019(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)

@State
def efkk_202_weapon():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4024(3)
        GFX_SetPalette(0)
        Unknown3032()
        GFX_OffsetX(-176000)
        GFX_OffsetY(128000)
    sprite('vrkkef202weapon', 5)
    physicsXImpulse(-3000)
    physicsYImpulse(3000)
    setGravity(2500)

    def upon_LANDING():
        physicsYImpulse(22000)
        GFX_1('kkef235_bound', -1)
    sprite('vrkkef202weapon', 10)
    GFX_0('efkk_202_hole_out', -1)
    sprite('vrkkef202weapon', 9)
    sprite('vrkkef202weapon_out', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)

@State
def efkk_202_hole_out():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4024(3)
        Unknown2019(500)
        GFX_SetPalette(3)
        GFX_OffsetX(-64000)
        GFX_OffsetY(64000)
        GFX_Scale(950)
    sprite('vrkkef_hole_a10', 4)
    sprite('vrkkef_hole_a11', 4)
    sprite('vrkkef_hole_a00', 16)
    GFX_0('efkk_202_out_electric', -1)
    sprite('vrkkef_hole_a01', 4)
    sprite('vrkkef_hole_a02', 4)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 4)
    GFX_Unload('efkk_202_out_electric')
    sprite('vrkkef_hole_a21', 4)

@State
def efkk_202_out_electric():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4024(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown3033()
        Unknown2019(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)

@State
def efkk_212_burner():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        GFX_SetPalette(2)
        Unknown3033()
        Unknown3001(255)
    sprite('vrkkef212_00', 4)
    Unknown2019(100)
    sprite('vrkkef212_01', 4)
    sprite('vrkkef212_02', 3)
    Unknown2019(-100)
    GFX_1('kkef_fire_kira', 0)
    GFX_1('kkef_fire_kira', 1)
    GFX_1('kkef_fire_kira', 2)
    GFX_1('kkef_fire_kira', 3)
    sprite('vrkkef212_03', 3)
    Unknown2019(100)
    GFX_1('kkef_fire_kira', 0)
    GFX_1('kkef_fire_kira', 1)
    sprite('vrkkef212_04', 3)
    GFX_1('kkef_fire_kira', 0)

@State
def efkk_212_hole():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4024(3)
        Unknown4009(3)
        GFX_SetPalette(3)
        Unknown2019(500)
        GFX_OffsetX(-160000)
        GFX_OffsetY(192000)
        GFX_Scale(950)
    sprite('vrkkef_hole_a10', 3)
    sprite('vrkkef_hole_a11', 3)
    sprite('vrkkef_hole_a00', 9)
    Unknown4007(0)
    Unknown4009(0)
    GFX_0('efkk_212_electric', -1)
    sprite('vrkkef_hole_a01', 4)
    sprite('vrkkef_hole_a02', 4)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 4)
    GFX_Unload('efkk_212_electric')
    sprite('vrkkef_hole_a21', 4)

@State
def efkk_212_electric():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4024(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown3033()
        Unknown2019(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)

@State
def efkk_212_hole_out():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4011(3)
        Unknown4024(3)
        Unknown4009(3)
        GFX_SetPalette(3)
        Unknown2019(500)
        Unknown2005()
        GFX_OffsetX(128000)
        GFX_OffsetY(112000)
        GFX_Rotation(-80000)
        GFX_Scale(850)
    sprite('vrkkef_hole_a00', 3)
    GFX_0('efkk_202_out_electric', -1)
    sprite('vrkkef_hole_a01', 1)
    sprite('vrkkef_hole_a01', 2)
    Unknown4007(0)
    Unknown4009(0)
    sprite('vrkkef_hole_a02', 3)
    sprite('vrkkef_hole_a03', 3)
    sprite('vrkkef_hole_a20', 4)
    GFX_Unload('efkk_202_out_electric')
    sprite('vrkkef_hole_a21', 4)

@State
def efkk_202_out_electric():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4024(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown3033()
        Unknown2019(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)

@State
def efkk_232_burner():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        GFX_SetPalette(2)
        Unknown3033()
        Unknown3001(255)
    sprite('vrkkef232_00', 3)
    Unknown2019(100)
    GFX_1('kkef_fire_kira', 0)
    sprite('vrkkef232_01', 3)
    Unknown2019(-100)
    GFX_1('kkef_fire_kira', 0)
    GFX_1('kkef_fire_kira', 1)
    sprite('vrkkef232_02', 3)

@State
def efkk_232_hole():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4024(3)
        Unknown4009(3)
        GFX_SetPalette(3)
        Unknown2019(500)
        GFX_OffsetX(-192000)
        GFX_OffsetY(164000)
        GFX_Scale(800)
    sprite('vrkkef_hole_a10', 2)
    sprite('vrkkef_hole_a11', 3)
    sprite('vrkkef_hole_a00', 2)
    GFX_0('efkk_232_electric', -1)
    sprite('vrkkef_hole_a00', 5)
    Unknown4007(0)
    sprite('vrkkef_hole_a01', 2)
    GFX_Unload('efkk_232_electric')
    Unknown4009(0)
    sprite('vrkkef_hole_a21', 2)

@State
def efkk_232_electric():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4024(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown3033()
        Unknown2019(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)

@State
def efkk_232_hole_out():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4011(3)
        Unknown4024(3)
        Unknown4009(3)
        GFX_SetPalette(3)
        Unknown2019(500)
        GFX_OffsetX(-112000)
        GFX_OffsetY(256000)
        GFX_Scale(750)
        Unknown2005()
    sprite('vrkkef_hole_a10', 3)
    sprite('vrkkef_hole_a11', 3)
    sprite('vrkkef_hole_a00', 3)
    GFX_0('efkk_232_out_electric', -1)
    sprite('vrkkef_hole_a00', 1)
    Unknown4007(0)
    sprite('vrkkef_hole_a01', 4)
    sprite('vrkkef_hole_a02', 4)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 3)
    GFX_Unload('efkk_232_out_electric')
    sprite('vrkkef_hole_a21', 3)

@State
def efkk_232_out_electric():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4024(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown3033()
        Unknown2019(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)

@State
def efkk_235_hole():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4011(3)
        Unknown4024(3)
        Unknown4009(3)
        GFX_SetPalette(3)
        Unknown2019(500)
        GFX_OffsetX(-192000)
        GFX_OffsetY(160000)
        GFX_Scale(750)
    sprite('vrkkef_hole_a10', 4)
    sprite('vrkkef_hole_a11', 2)
    sprite('vrkkef_hole_a11', 2)
    Unknown4007(0)
    Unknown4009(0)
    sprite('vrkkef_hole_a00', 3)
    GFX_0('efkk_235_electric', -1)
    sprite('vrkkef_hole_a01', 3)
    sprite('vrkkef_hole_a02', 3)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 4)
    GFX_Unload('efkk_235_electric')
    sprite('vrkkef_hole_a21', 4)

@State
def efkk_235_electric():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4024(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown3033()
        Unknown2019(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)

@State
def efkk_235_weapon():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4024(3)
        GFX_SetPalette(0)
        Unknown3032()
        GFX_OffsetX(-224000)
        GFX_OffsetY(96000)
    sprite('vrkkef235weapon', 11)
    physicsXImpulse(-8000)
    setGravity(2500)

    def upon_LANDING():
        physicsYImpulse(30000)
        GFX_1('kkef235_bound', -1)
    sprite('vrkkef235weapon', 9)
    GFX_0('efkk_235_hole_out', -1)
    sprite('vrkkef235weapon_out', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)

@State
def efkk_235_hole_out():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4024(3)
        GFX_SetPalette(3)
        Unknown2019(500)
        GFX_OffsetX(-88000)
        GFX_OffsetY(192000)
        GFX_Scale(800)
    sprite('vrkkef_hole_a10', 4)
    GFX_0('efkk_235_out_electric', -1)
    sprite('vrkkef_hole_a11', 4)
    sprite('vrkkef_hole_a00', 6)
    sprite('vrkkef_hole_a01', 3)
    sprite('vrkkef_hole_a02', 3)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 4)
    Unknown4007(0)
    GFX_Unload('efkk_235_out_electric')
    sprite('vrkkef_hole_a21', 4)

@State
def efkk_235_out_electric():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4024(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown3033()
        Unknown2019(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)

@State
def efkk_252_hole():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4024(3)
        GFX_SetPalette(3)
        Unknown2019(500)
        GFX_OffsetX(-128000)
        GFX_OffsetY(192000)
        GFX_Rotation(40000)
        GFX_Scale(850)
    sprite('vrkkef_hole_a11', 10)
    sprite('vrkkef_hole_a00', 8)
    GFX_0('efkk_252_electric', -1)
    Unknown4007(0)
    Unknown4009(0)
    sprite('vrkkef_hole_a01', 3)
    sprite('vrkkef_hole_a02', 3)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 3)
    GFX_Unload('efkk_252_electric')
    sprite('vrkkef_hole_a21', 3)

@State
def efkk_252_electric():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4024(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown3033()
        Unknown2019(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)

@State
def efkk_252_weapon():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4024(3)
        GFX_SetPalette(0)
        Unknown3032()
    sprite('vrkkef252weapon', 2)
    sprite('vrkkef252weapon', 8)
    physicsXImpulse(-20000)
    physicsYImpulse(4000)
    setGravity(2000)
    GFX_0('efkk_252_hole_out', -1)
    sprite('vrkkef252weapon_out', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)

@State
def efkk_252_hole_out():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4011(3)
        Unknown4024(3)
        GFX_SetPalette(3)
        Unknown2019(500)
        GFX_OffsetX(-320000)
        GFX_OffsetY(320000)
        GFX_Rotation(-15000)
        GFX_Scale(850)
    sprite('vrkkef_hole_a10', 4)
    Unknown4007(0)
    sprite('vrkkef_hole_a11', 4)
    sprite('vrkkef_hole_a00', 9)
    GFX_0('efkk_252_out_electric', -1)
    sprite('vrkkef_hole_a01', 4)
    sprite('vrkkef_hole_a02', 4)
    sprite('vrkkef_hole_a03', 11)
    sprite('vrkkef_hole_a20', 4)
    GFX_Unload('efkk_252_out_electric')
    sprite('vrkkef_hole_a21', 4)

@State
def efkk_252_out_electric():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4024(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown3033()
        Unknown2019(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)

@State
def efkk_253_burner():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        GFX_SetPalette(2)
        Unknown3033()
        Unknown3001(255)
    sprite('vrkkef253_00', 6)
    GFX_1('kkef_fire_kira', 0)
    sprite('vrkkef253_01', 3)
    GFX_1('kkef_fire_kira', 0)
    GFX_1('kkef_fire_kira', 1)
    sprite('vrkkef253_02', 3)
    GFX_1('kkef_fire_kira', 0)
    sprite('vrkkef253_03', 3)
    GFX_1('kkef_fire_kira', 0)
    Unknown4007(0)

@State
def efkk_253_hole():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4024(3)
        Unknown4009(3)
        GFX_SetPalette(3)
        Unknown2019(500)
        Unknown2005()
        GFX_OffsetX(110000)
        GFX_OffsetY(133000)
        GFX_Rotation(-60000)
        GFX_Scale(1000)
    sprite('vrkkef_hole_a10', 4)
    sprite('vrkkef_hole_a11', 4)
    Unknown4007(0)
    Unknown4009(0)
    sprite('vrkkef_hole_a00', 3)
    GFX_0('efkk_253_electric', -1)
    sprite('vrkkef_hole_a01', 3)
    sprite('vrkkef_hole_a02', 3)
    sprite('vrkkef_hole_a03', 3)
    sprite('vrkkef_hole_a20', 4)
    GFX_Unload('efkk_253_electric')
    sprite('vrkkef_hole_a21', 4)

@State
def efkk_253_electric():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4024(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown3033()
        Unknown2019(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)

@State
def efkk_253_weapon():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4024(3)
        GFX_SetPalette(0)
        Unknown3032()
    sprite('vrkkef253_weapon2', 4)
    GFX_0('efkk_253_hole_out', -1)

@State
def efkk_253_hole_out():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4024(3)
        GFX_SetPalette(3)
        Unknown2019(500)
        GFX_OffsetX(-192000)
        GFX_OffsetY(96000)
        GFX_Rotation(30000)
        GFX_Scale(950)
    sprite('vrkkef_hole_a00', 4)
    GFX_0('efkk_253_out_electric', -1)
    sprite('vrkkef_hole_a01', 4)
    sprite('vrkkef_hole_a02', 4)
    sprite('vrkkef_hole_a03', 10)
    sprite('vrkkef_hole_a20', 3)
    GFX_Unload('efkk_253_out_electric')
    sprite('vrkkef_hole_a21', 3)

@State
def efkk_253_out_electric():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4024(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown3033()
        Unknown2019(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)

@State
def efkk_340():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        GFX_SetPalette(2)
        Unknown3033()
        Unknown3001(255)
    sprite('vrkkef340_00', 3)
    sprite('vrkkef340_01', 3)
    Unknown2019(100)
    GFX_1('kkef_fire_kira', 0)
    sprite('vrkkef340_02', 2)
    Unknown2019(-100)
    GFX_1('kkef_fire_kira', 0)
    sprite('vrkkef340_03', 3)
    GFX_1('kkef_fire_kira', 0)
    sprite('vrkkef340_04', 4)
    GFX_1('kkef_fire_kira', 0)

@State
def efkk_340_hole():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4024(3)
        Unknown4009(3)
        GFX_SetPalette(3)
        Unknown2019(500)
        GFX_OffsetX(96000)
        GFX_OffsetY(360000)
    sprite('vrkkef_hole_b', 3)
    GFX_Scale(600)
    Unknown1099(100)
    sprite('vrkkef_hole_b', 3)
    GFX_Scale(1000)
    Unknown1099(0)
    sprite('vrkkef_hole_b', 15)
    Unknown4007(0)
    Unknown4009(0)
    sprite('vrkkef_hole_b', 6)
    Unknown1099(-100)

@State
def efkk_340_hole_out():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4011(3)
        Unknown4024(3)
        Unknown4009(3)
        GFX_SetPalette(3)
        Unknown2019(500)
        GFX_OffsetX(-189000)
        GFX_OffsetY(120000)
        GFX_Rotation(-40000)
    sprite('vrkkef_hole_b2', 6)
    GFX_Scale(0)
    Unknown1099(100)
    sprite('vrkkef_hole_b2', 5)
    GFX_Scale(600)
    Unknown1099(0)
    sprite('vrkkef_hole_b2', 11)
    Unknown4007(0)
    Unknown4009(0)
    sprite('vrkkef_hole_b2', 6)
    Unknown1099(-100)

@State
def efkk_340_out_electric():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4024(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown3033()
        Unknown2019(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)

@State
def efkk_throw():

    def upon_IMMEDIATE():
        Unknown23032(50)
        Unknown23033(50)
    sprite('null', 0)
    GFX_1('kkef311_linework_b', -1)

@State
def efkk_airdash():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 32767)
    GFX_2('kkef_airdash')

@State
def efkk_airdash_back():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 32767)
    GFX_2('kkef_airdash_back')

@State
def efkk_airbackdash():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 32767)
    GFX_2('kkef_airbackdash')

@State
def efkk_airbackdash_back():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 32767)
    GFX_2('kkef_airbackdash_back')

@State
def kkef_601():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        GFX_OffsetX(-40000)
        GFX_OffsetY(110000)
    sprite('null', 32767)
    GFX_2('kkef_601')

@State
def efkk_611():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        GFX_OffsetX(10000)
        GFX_OffsetY(30000)
    sprite('null', 19)
    GFX_2('kkef_611')

@State
def efkk_611b():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        GFX_OffsetX(10000)
        GFX_OffsetY(30000)
    sprite('null', 32767)
    GFX_2('kkef_611b')

@State
def efkk_denpa():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        GFX_SetPalette(2)
        Unknown2005()
        Unknown3033()
    sprite('vrkkef_denpa_00', 2)
    sprite('vrkkef_denpa_01', 2)
    sprite('vrkkef_denpa_02', 2)
    sprite('vrkkef_denpa_03', 2)

@State
def efkk_denpa2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        GFX_SetPalette(2)
        Unknown3033()
    sprite('vrkkef_denpa_00', 2)
    sprite('vrkkef_denpa_01', 2)
    sprite('vrkkef_denpa_02', 2)
    sprite('vrkkef_denpa_03', 2)

@Subroutine
def Drive_SetPosition():
    ProjectileHitWall(1)
    Unknown23023()
    Unknown2003(1)
    Unknown23022(1)
    GFX_SetPalette(0)
    Unknown2019(500)
    GFX_OffsetX(260000)
    GFX_OffsetY(200000)

    def upon_33():
        Unknown23032(10)
        Unknown23033(90)
        if (SLOT_23 <= 100000):
            GFX_OffsetY(100000)

    def upon_34():
        Unknown23032(50)
        Unknown23033(90)
        if (SLOT_23 <= 100000):
            GFX_OffsetY(100000)

    def upon_35():
        Unknown23032(90)
        Unknown23033(90)
        if (SLOT_23 <= 100000):
            GFX_OffsetY(100000)

    def upon_36():
        Unknown23032(10)
        Unknown23033(50)

    def upon_38():
        Unknown23032(90)
        Unknown23033(50)

    def upon_39():
        Unknown23032(10)
        Unknown23033(10)

    def upon_40():
        Unknown23032(50)
        Unknown23033(10)

    def upon_41():
        Unknown23032(90)
        Unknown23033(10)

@State
def efkk_Drive():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(4)
        Damage(600)
        Hitstop(0)
        hitstun(24)
        BonusProrationPct(110)
        Unknown11001(10, 10, 15)
        AirHitstunAnimation(18)
        AirUntechableTime(70)
        PushbackX(8000)
        AirPushbackX(1000)
        YImpluseBeforeWallbounce(1600)
        Unknown11056(1)
        OnlyInHitstun(1)
        Unknown11066(1)
        Unknown11062(1)
        Unknown11063(1)
        Unknown12052(1)
        StarterRating(3)
        callSubroutine('Drive_SetPosition')
        SLOT_5 = 1
        PhysicsPull(999, 5000, 3000)

        def upon_3():
            if (not SLOT_21):
                sendToLabel(0)
            if (SLOT_5 == 2):
                Unknown7015()
                PhysicsPull(0, 0, 0)
                GFX_Unload('efkk_203')
                GFX_Unload('efkk_203_yugami_loop')
                sendToLabel(10)
                if SLOT_2:
                    Unknown21012('SpinAssault', 33)
            if (SLOT_5 == 3):
                Unknown7015()
                PhysicsPull(0, 0, 0)
                GFX_Unload('efkk_203')
                GFX_Unload('efkk_203_yugami_loop')
                sendToLabel(13)
                if SLOT_2:
                    Unknown21012('SpinAssault', 33)
                clearUponHandler(3)
                clearUponHandler(17)
                sendToLabelUpon(47, 0)

        def upon_37():
            sendToLabel(0)

        def upon_44():
            sendToLabel(0)
        loopRelated(17, 240)
        sendToLabelUpon(17, 0)

        def upon_STATE_END():
            SLOT_5 = 0
    sprite('vrkkef203weapon00', 1)
    Unknown3001(0)
    GFX_SetPalette(0)
    sprite('vrkkef203weapon00', 1)
    Unknown3001(255)
    GFX_0('efkk_203', 0)
    GFX_1('kkef_203appear', 0)
    GFX_0('efkk_203_yugami_loop', 0)
    sprite('vrkkef203weapon01', 3)
    sprite('vrkkef203weapon02', 3)
    sprite('vrkkef203weapon03', 3)
    sprite('vrkkef203weapon04', 3)
    SFX_3('kkse_08')
    sprite('vrkkef203weapon05', 3)
    Unknown7014('kkse_09')
    label(100)
    sprite('vrkkef203weapon00', 3)
    sprite('vrkkef203weapon01', 3)
    sprite('vrkkef203weapon02', 3)
    sprite('vrkkef203weapon03', 3)
    sprite('vrkkef203weapon04', 3)
    sprite('vrkkef203weapon05', 3)
    loopRest()
    gotoLabel(100)
    label(10)
    clearUponHandler(3)
    clearUponHandler(17)
    sendToLabelUpon(47, 0)
    sprite('keep', 30)
    sendToLabelUpon(32, 11)
    label(11)
    sprite('vrkkef203weapon05', 111)
    sendToLabelUpon(26, 12)
    label(13)
    sprite('vrkkef203weapon05', 10)
    label(12)
    sprite('vrkkef203weapon06', 3)
    clearUponHandler(26)
    clearUponHandler(44)
    clearUponHandler(47)
    GFX_0('efkk_203_repuls', -1)
    GFX_0('efkk_203_yugami_group', -1)
    Unknown21012('efkk_fireball_Hontai', 32)
    Unknown21012('efkk_UltraSokidan_Hontai', 32)
    Unknown21012('efkk_UltraSokidan_Hontai_OD', 32)
    SFX_3('kkse_10')
    Unknown2003(0)
    PhysicsPull(6, -50000, -30000)
    SLOT_31 = (SLOT_31 + (-1))
    Unknown2037(1)
    sprite('vrkkef203weapon07', 4)
    sprite('vrkkef203weapon08', 20)
    Unknown2003(1)
    Unknown2037(0)
    sprite('vrkkef203weapon06', 8)
    GFX_Unload('efkk_203_repuls')
    sprite('vrkkef203weapon03', 30)
    PhysicsPull(0, 0, 0)
    clearUponHandler(3)
    clearUponHandler(17)
    clearUponHandler(44)
    clearUponHandler(47)
    clearUponHandler(26)
    clearUponHandler(37)
    Unknown7015()
    PhysicsPull(0, 0, 0)
    SLOT_5 = 3
    GFX_Unload('efkk_203')
    GFX_Unload('efkk_203_yugami_loop')
    GFX_Unload('efkk_203_repuls')
    Unknown3004(-4)
    ExitState()
    label(0)
    sprite('vrkkef203weapon00', 10)
    PhysicsPull(0, 0, 0)
    clearUponHandler(3)
    clearUponHandler(17)
    clearUponHandler(44)
    clearUponHandler(47)
    clearUponHandler(26)
    clearUponHandler(37)
    Unknown7015()
    PhysicsPull(0, 0, 0)
    SLOT_5 = 3
    GFX_Unload('efkk_203')
    GFX_Unload('efkk_203_yugami_loop')
    GFX_Unload('efkk_203_repuls')
    sprite('vrkkef203weapon01', 10)
    sprite('vrkkef203weapon02', 10)
    sprite('vrkkef203weapon03', 30)
    Unknown3004(-4)

@State
def efkk_Drive_OD():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(4)
        Damage(900)
        Hitstop(0)
        AttackP2(100)
        hitstun(24)
        MinimumDamagePct(0)
        BonusProrationPct(120)
        Unknown11001(10, 15, 20)
        AirHitstunAnimation(18)
        AirUntechableTime(120)
        PushbackX(8000)
        AirPushbackX(1000)
        StarterRating(3)
        YImpluseBeforeWallbounce(1600)
        Unknown11056(1)
        OnlyInHitstun(1)
        Unknown11066(1)
        Unknown11062(1)
        Unknown11063(1)
        Unknown12052(1)
        callSubroutine('Drive_SetPosition')
        SLOT_5 = 1
        PhysicsPull(999, 10000, 6000)

        def upon_3():
            Unknown21012('SpinAssault', 32)
            if (not SLOT_21):
                sendToLabel(0)
            if (SLOT_5 == 2):
                Unknown7015()
                PhysicsPull(0, 0, 0)
                GFX_Unload('efkk_203')
                GFX_Unload('efkk_203_yugami_loop')
                sendToLabel(10)
                if SLOT_2:
                    Unknown21012('SpinAssault', 33)
            if (SLOT_5 == 3):
                Unknown7015()
                PhysicsPull(0, 0, 0)
                GFX_Unload('efkk_203')
                GFX_Unload('efkk_203_yugami_loop')
                sendToLabel(13)
                if SLOT_2:
                    Unknown21012('SpinAssault', 33)
                clearUponHandler(3)
                clearUponHandler(17)
                sendToLabelUpon(47, 0)

        def upon_37():
            sendToLabel(0)

        def upon_44():
            sendToLabel(0)
        loopRelated(17, 360)
        sendToLabelUpon(17, 0)

        def upon_STATE_END():
            SLOT_5 = 0
    sprite('vrkkef203weapon00', 1)
    Unknown3001(0)
    GFX_SetPalette(0)
    sprite('vrkkef203weapon00', 1)
    Unknown3001(255)
    GFX_0('efkk_203', 0)
    GFX_1('kkef_203appear', 0)
    GFX_0('efkk_203_yugami_loop', 0)
    sprite('vrkkef203weapon01', 2)
    sprite('vrkkef203weapon02', 2)
    sprite('vrkkef203weapon03', 2)
    sprite('vrkkef203weapon04', 2)
    SFX_3('kkse_08')
    sprite('vrkkef203weapon05', 2)
    GFX_Unload('efkk_203b')
    GFX_0('efkk_203', -1)
    Unknown7014('kkse_09')
    label(100)
    sprite('vrkkef203weapon00', 2)
    sprite('vrkkef203weapon01', 2)
    sprite('vrkkef203weapon02', 2)
    sprite('vrkkef203weapon03', 2)
    sprite('vrkkef203weapon04', 2)
    sprite('vrkkef203weapon05', 2)
    loopRest()
    gotoLabel(100)
    label(10)
    clearUponHandler(3)
    clearUponHandler(17)
    sendToLabelUpon(47, 0)
    sprite('keep', 30)
    sendToLabelUpon(32, 11)
    label(11)
    sprite('vrkkef203weapon05', 111)
    sendToLabelUpon(26, 12)
    label(13)
    sprite('vrkkef203weapon05', 10)
    label(12)
    sprite('vrkkef203weapon06', 3)
    clearUponHandler(26)
    clearUponHandler(44)
    clearUponHandler(47)
    GFX_0('efkk_203_repuls', -1)
    GFX_0('efkk_203_yugami_group', -1)
    Unknown21012('efkk_fireball_Hontai', 32)
    Unknown21012('efkk_UltraSokidan_Hontai', 32)
    Unknown21012('efkk_UltraSokidan_Hontai_OD', 32)
    SFX_3('kkse_10')
    Unknown2003(0)
    PhysicsPull(6, -50000, -30000)
    SLOT_31 = (SLOT_31 + (-1))
    Unknown2037(1)
    sprite('vrkkef203weapon07', 4)
    sprite('vrkkef203weapon08', 20)
    Unknown2003(1)
    Unknown2037(0)
    sprite('vrkkef203weapon06', 8)
    GFX_Unload('efkk_203_repuls')
    sprite('vrkkef203weapon03', 30)
    PhysicsPull(0, 0, 0)
    clearUponHandler(3)
    clearUponHandler(17)
    clearUponHandler(44)
    clearUponHandler(47)
    clearUponHandler(26)
    clearUponHandler(37)
    Unknown7015()
    PhysicsPull(0, 0, 0)
    SLOT_5 = 3
    GFX_Unload('efkk_203')
    GFX_Unload('efkk_203_yugami_loop')
    GFX_Unload('efkk_203_repuls')
    Unknown3004(-4)
    ExitState()
    label(0)
    sprite('vrkkef203weapon00', 10)
    PhysicsPull(0, 0, 0)
    clearUponHandler(3)
    clearUponHandler(17)
    clearUponHandler(44)
    clearUponHandler(47)
    clearUponHandler(26)
    clearUponHandler(37)
    Unknown7015()
    PhysicsPull(0, 0, 0)
    SLOT_5 = 3
    GFX_Unload('efkk_203')
    GFX_Unload('efkk_203_yugami_loop')
    GFX_Unload('efkk_203_repuls')
    sprite('vrkkef203weapon01', 10)
    sprite('vrkkef203weapon02', 10)
    sprite('vrkkef203weapon03', 30)
    Unknown3001(128)
    Unknown3004(-4)

@State
def efkk_203():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
    label(0)
    sprite('null', 6)
    GFX_1('kkef_203gravi', -1)
    gotoLabel(0)

@State
def efkk_203_repuls():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(2)
    GFX_0('efkk_203_repuls_yugami', -1)
    GFX_1('kkef_203repuls_b', -1)
    label(0)
    sprite('null', 5)
    GFX_1('kkef_203repuls', -1)
    gotoLabel(0)

@State
def efkk_203_yugami_loop():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
    label(0)
    sprite('null', 15)
    GFX_0('efkk_203_yugami', -1)
    GFX_1('kkef_203gravi_b', -1)
    sprite('null', 15)
    GFX_0('efkk_203_yugami', -1)
    gotoLabel(0)

@State
def efkk_203_yugami():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown3032()
        Unknown3057(1)
        Unknown3058(50000)
        GFX_Scale(1000)
        Unknown3001(0)
    sprite('vrdist10', 32)
    Unknown3004(8)
    Unknown1099(-10)
    Unknown1108(3000)
    Unknown1077(-90000, 90000)
    sprite('vrdist10', 32)
    Unknown3004(-8)

@State
def efkk_203_yugami_group():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('null', 1)
    GFX_0('efkk_203_repuls_yugami', -1)
    sprite('null', 1)
    GFX_0('efkk_203_repuls_yugami', -1)

@State
def efkk_203_repuls_yugami():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3057(1)
        Unknown3058(75000)
        GFX_Scale(500)
        Unknown3001(255)
    sprite('vrdist10', 10)
    Unknown1099(250)

@State
def efkk_403_TrapA():

    def upon_IMMEDIATE():
        Unknown23023()
        ProjectileHitWall(1)
        GFX_OffsetX(110000)
        Unknown23022(1)
        GFX_SetPalette(0)
        SLOT_33 = 0

        def upon_STATE_END():
            SLOT_33 = 1
        sendToLabelUpon(44, 0)
        sendToLabelUpon(41, 0)
    sprite('kk403_h00', 1)
    physicsYImpulse(-10000)
    sprite('kk403_h00', 1)
    endMomentum(1)
    GFX_1('kkef403_smoke01', 0)
    SFX_3('kkse_02')
    sprite('kk403_h01', 1)
    sprite('kk403_h02', 1)
    sprite('kk403_h03', 1)
    sprite('kk403_h04', 1)
    sprite('kk403_h05', 1)
    sprite('kk403_h06', 1)
    sprite('kk403_h07', 1)
    sprite('kk403_h08', 1)
    SFX_3('kkse_03')
    sprite('kk403_h09', 1)
    sprite('kk403_h10', 1)
    sprite('kk403_h11', 1)
    sprite('kk403_h12', 1)
    sprite('kk403_h13', 1)
    GFX_0('efkk_403_beam', -1)
    sprite('kk403_h13', 6)
    GFX_0('efkk_403A_Atk', -1)
    sprite('kk403_h13', 30)
    Unknown21012('efkk_403_beam', 32)
    sprite('kk403_h12', 3)
    sprite('kk403_h11', 3)
    sprite('kk403_h10', 3)
    sprite('kk403_h09', 3)
    sprite('kk403_h08', 3)
    sprite('kk403_h07', 3)
    sprite('kk403_h06', 3)
    sprite('kk403_h05', 3)
    sprite('kk403_h04', 30)
    sprite('kk403_h04', 36)
    Unknown3004(-6)
    loopRest()
    ExitState()
    label(0)
    endMomentum(1)
    Unknown1006(0)
    clearUponHandler(3)
    clearUponHandler(44)
    clearUponHandler(47)
    clearUponHandler(41)
    Unknown2003(1)
    sprite('keep', 3)
    sprite('kk403_h08', 3)
    sprite('kk403_h07', 3)
    sprite('kk403_h06', 3)
    sprite('kk403_h05', 3)
    sprite('null', 45)
    Unknown21012('efkk_403_beam', 32)
    GFX_1('kkef403koware_05', -1)

@State
def efkk_403_TrapB():

    def upon_IMMEDIATE():
        Unknown23023()
        ProjectileHitWall(1)
        GFX_OffsetX(110000)
        Unknown2003(1)
        Unknown23022(1)
        GFX_SetPalette(0)
        SLOT_33 = 0

        def upon_STATE_END():
            SLOT_33 = 1
        sendToLabelUpon(44, 0)
        sendToLabelUpon(41, 0)
    sprite('kk403_h00', 10)
    physicsYImpulse(-1000)
    sprite('kk403_h00', 2)
    endMomentum(1)
    GFX_1('kkef403_smoke01', 0)
    SFX_3('kkse_02')
    sprite('kk403_h01', 2)
    sprite('kk403_h02', 2)
    sprite('kk403_h03', 2)
    sprite('kk403_h04', 2)
    sprite('kk403_h05', 2)
    sprite('kk403_h06', 2)
    sprite('kk403_h07', 2)
    sprite('kk403_h08', 2)
    SFX_3('kkse_03')
    sprite('kk403_h09', 2)
    sprite('kk403_h10', 2)
    sprite('kk403_h11', 2)
    sprite('kk403_h12', 2)
    sprite('kk403_h13', 240)

    def upon_3():
        if (SLOT_19 < 250000):
            sendToLabel(1)
        if (not SLOT_21):
            sendToLabel(0)
    label(1)
    sprite('kk403_h13', 20)
    Unknown23119(16777215, 5, 20)
    clearUponHandler(3)
    sprite('kk403_h13', 1)
    GFX_0('efkk_403_beam', -1)
    clearUponHandler(44)
    clearUponHandler(47)
    sprite('kk403_h13', 16)
    Unknown23119(0, 0, 0)
    GFX_0('efkk_403B_Atk', -1)
    sprite('kk403_h13', 10)
    Unknown21012('efkk_403_beam', 32)
    sprite('kk403_h13', 20)
    sprite('kk403_h12', 3)
    sprite('kk403_h11', 3)
    sprite('kk403_h10', 3)
    sprite('kk403_h09', 3)
    sprite('kk403_h08', 3)
    sprite('kk403_h07', 3)
    sprite('kk403_h06', 3)
    sprite('kk403_h05', 3)
    sprite('kk403_h04', 30)
    sprite('kk403_h04', 36)
    Unknown3004(-6)
    loopRest()
    ExitState()
    label(0)
    endMomentum(1)
    Unknown1006(0)
    clearUponHandler(3)
    clearUponHandler(44)
    clearUponHandler(47)
    clearUponHandler(41)
    Unknown2003(1)
    sprite('keep', 3)
    sprite('kk403_h08', 3)
    sprite('kk403_h07', 3)
    sprite('kk403_h06', 3)
    sprite('kk403_h05', 3)
    sprite('null', 45)
    Unknown21012('efkk_403_beam', 32)
    GFX_1('kkef403koware_05', -1)

@State
def efkk_403A_Atk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(860)
        ChipPercentage(8)
        Hitstop(0)
        Unknown11001(7, 7, 27)
        AirPushbackX(0)
        AttackP1(80)
        AirUntechableTime(50)
        GroundedHitstunAnimation(14)
        AirHitstunAnimation(14)
        StarterRating(3)
        Unknown12052(1)
        Unknown1064(5000)
        Unknown4011(3)    
    sprite('kk403_Atkcol', 10)

@State
def efkk_403B_Atk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(450)
        Hitstop(0)
        Unknown11001(7, 7, 27)
        PushbackX(8000)
        AirPushbackX(0)
        AttackP1(80)
        ChipPercentage(8)
        AirUntechableTime(60)
        Unknown11092(1)
        GroundedHitstunAnimation(14)
        AirHitstunAnimation(14)
        StarterRating(3)
        Unknown12052(1)
        Unknown1064(5000)
        Unknown4011(3)
    sprite('kk403_Atkcol', 2)
    RefreshMultihit()
    sprite('kk403_Atkcol', 2)
    RefreshMultihit()
    sprite('kk403_Atkcol', 2)
    RefreshMultihit()
    sprite('kk403_Atkcol', 2)
    RefreshMultihit()
    sprite('kk403_Atkcol', 2)
    RefreshMultihit()
    sprite('kk403_Atkcol', 2)
    RefreshMultihit()

@State
def efkk_403_beam():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4003('kkef403_beam00', '')
        Unknown3032()
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    GFX_1('kkef403jizoku_00', -1)
    ScreenShake(5000, 5000)
    GFX_0('efkk_ThunderTakusan', -1)
    label(0)
    sprite('null', 5)
    Unknown3001(0)
    GFX_1('kkef403end_00', -1)

@State
def efkk_ThunderTakusan():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
    label(0)
    sprite('null', 3)
    GFX_0('efkk_403_beamThunder00', -1)
    SFX_0('013_thunder_0')
    GFX_0('efkk_403_beamThunder01', -1)
    GFX_0('efkk_403_beamThunder02', -1)
    sprite('null', 3)
    GFX_0('efkk_403_beamThunder00', -1)
    Unknown36(1)
    Unknown2005()
    Unknown35()
    GFX_0('efkk_403_beamThunder01', -1)
    Unknown36(1)
    Unknown2005()
    Unknown35()
    GFX_0('efkk_403_beamThunder02', -1)
    Unknown36(1)
    Unknown2005()
    Unknown35()
    gotoLabel(0)

@State
def efkk_403_beamThunder00():

    def upon_IMMEDIATE():
        Unknown4003('kkef403_beam01', '')
        Unknown4015()
        Unknown3032()
    sprite('null', 8)
    Unknown1059(-30)
    Unknown1011(0, 650000)
    Unknown1062(-500, 100)

@State
def efkk_403_beamThunder01():

    def upon_IMMEDIATE():
        Unknown4003('kkef403_beam01', '')
        Unknown4015()
        Unknown3032()
    sprite('null', 8)
    Unknown1059(-30)
    Unknown1011(650000, 1300000)
    Unknown1062(-500, 100)

@State
def efkk_403_beamThunder02():

    def upon_IMMEDIATE():
        Unknown4003('kkef403_beam01', '')
        Unknown4015()
        Unknown3032()
    sprite('null', 8)
    Unknown1059(-30)
    Unknown1011(1300000, 1950000)
    Unknown1062(-500, 100)

@Subroutine
def Fireball_Hontai():

    def upon_3():
        if SLOT_2:
            if (SLOT_5 == 1):
                Unknown23001(300, 300)
            if (SLOT_5 >= 2):

                def upon_32():
                    Unknown23001(200, 40)
                    clearUponHandler(3)
                    clearUponHandler(32)
                    sendToLabel(1)
        if (not SLOT_21):
            clearUponHandler(3)
            sendToLabel(99)
    SLOT_32 = 0

    def upon_STATE_END():
        SLOT_32 = 1

    def upon_33():
        sendToLabel(10)

    def upon_34():
        sendToLabel(20)

    def upon_35():
        sendToLabel(30)

    def upon_5():
        if SLOT_5:
            YAccel(-50)
        else:
            clearUponHandler(5)
            sendToLabel(99)
    if (SLOT_52 == 1):
        FireBall(6, 1, 1, 1, 6, 0, 6, 0)
        loopRelated(17, 240)
    if (SLOT_53 == 1):
        FireBall(12, 1, 1, 1, 1, 0, 0, 0)
        loopRelated(17, 360)
    if (SLOT_54 == 1):
        FireBall(18, 1, 1, 1, 1, 0, 0, 0)
        loopRelated(17, 480)

    def upon_54():
        sendToLabel(99)

    def upon_17():
        sendToLabel(99)

    def upon_41():
        sendToLabel(99)

@State
def efkk_fireball_Hontai():

    def upon_IMMEDIATE():
        Unknown2010()
        SLOT_52 = 1
        callSubroutine('Fireball_Hontai')
        AttackLevel_(2)
        Damage(360)
        ChipPercentage(8)
        AttackP1(80)
        AttackP2(75)
        Unknown11092(1)
        AirUntechableTime(30)
        Hitstop(4)
        FireFX(1)
        Unknown11056(0)
        StarterRating(3)
        Unknown12052(1)
        FireFX(1)
        GFX_0('efkk_fireballStart', -1)
        if SLOT_137:
            DamageMultiplier(80)
    label(10)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    RefreshMultihit()
    GFX_OffsetY(150000)
    physicsYImpulse(12000)
    physicsXImpulse(2000)
    setGravity(400)
    ProjectileHitWall(0)
    GFX_0('efkk_FireBallroop', -1)
    Unknown2037(1)
    loopRest()
    gotoLabel(5)
    label(20)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    RefreshMultihit()
    GFX_OffsetY(150000)
    physicsYImpulse(12000)
    physicsXImpulse(4000)
    setGravity(200)
    ProjectileHitWall(0)
    GFX_0('efkk_FireBallroop', -1)
    Unknown2037(1)
    loopRest()
    gotoLabel(5)
    label(30)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    RefreshMultihit()
    GFX_OffsetY(150000)
    physicsYImpulse(12000)
    physicsXImpulse(8000)
    setGravity(200)
    ProjectileHitWall(0)
    GFX_0('efkk_FireBallroop', -1)
    Unknown2037(1)
    loopRest()
    gotoLabel(5)
    label(5)
    sprite('vrkkef402Atk', 2)
    RefreshMultihit()
    GFX_0('efkk_fireDust00', -1)
    if SLOT_95:
        GFX_1('kkef402jizoku_2p', -1)
    else:
        GFX_1('kkef402jizoku', -1)
    sprite('vrkkef402Atk', 2)
    RefreshMultihit()
    GFX_0('efkk_fireDust01', -1)
    loopRest()
    gotoLabel(5)
    label(1)
    sprite('vrkkef402Atk', 2)
    SLOT_55 = 14
    RefreshMultihit()
    AttackLevel_(4)
    Damage(750)
    blockstun(20)
    Unknown9287()
    Unknown11092(0)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirUntechableTime(60)
    StarterRating(3)
    Wallbounce(1)
    AirHitstunAfterWallbounce(60)
    Hitstop(5)
    Unknown11001(10, 10, 10)
    GFX_0('efkk_fireDust00', -1)
    if SLOT_95:
        GFX_1('kkef402jizoku_2p', -1)
    else:
        GFX_1('kkef402jizoku', -1)
    sprite('vrkkef402Atk', 3)
    GFX_0('efkk_fireDust01', -1)
    label(2)
    sprite('vrkkef402Atk', 3)
    GFX_0('efkk_fireDust00', -1)
    if SLOT_95:
        GFX_1('kkef402jizoku_2p', -1)
    else:
        GFX_1('kkef402jizoku', -1)
    sprite('vrkkef402Atk', 3)
    GFX_0('efkk_fireDust01', -1)
    SLOT_55 = (SLOT_55 + (-1))
    Unknown19(99, 2, 55)
    loopRest()
    gotoLabel(2)
    label(99)
    sprite('null', 3)
    Unknown2037(0)
    endMomentum(1)
    Unknown21012('efkk_FireBallroop', 32)
    Unknown4003('kkef402_fire04', '')
    Unknown4015()
    Unknown1077(0, 360000)
    sprite('null', 3)
    if SLOT_95:
        GFX_1('kkef402hit_03_2p', -1)
    else:
        GFX_1('kkef402hit_03', -1)
    GFX_0('efkk_fireDust01', -1)
    GFX_0('efkk_fireDust02', -1)

@State
def efkk_FireBallroop():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown23015(1)
        GFX_Scale(700)
        if SLOT_95:
            GFX_SetPalette(4)
        else:
            GFX_SetPalette(2)
        sendToLabelUpon(32, 1)
    sprite('vrkkef402_00', 1)
    label(0)
    sprite('vrkkef402_00', 3)
    SFX_3('kkse_13')
    sprite('vrkkef402_01', 3)
    sprite('vrkkef402_02', 3)
    sprite('vrkkef402_03', 3)
    gotoLabel(0)
    label(1)
    sprite('vrkkef402_03', 2)

@State
def efkk_fireDust00():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown3032()
        GFX_Scale(850)
        Unknown3001(150)
        if SLOT_95:
            Unknown4003('kkef402_fire03_2p', '')
            Unknown4015()
        else:
            Unknown4003('kkef402_fire03', '')
            Unknown4015()
    sprite('null', 10)
    Unknown1099(-30)
    Unknown1074(-5000)
    Unknown1077(0, 360000)

@State
def efkk_fireDust01():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown3032()
        Unknown3001(150)
        GFX_Scale(1000)
        if SLOT_95:
            Unknown4003('kkef402_fire03_2p', '')
            Unknown4015()
        else:
            Unknown4003('kkef402_fire03', '')
            Unknown4015()
    sprite('null', 10)
    Unknown1099(-30)
    Unknown1074(5000)
    Unknown1077(0, 360000)

@State
def efkk_fireDust02():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown3032()
        Unknown3001(150)
        GFX_Scale(1000)
        if SLOT_95:
            Unknown4003('kkef402_fire03_2p', '')
            Unknown4015()
        else:
            Unknown4003('kkef402_fire03', '')
            Unknown4015()
    sprite('null', 10)
    Unknown1099(30)
    Unknown1077(0, 360000)
    SFX_0('015_blaze_0')

@State
def efkk_fireballStart():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(3)
        Unknown3032()
        GFX_Scale(1200)
        if SLOT_95:
            Unknown4003('kkef402_fire00_2p', '')
            Unknown4015()
        else:
            Unknown4003('kkef402_fire00', '')
            Unknown4015()
    sprite('null', 10)
    if SLOT_95:
        GFX_1('kkef402star_fire_2p', -1)
    else:
        GFX_1('kkef402star_fire', -1)
    sprite('null', 10)
    Unknown3001(0)
    GFX_0('efkk_fireballStart01', -1)
    loopRest()
    Unknown13(23)

@State
def efkk_fireballStart01():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(3)
        Unknown3032()
        GFX_Scale(1200)
        if SLOT_95:
            Unknown4003('kkef402_fire01_2p', '')
            Unknown4015()
        else:
            Unknown4003('kkef402_fire01', '')
            Unknown4015()
    sprite('null', 10)

@State
def efkk_freezwind00():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('kkef401_freezewind00', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(0)
        Unknown1056(1300)
        GFX_Rotation(15000)
        sendToLabelUpon(32, 1)
    sprite('null', 5)
    GFX_1('kkef401icewind_start', -1)
    Unknown3004(26)
    sprite('null', 10)
    Unknown3004(26)
    label(0)
    sprite('null', 20)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown3004(-51)

@State
def efkk_401weapon():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(3)
        GFX_SetPalette(0)
        Unknown3032()
        GFX_OffsetX(-192000)
        GFX_OffsetY(148000)
    sprite('vrkkef401wpn00', 3)
    sprite('vrkkef401wpn01', 3)
    sprite('vrkkef401wpn02', 3)

@State
def efkk_401weapon2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(3)
        GFX_SetPalette(0)
        Unknown3032()
        Unknown2019(100)
        GFX_OffsetX(-192000)
        GFX_OffsetY(148000)
    sprite('vrkkef401wpn00b', 3)
    sprite('vrkkef401wpn01b', 3)
    sprite('vrkkef401wpn02b', 3)

@State
def efkk_401_hole():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        GFX_SetPalette(3)
        Unknown2019(500)
        GFX_OffsetX(-192000)
        GFX_OffsetY(148000)
        GFX_Scale(975)
    sprite('vrkkef_hole_a10', 4)
    sprite('vrkkef_hole_a11', 4)
    sprite('vrkkef_hole_a00', 24)
    GFX_0('efkk_401_electric', -1)
    sprite('vrkkef_hole_a01', 4)
    sprite('vrkkef_hole_a02', 4)
    sprite('vrkkef_hole_a03', 4)
    sprite('vrkkef_hole_a20', 4)
    GFX_Unload('efkk_401_electric')
    sprite('vrkkef_hole_a21', 4)

@State
def efkk_401_electric():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4024(2)
        Unknown4013(2)
        Unknown4006(2)
        Unknown13044(1)
        GFX_SetPalette(3)
        Unknown3033()
        Unknown2019(499)
    label(0)
    sprite('vrkkef_electric_00', 2)
    sprite('vrkkef_electric_01', 2)
    sprite('vrkkef_electric_02', 2)
    gotoLabel(0)

@State
def efkk_401tama():

    def upon_IMMEDIATE():
        Unknown2010()
        Damage(80)
        AttackP2(98)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirUntechableTime(60)
        WallbounceReboundTime(10)
        Unknown9202(20)
        PushbackX(24800)
        Hitstop(0)
        Unknown11057(400)
        Unknown11068(1)
        Unknown11108(3)
        AirPushbackX(30000)
        AirPushbackY(2000)

        def upon_ON_HIT_OR_BLOCK():
            Unknown2003(1)
            sendToLabel(1)
            Unknown21012('Freeze_Shot', 32)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        GFX_Scale(800)
        GFX_2('kkef401tama_mato')
        sendToLabelUpon(32, 1)
        sendToLabelUpon(7, 1)

        def upon_33():
            SFX_0('016_explode_0')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vr_blt', 120)
    GFX_1('kkef401tamacircle00', -1)
    IsInvisibility(1)
    RefreshMultihit()
    Unknown1025(85000, 100000)
    Unknown1011(-80000, 80000)
    label(1)
    sprite('null', 5)
    physicsXImpulse(0)
    Unknown3004(-51)

@State
def efkk_Mazleflash():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('kkef401mazle_mato')
        Unknown3032()
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    GFX_0('efkk_401tama', -1)
    Unknown21007(1, 33)
    Unknown48(23, 2, 52, 3, 2, 57)
    if (not SLOT_52):
        Unknown13(23)
    sprite('null', 2)
    GFX_0('efkk_401tama', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Unknown3004(-51)

@State
def efkk_BLTtakusan():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        sendToLabelUpon(32, 1)
    sprite('null', 1)
    label(0)
    sprite('null', 2)
    GFX_0('efkk_BLT', -1)
    Unknown48(23, 2, 52, 3, 2, 57)
    if (not SLOT_52):
        Unknown13(23)
    sprite('null', 2)
    GFX_0('efkk_BLT', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 8)

@State
def efkk_BLT():

    def upon_IMMEDIATE():
        GFX_SetPalette(2)

        def upon_LANDING():
            setGravity(1600)
            physicsYImpulse(10000)
            physicsXImpulse(-10000)
            SFX_3('nose_02')
    sprite('vr_blt', 40)
    Unknown1074(10000)
    Unknown1077(0, 360000)
    SFX_3('nose_02')
    setGravity(1600)
    physicsYImpulse(10000)
    physicsXImpulse(-10000)
    Unknown1025(-1000, 1000)
    Unknown1026(-1000, 5000)

@State
def efkk401_micile():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Damage(500)
        Unknown11092(1)
        MinimumDamagePct(100)
        Hitstop(1)
        AirUntechableTime(45)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(60000)
        YImpluseBeforeWallbounce(1800)
        Unknown11062(1)
        Unknown11068(1)
        Unknown1086(22)
        Unknown3032()
        loopRelated(17, 60)
        sendToLabelUpon(17, 1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrkkef401_micile00', 15)
    RefreshMultihit()
    GFX_1('kkef401micileroot_02', -1)
    GFX_0('efkk401_micilefire', -1)
    physicsYImpulse(10000)
    setGravity(-500)
    SFX_3('kkse_24')
    sprite('vrkkef401_micile00', 3)
    Damage(100)
    RefreshMultihit()
    Unknown11062(0)
    Unknown1039(500)
    AirPushbackY(30000)
    label(0)
    sprite('vrkkef401_micile00', 3)
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrkkef401_micile00', 1)

@State
def efkk401_micile_OD():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Damage(600)
        Unknown11092(1)
        MinimumDamagePct(100)
        Hitstop(1)
        AirUntechableTime(45)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(60000)
        YImpluseBeforeWallbounce(1800)
        Unknown11062(1)
        Unknown11068(1)
        Unknown9001(4)
        Unknown1086(22)
        Unknown3032()
        loopRelated(17, 60)
        sendToLabelUpon(17, 1)

        def upon_12():
            Unknown2038(1)

        def upon_3():
            if (SLOT_2 >= 5):
                sendToLabel(1)
                clearUponHandler(3)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrkkef401_micile00', 15)
    RefreshMultihit()
    GFX_1('kkef401micileroot_02', -1)
    GFX_0('efkk401_micilefire', -1)
    physicsYImpulse(10000)
    setGravity(-500)
    SFX_3('kkse_24')
    sprite('vrkkef401_micile00', 3)
    Damage(100)
    RefreshMultihit()
    Unknown11062(0)
    Unknown1039(500)
    AirPushbackY(33000)
    label(0)
    sprite('vrkkef401_micile00', 3)
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrkkef401_micile00', 2)
    Unknown23027()
    sprite('vrkkef401_micile00', 1)
    GFX_0('efkk401_LastBomb', -1)

@State
def efkk401_micilefire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('kkef401micilefire_mato')
        GFX_OffsetY(4294577296)
        GFX_Scale(1500)
        Unknown3001(0)
    sprite('null', 15)
    Unknown3004(51)
    label(0)
    sprite('null', 2)
    GFX_1('kkef401micilesmoke_01', -1)
    gotoLabel(0)

@State
def efkk401_LastBomb():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Damage(600)
        MinimumDamagePct(100)
        AttackP2(100)
        Hitstop(1)
        AirUntechableTime(60)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(45000)
        YImpluseBeforeWallbounce(1800)
        Unknown9001(4)
        FireFX(1)
        Unknown4003('kkef401_bomb', '')
        Unknown3032()
        GFX_Scale(1000)
        Unknown1073(20000)
        Unknown2054(1)
        Unknown23015(1)
        IsInvisibility(1)
    sprite('vrkkef401_micile00', 3)
    SFX_0('015_blaze_2')
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    SFX_0('025_cleanhit_grap')
    sprite('vrkkef401_micile00', 3)
    Unknown1097(250)
    sprite('vrkkef401_micile00', 3)
    Unknown1097(150)
    PFX('kkef_401_bloom', -1)
    ScreenShake(15000, 15000)
    sprite('vrkkef401_micile00', 9)
    Unknown1097(100)

@State
def efkk401_minigunbrake():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('vrkkef401_brake', 20)
    setGravity(1000)
    physicsYImpulse(5000)
    physicsXImpulse(-8000)
    sprite('vrkkef401_brake', 1)
    setGravity(0)
    GFX_1('kkef403koware_03', 0)
    GFX_1('kkef403koware_03', 1)

@State
def efkk401_reitouhou():

    def upon_IMMEDIATE():

        def upon_LANDING():
            setGravity(1600)
            physicsYImpulse(10000)
            physicsXImpulse(-10000)
        sendToLabelUpon(2, 0)
    sprite('kk401_11z', 40)
    Unknown1074(5000)
    Unknown1077(0, 360000)
    setGravity(1600)
    physicsYImpulse(10000)
    physicsXImpulse(-10000)
    Unknown1025(-1000, 1000)
    Unknown1026(-1000, 5000)
    label(0)
    sprite('null', 10)
    PFX_Scale(800)
    PFX('kkef403koware_05', -1)

@State
def efkk401_MisileAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        AirUntechableTime(600)
        Hitstop(0)
        PushbackX(0)
        AirPushbackX(0)
        AirPushbackY(0)
        GroundUntechableTime(1)
        Unknown11066(1)
        ForceCounterHit(1)
        Unknown11084(1)
        Unknown11050(9, '')
        Unknown11083(1)
        Unknown11064(1)
        Unknown11080(1)
        Unknown11068(1)

        def upon_12():
            Unknown21012('Freeze_Shot', 35)
    sprite('vrkkef401_MisileAtk', 1)

@State
def efkk400A_fire00():

    def upon_IMMEDIATE():
        Unknown3033()
        GFX_SetPalette(2)
        Unknown4007(2)
        Unknown4010(2)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        sendToLabelUpon(34, 3)
    sprite('null', 7)
    label(0)
    sprite('vrkkef400_00', 2)
    sprite('vrkkef400_01', 2)
    EnableAfterimage(1)
    gotoLabel(0)
    label(1)
    sprite('vrkkef400_02', 2)
    EnableAfterimage(0)
    sprite('vrkkef400_03', 2)
    sprite('vrkkef400_04', 3)
    sprite('vrkkef400_05', 3)
    sprite('vrkkef400_06', 3)
    sprite('vrkkef400_07', 2)
    sprite('null', 32767)
    label(2)
    sprite('vrkkef400_08', 2)
    sprite('vrkkef400_09', 2)
    sprite('vrkkef400_10', 6)
    sprite('vrkkef400_11', 2)
    sprite('vrkkef400_12', 2)
    sprite('vrkkef400_13', 2)
    sprite('null', 32767)
    label(3)
    sprite('vrkkef400_14', 2)
    GFX_OffsetX(50000)
    sprite('vrkkef400_15', 2)
    sprite('vrkkef400_16', 2)

@State
def efkk400_Hand00():

    def upon_IMMEDIATE():
        GFX_OffsetY(185000)
        GFX_OffsetX(95000)
        sendToLabelUpon(32, 1)
        Unknown4010(2)
        Unknown4007(22)
    sprite('kk400_13‚š', 1)
    label(0)
    sprite('kk400_13‚š', 2)
    GFX_1('kkef400miniboost_00', 0)
    Unknown1097(3)
    GFX_OffsetY(4294964796)
    GFX_OffsetX(-500)
    Unknown1073(4000)
    sprite('kk400_13‚š', 2)
    GFX_1('kkef400miniboost_00', 1)
    GFX_OffsetY(4294964796)
    sprite('kk400_13‚š', 2)
    GFX_1('kkef400miniboost_00', 2)
    GFX_OffsetY(5000)
    GFX_OffsetX(500)
    Unknown1073(-4000)
    gotoLabel(0)
    label(1)
    sprite('null', 1)

@State
def efkk400_Hand002nd():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown4024(3)
        AttackLevel_(4)
        Damage(600)
        StarterRating(3)
        AttackP2(70)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        GroundUntechableTime(-1)
        AirPushbackX(2000)
        AirPushbackY(12000)
        PushbackX(12000)
        AirUntechableTime(120)
        Unknown12052(1)
        Unknown4008(3)
        FireFX(1)
        sendToLabelUpon(34, 2)

        def upon_45():
            Unknown2071(22, 0, -50000, 100, 1)
    sprite('null', 1)
    GFX_0('efkk400_Handarame', -1)
    sprite('null', 166)
    label(2)
    sprite('null', 25)
    label(8)
    sprite('vrdmy_kk400', 1)
    clearUponHandler(3)
    Unknown1056(4000)
    Unknown1064(2000)
    ScreenShake(20000, 20000)
    GFX_1('kkef400addatk_02', -1)
    SFX_0('016_explode_1')
    SFX_3('kkse_16')

@State
def efkk400_Handarame():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        GFX_OffsetY(45000)
        GFX_Scale(700)
        GFX_2('kkef400arame_04')
    sprite('null', 30)
    SFX_3('kkse_21')
    sprite('null', 30)
    SFX_3('kkse_21')
    sprite('null', 30)
    SFX_3('kkse_21')
    sprite('null', 30)
    SFX_3('kkse_21')
    label(0)
    sprite('null', 15)
    SFX_3('kkse_21')
    loopRest()
    gotoLabel(0)

@State
def efkk400_Hand01():

    def upon_IMMEDIATE():
        GFX_OffsetY(185000)
        GFX_OffsetX(95000)
    sprite('kk400_25z', 7)
    GFX_0('efkk400_Handjet', -1)
    GFX_1('kkef400rokepanimp_01', -1)
    physicsXImpulse(1500)
    sprite('kk400_25z', 7)
    GFX_0('efkk401_hand01smoke', -1)
    physicsXImpulse(3000)
    sprite('kk400_25z', 15)
    physicsXImpulse(75000)

@State
def efkk401_hand01smoke():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 2)
    label(0)
    sprite('null', 2)
    GFX_1('kkef400rokepankidou_02', -1)
    gotoLabel(0)

@State
def efkk400_Handjet():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        GFX_OffsetY(26500)
        GFX_OffsetX(-80000)
        GFX_Scale(1200)
        GFX_Rotation(90000)
        GFX_2('kkef401micilefire_mato')
    label(0)
    sprite('null', 32767)

@State
def efkk400_CircleRenzok():

    def upon_IMMEDIATE():
        pass
    sprite('null', 10)
    GFX_1('kkef400asimotofire_01', -1)
    GFX_0('efkk400_CircleFire01', -1)
    sprite('null', 6)
    GFX_0('efkk400_CircleFire00', -1)

@State
def efkk400_CircleFire00():

    def upon_IMMEDIATE():
        Unknown3033()
        GFX_SetPalette(2)
        Unknown3001(200)
        GFX_OffsetX(100000)
        GFX_OffsetY(4294960296)
        GFX_Scale(1200)
    sprite('vrkkef400_30', 3)
    sprite('vrkkef400_31', 3)
    sprite('vrkkef400_32', 3)
    sprite('vrkkef400_33', 3)
    sprite('vrkkef400_34', 3)
    sprite('vrkkef400_35', 3)
    sprite('vrkkef400_36', 3)

@State
def efkk400_CircleFire01():

    def upon_IMMEDIATE():
        Unknown3033()
        GFX_SetPalette(2)
        GFX_OffsetX(250000)
        GFX_OffsetY(4294960296)
        Unknown3001(200)
        GFX_Scale(1000)
    sprite('vrkkef400_30', 3)
    sprite('vrkkef400_31', 3)
    sprite('vrkkef400_32', 3)
    sprite('vrkkef400_33', 3)
    sprite('vrkkef400_34', 3)
    sprite('vrkkef400_35', 3)
    sprite('vrkkef400_36', 3)

@State
def Warp01():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown4010(3)
    sprite('kk404_00', 2)
    sprite('kk404_01', 3)
    sprite('kk404_02', 3)
    GFX_1('kkef_404', 0)
    sprite('kk404_03', 3)
    GFX_1('kkef_404', 0)
    sprite('kk404_04', 3)
    GFX_1('kkef_404', 0)
    sprite('kk404_05', 3)
    GFX_1('kkef_404', 0)
    sprite('kk404_06', 3)
    GFX_1('kkef_404', 0)
    GFX_1('kkef_404_3', 1)
    sprite('kk404_07', 3)
    sprite('kk404_08', 3)
    sprite('kk404_09', 3)

@State
def efkk_UltraSokidan_Hontai():

    def upon_IMMEDIATE():
        Unknown2011()
        SLOT_53 = 1
        callSubroutine('Fireball_Hontai')
        AttackLevel_(3)
        Damage(360)
        AttackP1(80)
        AttackP2(60)
        hitstun(21)
        Unknown11092(1)
        Hitstop(3)
        AirPushbackY(18000)
        AirPushbackX(3000)
        AirHitstunAnimation(10)
        AirUntechableTime(36)
        FireFX(1)
        Unknown11056(0)
        StarterRating(2)
        MinimumDamagePct(15)
        GFX_Scale(5000)
        GFX_0('efkk_430Start', -1)
        if SLOT_137:
            DamageMultiplier(80)
    label(10)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    StartMultihit()
    GFX_OffsetY(150000)
    physicsYImpulse(40000)
    physicsXImpulse(2000)
    setGravity(1000)
    GFX_0('efkk_UltrafireRotate', -1)
    GFX_0('efkk_UltraFireBallroop', -1)
    GFX_Scale(1600)
    Unknown2037(1)
    loopRest()
    gotoLabel(5)
    label(20)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    StartMultihit()
    GFX_OffsetY(150000)
    physicsYImpulse(60000)
    physicsXImpulse(4000)
    setGravity(1000)
    GFX_0('efkk_UltrafireRotate', -1)
    GFX_0('efkk_UltraFireBallroop', -1)
    GFX_Scale(1600)
    Unknown2037(1)
    loopRest()
    gotoLabel(5)
    label(30)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    StartMultihit()
    GFX_OffsetY(150000)
    physicsYImpulse(80000)
    physicsXImpulse(8000)
    setGravity(1000)
    GFX_0('efkk_UltrafireRotate', -1)
    GFX_0('efkk_UltraFireBallroop', -1)
    GFX_Scale(1600)
    Unknown2037(1)
    loopRest()
    gotoLabel(5)
    label(5)
    sprite('vrkkef402Atk', 3)
    RefreshMultihit()
    GFX_0('efkk_UltrafireDust00', -1)
    if SLOT_95:
        PFX('kkef402jizoku_00_2p', -1)
    else:
        PFX('kkef402jizoku_00', -1)
    PFX_Scale(1500)
    sprite('vrkkef402Atk', 3)
    RefreshMultihit()
    GFX_0('efkk_fireDust01', -1)
    gotoLabel(5)
    label(1)
    sprite('vrkkef402Atk', 2)
    SLOT_55 = 14
    RefreshMultihit()
    AttackLevel_(5)
    Damage(1500)
    Unknown9287()
    Unknown11092(0)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirUntechableTime(120)
    Wallbounce(1)
    AirHitstunAfterWallbounce(60)
    Hitstop(5)
    Unknown11001(10, 10, 10)
    GFX_0('efkk_fireDust00', -1)
    if SLOT_95:
        PFX('kkef402jizoku_00_2p', -1)
    else:
        PFX('kkef402jizoku_00', -1)
    sprite('vrkkef402Atk', 2)
    GFX_0('efkk_fireDust01', -1)
    label(2)
    sprite('vrkkef402Atk', 2)
    GFX_0('efkk_fireDust00', -1)
    if SLOT_95:
        PFX('kkef402jizoku_00_2p', -1)
    else:
        PFX('kkef402jizoku_00', -1)
    sprite('vrkkef402Atk', 2)
    GFX_0('efkk_fireDust01', -1)
    SLOT_55 = (SLOT_55 + (-1))
    Unknown19(99, 2, 55)
    loopRest()
    gotoLabel(2)
    label(99)
    sprite('null', 3)
    Unknown2037(0)
    endMomentum(1)
    Unknown21012('efkk_UltrafireRotate', 32)
    Unknown21012('efkk_UltraFireBallroop', 32)
    GFX_0('efkk_UltraFireBallBrake', -1)
    Unknown1077(0, 360000)
    Unknown1097(200)
    sprite('null', 3)
    if SLOT_95:
        GFX_1('kkef402hit_03_2p', -1)
    else:
        GFX_1('kkef402hit_03', -1)
    GFX_0('efkk_fireDust01', -1)
    GFX_0('efkk_fireDust02', -1)

@State
def efkk_UltraSokidan_Hontai_OD():

    def upon_IMMEDIATE():
        Unknown2011()
        SLOT_54 = 1
        callSubroutine('Fireball_Hontai')
        AttackLevel_(3)
        Damage(360)
        AttackP1(80)
        AttackP2(60)
        hitstun(21)
        Unknown11092(1)
        Hitstop(3)
        AirPushbackY(18000)
        AirPushbackX(3000)
        AirHitstunAnimation(10)
        AirUntechableTime(36)
        FireFX(1)
        Unknown11056(0)
        Unknown9001(4)
        StarterRating(2)
        MinimumDamagePct(15)
        GFX_Scale(5000)
        GFX_0('efkk_430Start', -1)
        if SLOT_137:
            DamageMultiplier(80)
    label(10)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    StartMultihit()
    GFX_OffsetY(150000)
    physicsYImpulse(40000)
    physicsXImpulse(2000)
    setGravity(1000)
    GFX_0('efkk_UltrafireRotate', -1)
    GFX_0('efkk_UltraFireBallroop', -1)
    GFX_Scale(1600)
    Unknown2037(1)
    loopRest()
    gotoLabel(5)
    label(20)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    StartMultihit()
    GFX_OffsetY(150000)
    physicsYImpulse(60000)
    physicsXImpulse(4000)
    setGravity(1000)
    GFX_0('efkk_UltrafireRotate', -1)
    GFX_0('efkk_UltraFireBallroop', -1)
    GFX_Scale(1600)
    Unknown2037(1)
    loopRest()
    gotoLabel(5)
    label(30)
    sprite('null', 11)
    sprite('vrkkef402Atk', 2)
    StartMultihit()
    GFX_OffsetY(150000)
    physicsYImpulse(80000)
    physicsXImpulse(8000)
    setGravity(1000)
    GFX_0('efkk_UltrafireRotate', -1)
    GFX_0('efkk_UltraFireBallroop', -1)
    GFX_Scale(1600)
    Unknown2037(1)
    loopRest()
    gotoLabel(5)
    label(5)
    sprite('vrkkef402Atk', 3)
    RefreshMultihit()
    GFX_0('efkk_UltrafireDust00', -1)
    if SLOT_95:
        PFX('kkef402jizoku_00_2p', -1)
    else:
        PFX('kkef402jizoku_00', -1)
    PFX_Scale(1500)
    sprite('vrkkef402Atk', 3)
    RefreshMultihit()
    GFX_0('efkk_fireDust01', -1)
    gotoLabel(5)
    label(1)
    sprite('vrkkef402Atk', 2)
    SLOT_55 = 14
    RefreshMultihit()
    AttackLevel_(5)
    Damage(2500)
    Unknown9287()
    Unknown11092(0)
    GroundedHitstunAnimation(17)
    AirHitstunAnimation(17)
    AirUntechableTime(120)
    Wallbounce(1)
    AirHitstunAfterWallbounce(60)
    Hitstop(5)
    Unknown11001(10, 10, 10)
    GFX_0('efkk_fireDust00', -1)
    if SLOT_95:
        PFX('kkef402jizoku_00_2p', -1)
    else:
        PFX('kkef402jizoku_00', -1)
    sprite('vrkkef402Atk', 2)
    GFX_0('efkk_fireDust01', -1)
    label(2)
    sprite('vrkkef402Atk', 2)
    GFX_0('efkk_fireDust00', -1)
    if SLOT_95:
        PFX('kkef402jizoku_00_2p', -1)
    else:
        PFX('kkef402jizoku_00', -1)
    sprite('vrkkef402Atk', 2)
    GFX_0('efkk_fireDust01', -1)
    SLOT_55 = (SLOT_55 + (-1))
    Unknown19(99, 2, 55)
    loopRest()
    gotoLabel(2)
    label(99)
    sprite('null', 3)
    Unknown2037(0)
    endMomentum(1)
    Unknown1077(0, 360000)
    Unknown1097(200)
    Unknown21012('efkk_UltrafireRotate', 32)
    Unknown21012('efkk_UltraFireBallroop', 32)
    GFX_0('efkk_UltraFireBallBrake', -1)
    sprite('null', 3)
    if SLOT_95:
        GFX_1('kkef402hit_03_2p', -1)
    else:
        GFX_1('kkef402hit_03', -1)
    GFX_0('efkk_fireDust01', -1)
    GFX_0('efkk_fireDust02', -1)

@State
def efkk_UltrafireDust00():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_Scale(1600)
        Unknown3001(150)
        if SLOT_95:
            Unknown4003('kkef402_fire03_2p', '')
            Unknown4015()
        else:
            Unknown4003('kkef402_fire03', '')
            Unknown4015()
    sprite('null', 10)
    Unknown1099(-30)
    Unknown1074(-5000)
    Unknown1077(0, 360000)

@State
def efkk_430Start():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        GFX_Scale(2000)
        if SLOT_95:
            Unknown4003('kkef402_fire00_2p', '')
            Unknown4015()
        else:
            Unknown4003('kkef402_fire00', '')
            Unknown4015()
    sprite('null', 5)
    PFX_Scale(1500)
    if SLOT_95:
        GFX_1('kkef402star_fire_2p', -1)
    else:
        GFX_1('kkef402star_fire', -1)
    sprite('null', 5)
    GFX_0('efkk_430Start02', -1)
    sprite('null', 10)
    Unknown3001(0)
    GFX_0('efkk_430Start01', -1)

@State
def efkk_430Start01():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        GFX_Scale(2000)
        if SLOT_95:
            Unknown4003('kkef402_fire01_2p', '')
            Unknown4015()
        else:
            Unknown4003('kkef402_fire01', '')
            Unknown4015()
    sprite('null', 10)

@State
def efkk_430Start02():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        GFX_Scale(500)
        if SLOT_95:
            Unknown4003('kkef430_fireballstart00_2p', '')
            Unknown4015()
        else:
            Unknown4003('kkef430_fireballstart00', '')
            Unknown4015()
    sprite('null', 5)
    Unknown1099(200)
    sprite('null', 5)
    Unknown1099(0)

@State
def efkk_UltraFireBallroop():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown23015(3)
        GFX_Scale(1300)
        if SLOT_95:
            GFX_SetPalette(4)
        else:
            GFX_SetPalette(2)
        sendToLabelUpon(32, 1)
    sprite('vrkkef402_00', 1)
    label(0)
    sprite('vrkkef402_00', 3)
    SFX_3('kkse_13')
    sprite('vrkkef402_01', 3)
    sprite('vrkkef402_02', 3)
    sprite('vrkkef402_03', 3)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown3001(0)

@State
def efkk_UltrafireRotate():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        GFX_Scale(1300)
        if SLOT_95:
            Unknown4003('kkef430_fireball00_2p', '')
        else:
            Unknown4003('kkef430_fireball00', '')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    Unknown1074(1000)
    label(0)
    sprite('null', 5)
    Unknown1099(40)
    Unknown3004(-26)

@State
def efkk_UltraFireBallBrake():

    def upon_IMMEDIATE():
        if SLOT_95:
            Unknown4003('kkef402_fire04_2p', '')
            Unknown4015()
        else:
            Unknown4003('kkef402_fire04', '')
            Unknown4015()
    sprite('null', 7)

@State
def efkk401_Kakyufire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('kkef401micilefire_mato')
        GFX_Scale(1000)
        Unknown3001(0)
        sendToLabelUpon(32, 1)
    sprite('null', 15)
    Unknown3004(51)
    label(0)
    sprite('null', 2)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Unknown3004(-51)
    Unknown1099(-50)

@State
def efkk_AtkGravityBall():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('efkk_AtkGravityBallexe', 3, 0, 0)
        Unknown11063(1)
        Unknown11066(1)
        Unknown11084(1)
        Unknown11045(0)
        Unknown11002(-1)
        ThrowRange(200000)
        StarterRating(3)
        Unknown11032(80000, -80000, -1, -1)
        AttackP2(60)
        Unknown2054(1)
        Unknown4011(3)
        GFX_SetPalette(2)
        Unknown23015(1)
        GFX_OffsetY(200000)
        GFX_OffsetX(700000)
        PhysicsPull(999, 8000, 8000)

        def upon_34():
            clearUponHandler(34)
            sendToLabel(3)
            Unknown2003(1)

        def upon_12():
            clearUponHandler(12)
            Unknown2003(1)
            Unknown21007(3, 41)
    sprite('null', 4)
    sprite('vrkkef431_00', 3)
    SFX_3('kkse_26')
    sprite('vrkkef431_01', 3)
    sprite('vrkkef431_02', 3)
    sprite('vrkkef431_03', 3)
    sprite('vrkkef431_04', 3)
    sprite('vrkkef431_05', 3)
    GFX_0('efkk_GravityAura01', -1)
    GFX_0('efkk_HandMato', -1)
    label(1)
    sprite('vrkkef431_06', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    SFX_3('kkse_27')
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    loopRest()
    gotoLabel(1)
    label(3)
    sprite('vrkkef431_09', 3)
    Unknown21012('efkk_HandMato', 33)
    Unknown21012('efkk_GravityAura01', 32)
    PhysicsPull(0, 0, 0)
    sprite('vrkkef431_10', 3)
    sprite('vrkkef431_11', 3)
    sprite('vrkkef431_12', 3)
    label(4)
    sprite('null', 3)

@State
def efkk_AtkGravityBallexe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown2054(1)
        GFX_SetPalette(2)
        Unknown23015(3)
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        YImpluseBeforeWallbounce(1400)
        AirPushbackX(0)
        Hitstop(0)
        AirHitstunAnimation(11)
        AirUntechableTime(120)
        GroundUntechableTime(1)
        StarterRating(3)
        Unknown11050(9, '')
        CameraControlEnable(1)
        Unknown20009(800)
        Unknown23181(240)
        ProjectileHitWall(1)
    sprite('keep', 9)
    Unknown23027()
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    Unknown21012('efkk_GravityAura01', 32)
    Unknown21012('efkk_HandMato', 32)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    SFX_3('kkse_15')
    Unknown36(22)
    Unknown1099(-9)
    Unknown35()
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    Unknown36(22)
    Unknown23119(16777215, 6, 6)
    Unknown35()
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_09', 3)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    Unknown21012('efkk_HandMato', 34)
    Unknown5005(0)
    Unknown20009(1250)
    Unknown21012('UltimateBlackhole', 35)
    sprite('vrkkef431_10', 3)
    Unknown5000(0, 0)
    Unknown5001(0, 4, 4, 0, 0)
    sprite('vrkkef431_11', 3)
    Unknown5000(0, 0)
    Unknown5001(0, 4, 4, 0, 0)
    sprite('vrkkef431_12', 3)
    Unknown5000(0, 0)
    Unknown5001(0, 4, 4, 0, 0)
    sprite('vrkkef431_12', 24)
    Unknown3001(0)
    Unknown5000(0, 0)
    Unknown5001(0, 4, 4, 0, 0)
    Unknown36(22)
    GFX_OffsetY(1000000)
    Unknown35()
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(9)
    sprite('vrkkef431_12', 1)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(9)
    sprite('vrkkef431_12', 1)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(9)
    label(9)
    sprite('vrkkef431_08', 3)
    Unknown5005(1)
    RefreshMultihit()
    Unknown11023(1)
    GFX_0('efkk_AtkGravityBallexe2nd', -1)
    sprite('vrkkef431_08', 5)
    StartMultihit()
    CameraControlEnable(0)

@State
def efkk_AtkGravityBallexe2nd():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(0)
        Damage(1200)
        MinimumDamagePct(100)
        AttackP2(100)
        StarterRating(3)
        AirHitstunAnimation(11)
        GroundUntechableTime(10)
        AirPushbackY(-220000)
        Hitstop(0)
        Unknown11050(9, '')
        Unknown11064(1)
        Unknown2003(1)
        Unknown4009(22)
        Unknown2054(1)
        Unknown23001(0, 0)
        Unknown1006(50000)

        def upon_12():
            Unknown8004(104, 1, 1)
            ScreenShake(0, 10000)

        def upon_3():
            if Unknown23166('CmnActFDownCrash'):
                Unknown2003(0)
                RefreshMultihit()
    sprite('vrkkef431Atk', 33)
    sprite('vrkkef431Atk', 33)
    Unknown4011(22)

@State
def efkk_HandMato():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4011(3)
        Unknown4007(2)
        Unknown3032()
        Unknown23015(1)
        Unknown2005()
        GFX_OffsetX(60000)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        IsInvisibility(1)
    sprite('null', 4)
    sprite('vrkkef431_40', 32767)
    GFX_0('efkk_HandRing', -1)
    label(0)
    sprite('vrkkef431_40', 32767)
    Unknown21012('efkk_HandRing', 32)
    gotoLabel(2)
    label(1)
    sprite('vrkkef431_40', 5)
    Unknown21012('efkk_HandRing', 33)
    label(2)
    sprite('null', 1)

@State
def efkk_HandRing():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4008(2)
        Unknown3032()
        Unknown23015(4)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        IsInvisibility(1)
    sprite('vrkkef431_41', 7)
    sprite('vrkkef431_41', 7)
    Unknown23119(16777215, 15, 1)
    label(0)
    sprite('vrkkef431_41', 2)
    GFX_OffsetY(2000)
    sprite('vrkkef431_41', 2)
    GFX_OffsetY(4294965296)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    GFX_2('kkef_gravityring_02')
    Unknown4003('kkef431_rotatering00', '')
    GFX_OffsetX(-55000)
    Unknown23119(0, 10, 1)
    GFX_Scale(200)
    Unknown1099(25)
    sprite('null', 10)
    ScreenShake(40000, 4000)
    Unknown1099(75)
    sprite('null', 20)
    Unknown1099(0)
    sprite('null', 25)
    Unknown1099(-25)
    sprite('null', 25)
    sprite('null', 5)
    Unknown23119(16777215, 5, 1)
    gotoLabel(3)
    label(2)
    sprite('vrkkef431_41', 5)
    Unknown23119(0, 5, 1)
    label(3)
    sprite('null', 1)

@State
def efkk_GravityAura01():

    def upon_IMMEDIATE():
        Unknown4003('kkef431_backaura00', '')
        Unknown4015()
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        sendToLabelUpon(32, 1)
        GFX_Scale(400)
    label(0)
    sprite('null', 9)
    GFX_1('kkef431aura_minisubpos', -1)
    GFX_0('efkk_GravityYugami', -1)
    Unknown1074(600)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    GFX_0('efkk_GravityYugami', -1)
    sprite('null', 20)
    Unknown3004(-13)

@State
def efkk_GravityYugami():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3057(1)
        Unknown3058(60000)
        GFX_Scale(2400)
    sprite('vrdist00', 20)
    Unknown1099(-65)
    Unknown1108(3000)
    Unknown1077(-90000, 90000)

@State
def efkk_GravityBall():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
        Unknown4010(2)
        GFX_SetPalette(2)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 3)
        GFX_OffsetY(167000)
        GFX_OffsetX(100000)
        Unknown23015(3)
    sprite('null', 10)
    sprite('vrkkef431_00', 4)
    SFX_3('kkse_26')
    sprite('vrkkef431_01', 4)
    sprite('vrkkef431_02', 4)
    sprite('vrkkef431_03', 4)
    sprite('vrkkef431_04', 4)
    sprite('vrkkef431_05', 32767)
    Unknown1099(-1)
    label(1)
    sprite('vrkkef431_06', 3)
    GFX_Scale(1000)
    physicsXImpulse(-6000)
    SFX_3('kkse_27')
    sprite('vrkkef431_07', 3)
    physicsXImpulse(0)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_GravityAura00', -1)
    label(2)
    sprite('vrkkef431_06', 3)
    GFX_1('kkef431aura_00', -1)
    GFX_0('efkk_Gravitythunder00', -1)
    SFX_3('kkse_27')
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    gotoLabel(2)
    label(3)
    sprite('vrkkef431_09', 3)
    Unknown21012('efkk_GravityAura00', 32)
    sprite('vrkkef431_10', 3)
    sprite('vrkkef431_11', 3)
    sprite('vrkkef431_12', 3)

@State
def efkk_Gravitythunder00():

    def upon_IMMEDIATE():
        Unknown4003('kkef431_randthunder00', '')
        Unknown4015()
        Unknown3032()
        GFX_SetPalette(2)
        Unknown21004(191)
    sprite('null', 2)
    Unknown3001(255)
    Unknown1102(-600, 300)
    Unknown1077(0, 360000)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(255)
    sprite('null', 2)
    Unknown3001(0)

@State
def efkk_Gravitythunder01():

    def upon_IMMEDIATE():
        Unknown4003('kkef431_randthunder00', '')
        Unknown4015()
        GFX_SetPalette(2)
        Unknown21004(191)
        Unknown3032()
    sprite('null', 4)
    Unknown3001(0)
    Unknown1077(0, 360000)
    sprite('null', 1)
    Unknown3001(255)
    sprite('null', 1)
    Unknown3001(0)
    sprite('null', 1)
    Unknown3001(255)
    sprite('null', 1)
    Unknown3001(0)
    sprite('null', 1)
    Unknown3001(255)
    sprite('null', 1)
    Unknown3001(0)
    sprite('null', 1)
    Unknown3001(255)

@State
def efkk_Gravitythunder02():

    def upon_IMMEDIATE():
        Unknown4003('kkef431_randthunder00', '')
        Unknown4015()
        Unknown3032()
        GFX_SetPalette(2)
        Unknown21004(191)
    sprite('null', 8)
    Unknown1102(-600, 300)
    Unknown1077(0, 360000)

@State
def efkk_GravityAura00():

    def upon_IMMEDIATE():
        Unknown4003('kkef431_backaura00', '')
        Unknown4015()
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        sendToLabelUpon(32, 0)
        GFX_Scale(800)
        Unknown23015(2)
    sprite('null', 32767)
    Unknown1074(600)
    label(0)
    sprite('null', 20)
    Unknown3004(-13)

@State
def efkk_AtkGravityBall_OD():

    def upon_IMMEDIATE():
        AttackDefaults_Throw('efkk_AtkGravityBallexe_OD', 3, 0, 0)
        Unknown11063(1)
        Unknown11066(1)
        Unknown11084(1)
        Unknown11045(0)
        Unknown11002(-1)
        ThrowRange(200000)
        StarterRating(3)
        Unknown11032(80000, -80000, -1, -1)
        AttackP2(60)
        Unknown2054(1)
        Unknown4011(3)
        GFX_SetPalette(2)
        Unknown23015(1)
        GFX_OffsetY(200000)
        GFX_OffsetX(700000)
        ProjectileHitWall(1)
        PhysicsPull(999, 12000, 12000)

        def upon_34():
            clearUponHandler(34)
            sendToLabel(3)
            Unknown2003(1)

        def upon_12():
            clearUponHandler(12)
            Unknown2003(1)
            Unknown21007(3, 41)
    sprite('null', 4)
    sprite('vrkkef431_00', 3)
    SFX_3('kkse_26')
    sprite('vrkkef431_01', 3)
    sprite('vrkkef431_02', 3)
    sprite('vrkkef431_03', 3)
    sprite('vrkkef431_04', 3)
    sprite('vrkkef431_05', 3)
    GFX_0('efkk_GravityAura01', -1)
    GFX_0('efkk_HandMato', -1)
    label(1)
    sprite('vrkkef431_06', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    SFX_3('kkse_27')
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    loopRest()
    gotoLabel(1)
    label(3)
    sprite('vrkkef431_09', 3)
    Unknown21012('efkk_HandMato', 33)
    Unknown21012('efkk_GravityAura01', 32)
    PhysicsPull(0, 0, 0)
    sprite('vrkkef431_10', 3)
    sprite('vrkkef431_11', 3)
    sprite('vrkkef431_12', 3)
    label(4)
    sprite('null', 3)

@State
def efkk_AtkGravityBallexe_OD():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown2054(1)
        GFX_SetPalette(2)
        Unknown23015(3)
        ProjectileHitWall(1)
        AttackLevel_(0)
        Damage(0)
        StarterRating(3)
        AttackP2(100)
        YImpluseBeforeWallbounce(1400)
        AirPushbackX(0)
        Hitstop(0)
        AirHitstunAnimation(11)
        AirUntechableTime(120)
        GroundUntechableTime(1)
        Unknown11050(9, '')
        CameraControlEnable(1)
        Unknown20009(800)
        Unknown23181(240)
    sprite('keep', 9)
    Unknown23027()
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    Unknown21012('efkk_GravityAura01', 32)
    Unknown21012('efkk_HandMato', 32)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    SFX_3('kkse_15')
    Unknown36(22)
    Unknown1099(-9)
    Unknown35()
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_06', 3)
    GFX_0('efkk_Gravitythunder02', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_07', 3)
    GFX_0('efkk_Gravitythunder00', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    Unknown36(22)
    Unknown23119(16777215, 6, 6)
    Unknown35()
    sprite('vrkkef431_08', 3)
    GFX_0('efkk_Gravitythunder01', -1)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    sprite('vrkkef431_09', 3)
    Unknown5000(0, 0)
    Unknown5001(1, 1, 1, 0, 0)
    Unknown21012('efkk_HandMato', 34)
    Unknown5005(0)
    Unknown20009(1250)
    Unknown21012('UltimateBlackhole_OD', 35)
    sprite('vrkkef431_10', 3)
    Unknown5000(0, 0)
    Unknown5001(0, 4, 4, 0, 0)
    sprite('vrkkef431_11', 3)
    Unknown5000(0, 0)
    Unknown5001(0, 4, 4, 0, 0)
    sprite('vrkkef431_12', 3)
    Unknown5000(0, 0)
    Unknown5001(0, 4, 4, 0, 0)
    sprite('vrkkef431_12', 24)
    Unknown3001(0)
    Unknown5000(0, 0)
    Unknown5001(0, 4, 4, 0, 0)
    Unknown36(22)
    GFX_OffsetY(1000000)
    Unknown35()
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(9)
    sprite('vrkkef431_12', 1)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(9)
    sprite('vrkkef431_12', 1)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(9)
    label(9)
    sprite('vrkkef431_08', 3)
    Unknown5005(1)
    RefreshMultihit()
    Unknown11023(1)
    GFX_0('efkk_AtkGravityBallexe2nd_OD', -1)
    sprite('vrkkef431_08', 5)
    StartMultihit()
    CameraControlEnable(0)

@State
def efkk_AtkGravityBallexe2nd_OD():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(0)
        Damage(1800)
        MinimumDamagePct(100)
        AirHitstunAnimation(11)
        GroundUntechableTime(30)
        AirPushbackY(-240000)
        AttackP2(100)
        StarterRating(3)
        Hitstop(0)
        Unknown11050(9, '')
        Unknown11064(1)
        StarterRating(3)
        Unknown9001(4)
        Unknown2003(1)
        ProjectileHitWall(1)
        Unknown4009(22)
        Unknown2054(1)
        Unknown23001(0, 0)
        Unknown1006(50000)

        def upon_12():
            Unknown8003(104, 1, 1)
            Unknown8004(104, 1, 1)
            ScreenShake(0, 10000)

        def upon_3():
            if Unknown23166('CmnActFDownCrash'):
                Unknown2003(0)
                RefreshMultihit()
    sprite('vrkkef431Atk', 33)
    sprite('vrkkef431Atk', 33)
    Unknown4011(22)

@State
def vrkkef432_Land():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(3)
        Unknown2019(100)
        GFX_OffsetX(110000)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(44, 1)
    sprite('null', 10)
    sprite('vrkkef432_Land00', 3)
    sprite('vrkkef432_Land01', 3)
    sprite('vrkkef432_Land02', 3)
    sprite('vrkkef432_Land03', 3)
    sprite('vrkkef432_Land04', 3)
    sprite('vrkkef432_Land05', 32767)
    label(0)
    sprite('vrkkef432_Land06', 32767)
    label(1)
    sprite('vrkkef432_Land06', 3)
    Unknown4007(0)
    clearUponHandler(44)
    sprite('vrkkef432_Land07', 3)
    sprite('vrkkef432_Land08', 3)
    sprite('vrkkef432_Land09', 3)
    sprite('vrkkef432_Land10', 3)
    sprite('vrkkef432_Land00', 30)

@State
def vrkkef432_Air():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(3)
        Unknown2019(100)
        GFX_OffsetX(110000)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(44, 1)
        loopRelated(17, 550)
        sendToLabelUpon(17, 1)
    sprite('vrkkef432_Air00', 15)
    Unknown23123(16777215, 12)
    GFX_OffsetY(4294877296)
    physicsYImpulse(6000)
    GFX_0('efkk432_burner1', 0)
    GFX_0('efkk432_burner2', 1)
    GFX_0('efkk432_burner3', 2)
    sprite('vrkkef432_Air00a', 10)
    physicsYImpulse(0)
    sprite('vrkkef432_Air01', 3)
    sprite('vrkkef432_Air02', 3)
    sprite('vrkkef432_Air03', 3)
    sprite('vrkkef432_Air04', 3)
    sprite('vrkkef432_Air05', 32767)
    label(0)
    sprite('vrkkef432_Air06', 32767)
    label(1)
    sprite('vrkkef432_Air06', 3)
    Unknown4007(0)
    clearUponHandler(44)
    clearUponHandler(17)
    sprite('vrkkef432_Air07', 3)
    sprite('vrkkef432_Air08', 3)
    sprite('vrkkef432_Air09', 3)
    sprite('vrkkef432_Air10', 3)
    sprite('vrkkef432_Air00', 10)
    sprite('vrkkef432_Air00', 20)
    Unknown21012('efkk432_burner1', 32)
    Unknown21012('efkk432_burner2', 32)
    Unknown21012('efkk432_burner3', 32)
    Unknown3004(-10)

@State
def efkk432_burner1():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
        GFX_2('kkef432micilefire_mato')
        GFX_Scale(700)
        GFX_Rotation(0)
        Unknown3001(0)
        sendToLabelUpon(32, 1)
    sprite('null', 16)
    Unknown3004(16)
    sprite('null', 32767)
    label(1)
    sprite('null', 10)
    Unknown3004(-25)
    Unknown1099(-21)

@State
def efkk432_burner2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
        GFX_2('kkef432micilefire_mato')
        GFX_Scale(625)
        GFX_Rotation(-11250)
        Unknown3001(0)
        sendToLabelUpon(32, 1)
    sprite('null', 16)
    Unknown3004(16)
    sprite('null', 32767)
    label(1)
    sprite('null', 10)
    Unknown3004(-25)
    Unknown1099(-20)

@State
def efkk432_burner3():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
        GFX_2('kkef432micilefire_mato')
        GFX_Scale(625)
        GFX_Rotation(11250)
        Unknown3001(0)
        sendToLabelUpon(32, 1)
    sprite('null', 16)
    Unknown3004(16)
    sprite('null', 32767)
    label(1)
    sprite('null', 10)
    Unknown3004(-25)
    Unknown1099(-20)

@State
def efkk_BigTager():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(3)
        GFX_SetPalette(6)
        Unknown2019(500)
        GFX_OffsetX(0)
        GFX_OffsetY(25000)
        GFX_Scale(1000)

        def upon_41():
            Collidable(1)
            Unknown2016(400)
            Unknown2015(200)
            Unknown2021(1)

        def upon_STATE_END():
            Collidable(0)
            Unknown2016(-1)
            Unknown2015(-1)
            Unknown2021(0)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        sendToLabelUpon(44, 2)
        loopRelated(17, 550)
        sendToLabelUpon(17, 2)
    sprite('null', 4)
    ScreenShake(1000, 4000)
    SFX_0('019_quake_1')
    GFX_0('efkk_TagerHole', -1)
    sprite('null', 4)
    ScreenShake(1000, 4000)
    sprite('kk432tgcutin_20', 4)
    ScreenShake(1000, 4000)
    SFX_0('019_quake_1')
    SFX_3('kkse_16')
    SFX_3('kkse_16')
    sprite('kk432tgcutin_21', 4)
    ScreenShake(2000, 8000)
    sprite('kk432tgcutin_22', 4)
    ScreenShake(2000, 8000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_23', 4)
    ScreenShake(2000, 8000)
    sprite('kk432tgcutin_24', 4)
    ScreenShake(2000, 8000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_25', 4)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_26', 4)
    ScreenShake(2000, 8000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_00', 12)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_01', 4)
    ScreenShake(2000, 8000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_02', 4)
    label(0)
    sprite('kk432tgcutin_03', 32767)
    GFX_0('efkk_BeamCharge', -1)
    label(1)
    sprite('kk432tgcutin_03', 1)
    Unknown21012('efkk_BeamCharge', 32)
    sprite('kk432tgcutin_03', 32767)
    GFX_0('efkk_Beam00', -1)
    label(99)
    sprite('null', 4)
    sprite('kk432tgcutin_20', 4)
    ScreenShake(1000, 4000)
    SFX_0('019_quake_1')
    SFX_3('kkse_16')
    SFX_3('kkse_16')
    sprite('kk432tgcutin_21', 4)
    ScreenShake(2000, 6000)
    sprite('kk432tgcutin_22', 4)
    ScreenShake(2000, 6000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_23', 4)
    ScreenShake(2000, 6000)
    sprite('kk432tgcutin_24', 4)
    ScreenShake(2000, 6000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_25', 4)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_26', 4)
    ScreenShake(2000, 6000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_00', 10)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_01', 4)
    ScreenShake(2000, 6000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_02', 4)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('kk432tgcutin_02', 4)
    Unknown4007(0)
    Collidable(0)
    clearUponHandler(44)
    clearUponHandler(17)
    sprite('kk432tgcutin_01', 4)
    sprite('kk432tgcutin_00', 4)
    sprite('kk432tgcutin_26', 4)
    Unknown21012('efkk_TagerHole', 32)
    ScreenShake(5500, 5500)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_25', 4)
    sprite('kk432tgcutin_24', 4)
    ScreenShake(5500, 5500)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_23', 4)
    sprite('kk432tgcutin_22', 4)
    ScreenShake(5500, 5500)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_21', 4)
    sprite('kk432tgcutin_20', 4)
    ScreenShake(5500, 5500)
    sprite('null', 15)

@State
def efkk_TagerHole():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        GFX_SetPalette(2)
        Unknown3035()
        Unknown2019(500)
        GFX_2('kkef430_02')
        GFX_Scale(1300)
        GFX_OffsetX(-300000)
        sendToLabelUpon(32, 0)
    sprite('vrkkef432_bloom', 40)
    sprite('vrkkef432_bloom', 10)
    Unknown1059(-60)
    physicsXImpulse(24000)
    sprite('vrkkef432_bloom', 32767)
    Unknown1059(0)
    physicsXImpulse(0)
    label(0)
    sprite('vrkkef432_bloom', 3)
    Unknown1059(60)
    physicsXImpulse(-40000)
    sprite('vrkkef432_bloom', 5)
    Unknown1059(0)
    sprite('vrkkef432_bloom', 15)
    physicsXImpulse(0)
    sprite('vrkkef432_bloom', 4)
    GFX_1('kkef430_end', -1)
    Unknown3004(-32)
    Unknown1099(-50)

@State
def efkk_Beam00():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(2)
        Unknown4007(3)
        Unknown3032()
        Unknown4003('kkef432_beam00', '')
        Unknown4015()
        GFX_Scale(2000)
        GFX_OffsetY(300000)
        GFX_OffsetX(150000)
        sendToLabelUpon(32, 1)
    sprite('null', 1)
    ScreenShake(150000, 150000)
    label(0)
    sprite('null', 1)
    GFX_1('kkef432_beamcircle01', -1)
    Unknown1064(2000)
    GFX_0('efkk_Beamthunder00', -1)
    SFX_3('kkse_18')
    sprite('null', 1)
    Unknown1064(1900)
    GFX_0('efkk_Beamthunder01', -1)
    sprite('null', 1)
    Unknown1064(1950)
    GFX_0('efkk_Beamthunder02', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    GFX_1('kkef432_beamend_flash', -1)
    Unknown3001(230)

@State
def efkk_Beamthunder00():

    def upon_IMMEDIATE():
        Unknown4003('kkef432_thunder00', '')
        Unknown4015()
        Unknown2054(1)
        Unknown3032()
    sprite('null', 2)
    Unknown3001(255)
    Unknown1102(0, 600)
    Unknown1077(0, 360000)

@State
def efkk_Beamthunder01():

    def upon_IMMEDIATE():
        Unknown4003('kkef432_thunder00', '')
        Unknown4015()
        Unknown2054(1)
        Unknown2005()
        Unknown3032()
    sprite('null', 4)
    Unknown3001(255)
    Unknown1102(0, 600)
    Unknown1077(0, 360000)

@State
def efkk_Beamthunder02():

    def upon_IMMEDIATE():
        Unknown4003('kkef432_thunder00', '')
        Unknown4015()
        Unknown2054(1)
        Unknown3032()
    sprite('null', 2)
    Unknown1102(0, 600)
    Unknown1077(0, 360000)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(255)

@State
def efkk_Beamthunder03():

    def upon_IMMEDIATE():
        Unknown4003('kkef431_randthunder00', '')
        Unknown4015()
        Unknown2054(1)
        Unknown3032()
    sprite('null', 2)
    Unknown3001(255)
    Unknown1102(-600, 300)
    Unknown1077(0, 360000)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(255)
    sprite('null', 2)
    Unknown3001(0)

@State
def efkk_BeamCharge():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(2)
        Unknown4011(3)
        Unknown3032()
        GFX_OffsetY(300000)
        GFX_OffsetX(150000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 3)
    GFX_0('efkk_Beamthunder02', -1)
    SFX_3('kkse_17')
    Unknown36(1)
    Unknown3001(150)
    Unknown35()
    GFX_0('efkk_BeamCharge00', -1)
    GFX_1('kkef432charge_sub', -1)
    sprite('null', 3)
    GFX_0('efkk_Beamthunder03', -1)
    Unknown36(1)
    Unknown3001(150)
    Unknown35()
    sprite('null', 4)
    GFX_0('efkk_Beamthunder03', -1)
    Unknown36(1)
    Unknown3001(150)
    Unknown35()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown3004(-26)

@State
def efkk_BeamCharge00():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('kkef432_charge00', '')
        Unknown4015()
        Unknown2054(1)
        Unknown3032()
        GFX_Scale(800)
        Unknown3001(0)
    sprite('null', 10)
    Unknown1099(-40)
    Unknown3004(26)
    Unknown1074(6000)
    Unknown1077(0, 360000)
    sprite('null', 10)
    sprite('null', 10)
    Unknown3004(-26)

@State
def efkk_BigTagerAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        AttackLevel_(5)
        Damage(300)
        MinimumDamagePct(5)
        AttackP2(97)
        ChipPercentage(10)
        AirUntechableTime(120)
        GroundUntechableTime(1)
        Hitstop(0)
        AirPushbackX(100000)
        AirPushbackY(0)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirHitstunAfterWallbounce(50)
        WallbounceReboundTime(0)
        Wallstick(1)
        WallstickLength(50)
        Unknown11072(1, 1000000, 120000)
        Unknown11057(300)
        Unknown11084(1)

        def upon_12():
            clearUponHandler(12)
            Unknown2037(1)
            Unknown21007(3, 32)

        def upon_11():
            SLOT_51 = (SLOT_51 + 1)

        def upon_3():
            if (SLOT_51 <= 20):
                Damage(300)
            else:
                if (SLOT_51 > 20):
                    Damage(260)
                if (SLOT_51 > 40):
                    Damage(220)
                if (SLOT_51 > 60):
                    Damage(180)
                    MinimumDamagePct(20)
                if (SLOT_51 > 80):
                    Damage(140)
                    MinimumDamagePct(20)
                if (SLOT_51 > 100):
                    Damage(100)
                    MinimumDamagePct(20)
            if SLOT_2:
                Unknown11072(3, 5000, 0)

        def upon_33():
            pass
        sendToLabelUpon(32, 0)
    label(1)
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()
    Unknown11050(0, 'ef_exhit_sub')
    Unknown11051(0, 'ef_girds')
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()
    Unknown11051(8, '')
    Unknown11050(8, '')
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()
    Unknown11051(8, '')
    Unknown11050(8, '')
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()
    Unknown11050(0, 'ef_exhit_sub')
    Unknown11051(0, 'ef_girds')
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()

@State
def efkk_ODBigTager():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(3)
        GFX_SetPalette(6)
        Unknown2019(500)
        GFX_OffsetX(0)
        GFX_OffsetY(25000)
        GFX_Scale(1000)

        def upon_41():
            Collidable(1)
            Unknown2016(400)
            Unknown2015(200)
            Unknown2021(1)

        def upon_STATE_END():
            Collidable(0)
            Unknown2016(-1)
            Unknown2015(-1)
            Unknown2021(0)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        sendToLabelUpon(44, 2)
        loopRelated(17, 550)
        sendToLabelUpon(17, 2)
    sprite('null', 4)
    ScreenShake(1000, 4000)
    SFX_0('019_quake_1')
    GFX_0('efkk_TagerHole', -1)
    sprite('null', 4)
    ScreenShake(1000, 4000)
    sprite('kk432tgcutin_30', 4)
    ScreenShake(1000, 4000)
    SFX_0('019_quake_1')
    SFX_3('kkse_16')
    SFX_3('kkse_16')
    sprite('kk432tgcutin_31', 4)
    ScreenShake(2000, 8000)
    sprite('kk432tgcutin_32', 4)
    ScreenShake(2000, 8000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_33', 4)
    ScreenShake(2000, 8000)
    sprite('kk432tgcutin_34', 4)
    ScreenShake(2000, 8000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_35', 4)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_36', 4)
    ScreenShake(2000, 8000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_04', 12)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_05', 4)
    ScreenShake(2000, 8000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_06', 4)
    label(0)
    sprite('kk432tgcutin_07', 32767)
    GFX_0('efkk_ODBeamCharge', -1)
    label(1)
    sprite('kk432tgcutin_07', 1)
    Unknown21012('efkk_ODBeamCharge', 32)
    sprite('kk432tgcutin_07', 32767)
    GFX_0('efkk_ODBeam00', -1)
    label(99)
    sprite('null', 4)
    sprite('kk432tgcutin_30', 4)
    ScreenShake(1000, 4000)
    SFX_0('019_quake_1')
    SFX_3('kkse_16')
    SFX_3('kkse_16')
    sprite('kk432tgcutin_31', 4)
    ScreenShake(2000, 6000)
    sprite('kk432tgcutin_22', 4)
    ScreenShake(2000, 6000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_33', 4)
    ScreenShake(2000, 6000)
    sprite('kk432tgcutin_34', 4)
    ScreenShake(2000, 6000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_35', 4)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_36', 4)
    ScreenShake(2000, 6000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_04', 10)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_05', 4)
    ScreenShake(2000, 6000)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_06', 4)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('kk432tgcutin_06', 4)
    Unknown4007(0)
    Collidable(0)
    clearUponHandler(44)
    clearUponHandler(17)
    sprite('kk432tgcutin_05', 4)
    sprite('kk432tgcutin_04', 4)
    sprite('kk432tgcutin_36', 4)
    Unknown21012('efkk_TagerHole', 32)
    ScreenShake(5500, 5500)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_35', 4)
    sprite('kk432tgcutin_34', 4)
    ScreenShake(5500, 5500)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_33', 4)
    sprite('kk432tgcutin_32', 4)
    ScreenShake(5500, 5500)
    SFX_0('019_quake_1')
    sprite('kk432tgcutin_31', 4)
    sprite('kk432tgcutin_30', 4)
    ScreenShake(5500, 5500)

@State
def efkk_ODBeam00():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(2)
        Unknown4007(3)
        Unknown3032()
        Unknown4003('kkef432_beam01', '')
        Unknown4015()
        GFX_Scale(2000)
        GFX_OffsetY(300000)
        GFX_OffsetX(150000)
        sendToLabelUpon(32, 1)
    sprite('null', 1)
    ScreenShake(150000, 150000)
    label(0)
    sprite('null', 1)
    GFX_1('kkef432_beamcircle01', -1)
    Unknown1064(2000)
    GFX_0('efkk_ODBeamthunder00', -1)
    SFX_3('kkse_18')
    sprite('null', 1)
    Unknown1064(1900)
    GFX_0('efkk_ODBeamthunder01', -1)
    sprite('null', 1)
    Unknown1064(1950)
    GFX_0('efkk_ODBeamthunder02', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    GFX_1('kkef432_odbeamend_flash', -1)
    Unknown3001(230)

@State
def efkk_ODBeamthunder00():

    def upon_IMMEDIATE():
        Unknown4003('kkef432_thunder01', '')
        Unknown4015()
        Unknown2054(1)
        Unknown3032()
    sprite('null', 2)
    Unknown3001(255)
    Unknown1102(0, 600)
    Unknown1077(0, 360000)

@State
def efkk_ODBeamthunder01():

    def upon_IMMEDIATE():
        Unknown4003('kkef432_thunder01', '')
        Unknown4015()
        Unknown2054(1)
        Unknown2005()
        Unknown3032()
    sprite('null', 4)
    Unknown3001(255)
    Unknown1102(0, 600)
    Unknown1077(0, 360000)

@State
def efkk_ODBeamthunder02():

    def upon_IMMEDIATE():
        Unknown4003('kkef432_thunder01', '')
        Unknown4015()
        Unknown2054(1)
        Unknown3032()
    sprite('null', 2)
    Unknown1102(0, 600)
    Unknown1077(0, 360000)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(255)

@State
def efkk_ODBeamthunder03():

    def upon_IMMEDIATE():
        Unknown4003('kkef432_thunder01', '')
        Unknown4015()
        Unknown2054(1)
        Unknown3032()
    sprite('null', 2)
    Unknown3001(255)
    Unknown1102(-600, 300)
    Unknown1077(0, 360000)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(255)
    sprite('null', 2)
    Unknown3001(0)

@State
def efkk_ODBeamCharge():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(2)
        Unknown4011(3)
        Unknown3032()
        GFX_OffsetY(300000)
        GFX_OffsetX(150000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 3)
    GFX_0('efkk_ODBeamthunder02', -1)
    SFX_3('kkse_17')
    Unknown36(1)
    Unknown3001(150)
    Unknown35()
    GFX_0('efkk_ODBeamCharge00', -1)
    GFX_1('kkef432odcharge_sub', -1)
    sprite('null', 3)
    GFX_0('efkk_ODBeamthunder03', -1)
    Unknown36(1)
    Unknown3001(150)
    Unknown35()
    sprite('null', 4)
    GFX_0('efkk_ODBeamthunder03', -1)
    Unknown36(1)
    Unknown3001(150)
    Unknown35()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown3004(-26)

@State
def efkk_ODBeamCharge00():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('kkef432_charge01', '')
        Unknown4015()
        Unknown2054(1)
        Unknown3032()
        GFX_Scale(800)
        Unknown3001(0)
    sprite('null', 10)
    Unknown1099(-40)
    Unknown3004(26)
    Unknown1074(6000)
    Unknown1077(0, 360000)
    sprite('null', 10)
    sprite('null', 10)
    Unknown3004(-26)

@State
def efkk_BigTagerAtk_OD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        AttackLevel_(5)
        Damage(200)
        MinimumDamagePct(5)
        AttackP2(97)
        ChipPercentage(10)
        AirUntechableTime(120)
        GroundUntechableTime(1)
        Hitstop(0)
        AirPushbackX(100000)
        AirPushbackY(0)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirHitstunAfterWallbounce(50)
        WallbounceReboundTime(0)
        Wallstick(1)
        WallstickLength(50)
        Unknown11072(1, 1000000, 120000)
        Unknown9001(4)
        Unknown11057(300)
        Unknown11084(1)

        def upon_12():
            clearUponHandler(12)
            Unknown2037(1)

        def upon_11():
            SLOT_51 = (SLOT_51 + 1)

        def upon_3():
            if (SLOT_51 <= 20):
                Damage(300)
            else:
                if (SLOT_51 > 20):
                    Damage(260)
                if (SLOT_51 > 40):
                    Damage(220)
                if (SLOT_51 > 60):
                    Damage(180)
                    MinimumDamagePct(20)
            if SLOT_2:
                Unknown11072(3, 10000, 0)

        def upon_33():
            pass
        sendToLabelUpon(32, 0)
    label(1)
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    Unknown11050(0, '')
    Unknown11051(0, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    Unknown11051(8, '')
    Unknown11050(8, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    Unknown11051(8, '')
    Unknown11050(8, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    Unknown11051(8, '')
    Unknown11050(8, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    Unknown11051(8, '')
    Unknown11050(8, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    Unknown11051(8, '')
    Unknown11050(8, '')
    gotoLabel(1)
    label(0)
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    Unknown11050(0, '')
    Unknown11051(0, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    Unknown11051(8, '')
    Unknown11050(8, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    Unknown11050(0, '')
    Unknown11051(0, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    Unknown11051(8, '')
    Unknown11050(8, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    Unknown11050(0, '')
    Unknown11051(0, '')
    sprite('vrkkef432Atk', 1)
    RefreshMultihit()
    sprite('vrkkef432Atk', 2)
    RefreshMultihit()

@State
def __450Cam():

    def upon_IMMEDIATE():
        Unknown4008(2)
        Unknown3032()
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 0)
        Unknown20003(1)
        CameraControlEnable(1)
        Unknown20002(1)
    sprite('null', 32767)
    Unknown1086(22)
    Unknown20009(1300)
    label(0)
    sprite('null', 60)
    Unknown20001(1)
    Unknown1086(3)
    GFX_OffsetX(200000)
    Unknown20009(1000)
    GFX_0('450Shake', -1)
    sprite('null', 10)
    Unknown20001(0)
    Unknown20009(950)
    SFX_0('019_quake_1')
    SFX_0('019_quake_1')
    SFX_0('019_quake_0')
    sprite('null', 10)
    Unknown20009(925)
    SFX_0('019_quake_1')
    sprite('null', 10)
    Unknown20009(900)
    sprite('null', 10)
    Unknown20009(875)
    SFX_0('019_quake_1')
    sprite('null', 10)
    Unknown20009(850)
    SFX_0('019_quake_1')
    sprite('null', 10)
    Unknown20009(825)
    SFX_0('019_quake_1')
    sprite('null', 10)
    Unknown20009(800)
    SFX_0('019_quake_1')
    sprite('null', 10)
    Unknown20009(775)
    SFX_0('019_quake_1')
    sprite('null', 10)
    Unknown20009(750)
    SFX_0('019_quake_1')
    sprite('null', 10)
    Unknown20009(725)
    SFX_0('019_quake_1')
    sprite('null', 10)
    Unknown20009(700)
    sprite('null', 10)
    Unknown20009(675)
    SFX_0('019_quake_1')
    sprite('null', 10)
    Unknown20009(650)
    sprite('null', 10)
    Unknown20009(625)
    SFX_0('019_quake_1')
    sprite('null', 10)
    Unknown20009(600)
    sprite('null', 10)
    Unknown20009(575)
    SFX_0('019_quake_1')
    sprite('null', 10)
    Unknown20009(550)
    sprite('null', 10)
    Unknown20009(525)
    SFX_0('019_quake_1')
    sprite('null', 10)
    Unknown20009(500)
    sprite('null', 10)
    Unknown20009(475)
    SFX_0('019_quake_1')
    sprite('null', 10)
    Unknown20009(450)
    sprite('null', 10)
    Unknown20009(425)
    SFX_0('019_quake_1')
    sprite('null', 10)
    Unknown20009(400)
    sprite('null', 15)
    Unknown20009(375)
    SFX_0('019_quake_1')
    sprite('null', 15)
    Unknown20009(350)
    sprite('null', 15)
    Unknown20009(325)
    SFX_0('019_quake_1')
    sprite('null', 15)
    Unknown20009(300)
    sprite('null', 15)
    Unknown20009(275)
    SFX_0('019_quake_1')
    sprite('null', 15)
    Unknown20009(250)
    sprite('null', 15)
    Unknown20009(225)
    SFX_0('019_quake_1')
    sprite('null', 15)
    Unknown20009(200)
    sprite('null', 15)
    Unknown20009(175)
    SFX_0('019_quake_1')
    sprite('null', 15)
    Unknown20009(150)
    sprite('null', 15)
    Unknown20009(125)
    SFX_0('019_quake_1')
    sprite('null', 32767)
    label(1)
    sprite('null', 3)
    Unknown20009(150)
    SFX_3('kkse_29')
    SFX_3('kkse_29')
    sprite('null', 3)
    Unknown20009(175)
    sprite('null', 3)
    Unknown20009(200)
    sprite('null', 3)
    Unknown20009(225)
    sprite('null', 3)
    Unknown20009(250)
    sprite('null', 3)
    Unknown20009(275)
    sprite('null', 3)
    Unknown20009(300)
    sprite('null', 3)
    Unknown20009(325)
    sprite('null', 3)
    Unknown20009(350)
    sprite('null', 3)
    Unknown20009(375)
    sprite('null', 3)
    Unknown20009(400)
    sprite('null', 3)
    Unknown20009(425)
    sprite('null', 3)
    Unknown20009(450)
    sprite('null', 3)
    Unknown20009(475)
    sprite('null', 3)
    Unknown20009(500)
    sprite('null', 3)
    Unknown20009(525)
    sprite('null', 3)
    Unknown20009(550)
    sprite('null', 3)
    Unknown20009(575)
    sprite('null', 3)
    Unknown20009(600)
    sprite('null', 3)
    Unknown20009(625)
    sprite('null', 3)
    Unknown20009(650)
    sprite('null', 3)
    Unknown20009(675)
    sprite('null', 3)
    Unknown20009(700)
    sprite('null', 3)
    Unknown20009(725)
    sprite('null', 3)
    Unknown20009(750)
    sprite('null', 3)
    Unknown20009(775)
    sprite('null', 3)
    Unknown20009(1000)
    sprite('null', 3)
    Unknown20009(1025)
    sprite('null', 3)
    Unknown20009(1050)
    sprite('null', 3)
    Unknown20009(1075)
    sprite('null', 32767)
    Unknown20009(1100)

@State
def __450Shake():

    def upon_IMMEDIATE():
        Unknown4010(2)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 10)
    ScreenShake(4000, 4000)
    sprite('null', 5)
    gotoLabel(0)
    label(1)
    sprite('null', 5)

@State
def __450Shake2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 10)
    ScreenShake(20000, 20000)
    sprite('null', 5)
    gotoLabel(0)
    label(1)
    sprite('null', 5)

@State
def efkk_WinBG():

    def upon_IMMEDIATE():
        Unknown4010(3)
        GFX_2('kkef450winbg_01')
        GFX_Scale(900)
        GFX_OffsetY(30000)
    sprite('null', 32767)
    GFX_0('efkk_WinBG2', -1)

@State
def efkk_WinBG2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(3)
        Unknown23015(2)
        Unknown4003('kkef450_finishbg', '')
    sprite('null', 32767)

@State
def efkk_Whiteout():

    def upon_IMMEDIATE():
        GFX_2('kkef450scenechange_03')
    sprite('null', 110)
    sprite('null', 10)
    Unknown3004(-26)

@State
def efkk_AHJishaku00():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('kkef450_jishaku00', '')
        Unknown2054(1)
        Unknown3032()
        Unknown2005()
        GFX_Scale(1000)
        Unknown1086(22)
        Unknown1006(0)
        GFX_2('kkef450ray2_00')
    sprite('null', 120)

@State
def efkk_InsekiEff():

    def upon_IMMEDIATE():
        GFX_OffsetY(380000)
        GFX_OffsetX(200000)
    sprite('null', 60)
    ScreenShake(20000, 20000)
    PFX_Rotation(500)
    PFX('kkef450insekimagi_00', -1)

@State
def efkk202_BLT():

    def upon_IMMEDIATE():
        GFX_SetPalette(2)

        def upon_LANDING():
            setGravity(1600)
            physicsYImpulse(10000)
            physicsXImpulse(-10000)
            SFX_3('kkse_31')
        Unknown23015(1)
    sprite('vr_blt202', 40)
    Unknown1074(10000)
    Unknown1077(0, 360000)
    SFX_3('nose_02')
    setGravity(1600)
    physicsYImpulse(10000)
    physicsXImpulse(-10000)
    Unknown1025(-1000, 1000)
    Unknown1026(-1000, 5000)

@State
def efkk402_BLT():

    def upon_IMMEDIATE():

        def upon_LANDING():
            setGravity(1600)
            physicsYImpulse(10000)
            physicsXImpulse(-10000)
            SFX_3('kkse_31')
        Unknown23015(1)
    sprite('vr_blt402', 40)
    Unknown1074(10000)
    Unknown1077(0, 360000)
    SFX_3('nose_02')
    setGravity(1600)
    physicsYImpulse(8000)
    physicsXImpulse(-10000)
    Unknown1025(-1000, 1000)
    Unknown1026(-1000, 5000)

@State
def efkk_610_hole_out():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4011(3)
        Unknown4024(3)
        Unknown4009(3)
        GFX_SetPalette(3)
        GFX_OffsetX(-115000)
        GFX_OffsetY(4294953296)
        GFX_Rotation(-90000)
    sprite('vrkkef601_hole', 10)
    GFX_Scale(0)
    Unknown1059(50)
    Unknown1067(80)
    sprite('vrkkef601_hole', 23)
    Unknown1056(500)
    Unknown1064(800)
    Unknown1099(0)
    sprite('vrkkef601_hole', 11)
    Unknown4007(0)
    Unknown4009(0)
    sprite('vrkkef601_hole', 6)
    Unknown1099(-100)

@State
def efkk_TagerHole_event():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(2)
        Unknown2019(500)
        GFX_2('kkef430_02')
        GFX_Scale(700)
    sprite('vrkkef432_bloom', 40)
    sprite('vrkkef432_bloom', 10)
    Unknown1059(-80)
    sprite('vrkkef432_bloom', 32767)
    Unknown1059(0)
    GFX_Scale(0)
    IsInvisibility(1)

@State
def BurstDD_AtkMatome():

    def upon_IMMEDIATE():
        pass
    sprite('null', 10)
    label(0)
    sprite('null', 10)
    GFX_0('BurstDD_Atk', -1)
    loopRest()
    gotoLabel(0)

@State
def BurstDD_Atk():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Damage(200)
        AttackP2(100)
        SameMoveProration(-1)
        AirUntechableTime(100)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(30000)
        AirPushbackY(12000)
        WallbounceReboundTime(50)
        Hitstop(4)
        GroundUntechableTime(1)
        FireFX(1)
        Unknown11064(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamagePct(10)
        IsInvisibility(1)
        Unknown23151(22, 105)
    sprite('vr_blt', 6)
    RefreshMultihit()

@State
def BurstDD_missile():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Damage(60)
        AttackP2(100)
        SameMoveProration(-1)
        AirUntechableTime(100)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(40000)
        AirPushbackY(3000)
        WallbounceReboundTime(50)
        Hitstop(1)
        GroundUntechableTime(1)
        FireFX(1)
        Unknown11064(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamagePct(10)
        Unknown9218(1)
        Unknown9219(1)
        Unknown11050(4, '')
        Unknown11069('BurstDD_missile')
        Unknown11062(1)

        def upon_32():
            Unknown11069('BurstDD_missile2')
        Unknown53(1)

        def upon_3():
            Unknown2072('160000000000000050c300003075000001000000')
        GFX_Scale(700)
        sendToLabelUpon(11, 1)
        EnableAfterimage(1)
        Unknown23015(1)
    sprite('vrkkef_missile', 2)
    GFX_2('kkef440_jet')
    physicsXImpulse(15000)
    physicsYImpulse(7500)
    GFX_1('kkef440_jetkidou', 0)
    sprite('vrkkef_missile', 2)
    GFX_1('kkef440_jetkidou', 0)
    sprite('vrkkef_missile', 2)
    physicsXImpulse(30000)
    physicsYImpulse(3750)
    Unknown1074(2250)
    GFX_1('kkef440_jetkidou', 0)
    sprite('vrkkef_missile', 2)
    GFX_1('kkef440_jetkidou', 0)
    label(0)
    sprite('vrkkef_missile', 1)
    physicsXImpulse(45000)
    physicsYImpulse(-7500)
    Unknown1074(0)
    GFX_1('kkef440_jetkidou', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_0('BurstDD_Bomb', -1)

@State
def BurstDD_missile2():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Damage(60)
        AttackP2(100)
        AirUntechableTime(200)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackX(-15000)
        AirPushbackY(40000)
        Hitstop(1)
        EnableGroundBounce(2)
        GroundbounceHeight(60)
        GroundUntechableTime(1)
        FireFX(1)
        Unknown11064(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamagePct(10)
        Unknown11050(4, '')
        Unknown11069('BurstDDAdd')
        Unknown11062(1)
        Unknown53(1)

        def upon_3():
            Unknown2072('160000000000000050c300003075000001000000')
        GFX_Scale(1000)
        Unknown23015(1)
        sendToLabelUpon(11, 1)
    sprite('vrkkef_missile', 2)
    GFX_2('kkef440_jet')
    physicsXImpulse(15000)
    physicsYImpulse(3750)
    GFX_1('kkef440_jetkidou', 0)
    sprite('vrkkef_missile', 2)
    GFX_1('kkef440_jetkidou', 0)
    sprite('vrkkef_missile', 2)
    physicsXImpulse(30000)
    physicsYImpulse(1875)
    Unknown1074(1125)
    GFX_1('kkef440_jetkidou', 0)
    sprite('vrkkef_missile', 2)
    GFX_1('kkef440_jetkidou', 0)
    label(0)
    sprite('vrkkef_missile', 2)
    physicsXImpulse(45000)
    physicsYImpulse(-3750)
    Unknown1074(0)
    GFX_1('kkef440_jetkidou', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_0('BurstDD_Bomb', -1)

@State
def BurstDD_Bomb():

    def upon_IMMEDIATE():
        GFX_SetPalette(2)
        Unknown3033()
        Unknown1010(0, 300000)
    sprite('vrkkef440_00', 2)
    SFX_0('016_explode_1')
    sprite('vrkkef440_01', 2)
    sprite('vrkkef440_02', 2)
    sprite('vrkkef440_03', 2)
    Unknown1097(-300)
    Unknown1077(0, 360000)
    EnableAfterimage(1)
    AfterimageCount(3)
    sprite('vrkkef440_03', 2)
    Unknown1097(100)
    sprite('vrkkef440_03', 2)
    Unknown1097(100)
    sprite('vrkkef440_03', 2)
    Unknown1097(100)
    sprite('vrkkef440_04', 4)
    Unknown1099(75)
    sprite('vrkkef440_05', 2)
    Unknown3004(-51)
    sprite('vrkkef440_06', 2)

@State
def BurstDD_thunderball():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        GFX_OffsetX(250000)
        Unknown3001(255)
        Unknown4003('kkef440_thunderball00', '')
        GFX_2('kkef440_thunderLoop')
        sendToLabelUpon(32, 1)
        GFX_0('BurstDD_Camera', -1)
    label(0)
    sprite('null', 2)
    Unknown1097(80)
    GFX_0('efkk440_thunder00', -1)
    ScreenShake(2500, 2500)
    SFX_0('014_electric_sl')
    sprite('null', 2)
    Unknown1097(-80)
    GFX_0('efkk440_thunder01', -1)
    ScreenShake(2500, 2500)
    SFX_0('014_electric_m')
    gotoLabel(0)
    label(1)
    sprite('null', 2)
    Unknown3004(-51)
    Unknown1099(100)
    GFX_0('BurstDD_thunderballSub', -1)
    ScreenShake(20000, 20000)
    sprite('null', 2)
    ScreenShake(20000, 20000)
    sprite('null', 2)
    ScreenShake(20000, 20000)
    GFX_0('efkk440_thunderEnd', -1)

@State
def efkk440_thunder00():

    def upon_IMMEDIATE():
        Unknown4003('kkef432_thunder00', '')
        Unknown4015()
        Unknown2054(1)
        Unknown2005()
        Unknown3032()
        GFX_OffsetY(170000)
        GFX_Scale(800)
        Unknown21010(1)
    sprite('null', 2)
    Unknown3001(255)
    Unknown1077(0, 360000)

@State
def efkk440_thunder01():

    def upon_IMMEDIATE():
        Unknown4003('kkef432_thunder00', '')
        Unknown4015()
        Unknown2054(1)
        Unknown3032()
        GFX_OffsetY(170000)
        GFX_Scale(800)
        Unknown21010(1)
    sprite('null', 2)
    Unknown1077(0, 360000)
    sprite('null', 2)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(255)

@State
def efkk440_thunderEnd():

    def upon_IMMEDIATE():
        GFX_OffsetY(170000)
    sprite('null', 30)
    PFX_Scale(1700)
    GFX_2('kkef440_thunderEnde')
    Unknown1099(50)
    sprite('null', 10)
    Unknown1099(12)
    sprite('null', 10)
    Unknown1099(6)
    sprite('null', 10)
    Unknown1099(3)

@State
def BurstDD_thunderballSub():

    def upon_IMMEDIATE():
        GFX_OffsetY(170000)
        GFX_Scale(400)
        Unknown3032()
        Unknown4003('kkef440_thunderball01', '')
    sprite('null', 6)
    Unknown1099(30)
    sprite('null', 5)
    Unknown3004(-26)
    Unknown1099(60)

@State
def BurstDDEx_SmokeHead():

    def upon_IMMEDIATE():
        GFX_2('kkef440_bombhead_00')
        Unknown4013(2)
        Unknown1064(979)
        Unknown1056(1050)
        GFX_OffsetY(450000)
        Unknown21010(1)
    sprite('null', 10)
    physicsYImpulse(40000)
    Unknown1099(3)
    sprite('null', 5)
    physicsYImpulse(8750)
    sprite('null', 20)
    physicsYImpulse(0)
    sprite('null', 40)
    Unknown21010(0)

@State
def BurstDDEx_SmokeBody():

    def upon_IMMEDIATE():
        GFX_Scale(1500)
        GFX_OffsetX(200000)
        Unknown21010(1)
    sprite('null', 5)
    GFX_1('kkef440_flash', -1)
    sprite('null', 30)
    GFX_2('kkef440_bombbody_00')
    GFX_0('BurstDDEx_SmokeHead', -1)
    sprite('null', 40)
    Unknown21010(0)

@State
def BurstDD_Camera():

    def upon_IMMEDIATE():
        Unknown4010(3)
        CameraControlEnable(1)
        Unknown20003(1)
        sendToLabelUpon(32, 0)
        Unknown21010(1)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    Unknown1006(0)
    Unknown20009(1300)
    physicsYImpulse(45000)
    sprite('null', 35)
    physicsYImpulse(0)
    Unknown21010(0)
    sprite('null', 15)
    physicsYImpulse(-64000)
    Unknown20009(1000)
    sprite('null', 60)
    physicsYImpulse(0)

@State
def efkk440_PartsA():

    def upon_IMMEDIATE():
        setGravity(3000)
        sendToLabelUpon(2, 1)
        Unknown23022(1)
    label(0)
    sprite('kk440_16_w1', 4)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_1('kkef403koware_05', -1)

@State
def efkk440_PartsB():

    def upon_IMMEDIATE():
        setGravity(3000)
        sendToLabelUpon(2, 1)
        Unknown23022(1)
    label(0)
    sprite('kk440_16_w2', 4)
    gotoLabel(0)
    label(1)
    sprite('null', 2)
    GFX_1('kkef403koware_05', -1)

@State
def efkk440_PartsC():

    def upon_IMMEDIATE():
        setGravity(3000)
        sendToLabelUpon(2, 1)
        Unknown23022(1)
    label(0)
    sprite('kk440_16_w3', 4)
    gotoLabel(0)
    label(1)
    sprite('null', 2)
    Unknown4054(12)
    PFX('kkef403koware_05', -1)

@State
def efkk440_PartsD():

    def upon_IMMEDIATE():
        setGravity(3000)
        sendToLabelUpon(2, 1)
        Unknown23022(1)
    label(0)
    sprite('kk440_16_w4', 4)
    gotoLabel(0)
    label(1)
    sprite('null', 2)
    Unknown4054(12)
    PFX('kkef403koware_05', -1)

@State
def efkk440_MissileFire():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('kkef_440_missileEnter')
        Unknown4010(2)
        Unknown4007(2)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    Unknown3004(-51)

@State
def efkk440_Koge():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_SetPalette(2)
        Unknown3001(180)
        Unknown4007(2)
        Unknown4010(2)
    sprite('vrkkef440_koge', 30)
    sprite('vrkkef440_koge', 15)
    GFX_1('kkef_440_kogesmoke', 0)
    GFX_1('kkef_440_kogesmoke', 1)
    GFX_1('kkef_440_kogesmoke', 2)
    GFX_1('kkef_440_kogesmoke', 3)
    GFX_1('kkef_440_kogesmoke', 4)
    sprite('vrkkef440_koge', 5)
    Unknown3004(-36)

@State
def efkk440_Parts2A():

    def upon_IMMEDIATE():
        setGravity(1000)
        sendToLabelUpon(2, 1)
        Unknown23022(1)
    label(0)
    sprite('kk440_23w1', 4)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_1('kkef403koware_05', -1)
    SFX_0('016_explode_0')

@State
def efkk440_Parts2B():

    def upon_IMMEDIATE():
        setGravity(1000)
        sendToLabelUpon(2, 1)
        Unknown23022(1)
    label(0)
    sprite('kk440_23w2', 4)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_1('kkef403koware_05', -1)

@State
def efkk440_Parts2C():

    def upon_IMMEDIATE():
        setGravity(1000)
        sendToLabelUpon(2, 1)
        Unknown23022(1)
        Unknown1074(-2500)
    sprite('kk440_23w3', 4)
    physicsXImpulse(-12000)
    physicsYImpulse(12000)
    label(0)
    sprite('kk440_23w3', 4)
    physicsXImpulse(-4000)
    physicsYImpulse(-15000)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_1('kkef403koware_05', -1)
    SFX_0('016_explode_0')

@State
def efkk440_Parts2D():

    def upon_IMMEDIATE():
        setGravity(1000)
        sendToLabelUpon(2, 1)
        Unknown23022(1)
        Unknown1074(-1000)
    label(0)
    sprite('kk440_23w4', 4)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_1('kkef403koware_05', -1)

@State
def efkk440_ThunderTame():

    def upon_IMMEDIATE():
        GFX_Scale(750)
        Unknown4010(2)
        Unknown4007(2)
        GFX_2('kkef_440_thunder_tame')
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    GFX_OffsetX(2500)
    GFX_OffsetY(4294964796)
    sprite('null', 2)
    GFX_OffsetX(-2500)
    GFX_OffsetY(2500)
    gotoLabel(0)
    label(1)
    sprite('null', 32767)
    GFX_OffsetY(65000)

@State
def efkk405_Fire00():

    def upon_IMMEDIATE():
        Unknown3033()
        GFX_SetPalette(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        sendToLabelUpon(32, 0)
        Unknown4003('kkef405_fire00', '')
    sprite('vrkkef405_00', 3)
    GFX_1('kkef405_fire', 0)
    GFX_1('kkef405_fire', 1)
    sprite('vrkkef405_01', 3)
    GFX_1('kkef405_fire', 0)
    GFX_1('kkef405_fire', 1)
    sprite('vrkkef405_02', 3)
    GFX_1('kkef405_fire', 0)
    GFX_1('kkef405_fire', 1)
    sprite('vrkkef405_03', 3)
    GFX_1('kkef405_fire', 0)
    GFX_1('kkef405_fire', 1)
    sprite('vrkkef405_04', 3)
    GFX_1('kkef405_fire', 0)
    GFX_1('kkef405_fire', 1)
    label(0)
    sprite('null', 10)
    Unknown4009(0)
    Unknown3004(-30)
    Unknown1099(20)
    physicsYImpulse(-10000)

@State
def efkk405_PartsA():

    def upon_IMMEDIATE():
        setGravity(1000)
        sendToLabelUpon(2, 1)
        Unknown23022(1)
    label(0)
    sprite('kk405_11a', 4)
    GFX_1('kkef405_smoke', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_1('kkef403koware_05', -1)

@State
def efkk405_PartsB():

    def upon_IMMEDIATE():
        setGravity(1000)
        sendToLabelUpon(2, 1)
        Unknown23022(1)
    label(0)
    sprite('kk405_11b', 4)
    GFX_1('kkef405_smoke', 0)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_1('kkef403koware_05', -1)
    SFX_0('016_explode_0')

@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    SFX_0('019_quake_0')
    loopRest()
    gotoLabel(0)

@State
def Act3Event_kkvsph_no():

    def upon_IMMEDIATE():
        Unknown30012(0)
        sendToLabelUpon(32, 0)
        GFX_OffsetX(-160000)
        Unknown2019(500)
    sprite('no064_04', 3)
    sprite('no064_04', 32767)
    loopRest()
    label(0)
    sprite('no064_05', 4)
    sprite('no064_06', 4)
    sprite('no064_07', 4)
    sprite('no064_08', 4)
    sprite('no032_00', 1)
    Unknown2005()
    Unknown2034(0)
    Collidable(0)
    physicsXImpulse(18000)
    sprite('no032_01', 2)
    sprite('no032_02', 4)
    sprite('no032_03', 4)
    sprite('no032_04', 4)
    Unknown8006(100, 1, 1)
    sprite('no032_05', 4)
    sprite('no032_06', 4)
    sprite('no032_07', 4)
    sprite('no032_08', 4)
    Unknown8006(100, 1, 1)
    sprite('no032_09', 4)
    loopRest()

@State
def Act3Event_kgvskk_mu():

    def upon_IMMEDIATE():
        Unknown30012(1)
        sendToLabelUpon(32, 1)
        Unknown1086(22)
        Unknown2005()
        GFX_OffsetX(-100000)
        Unknown2019(500)
    label(0)
    sprite('mu000_00', 6)
    sprite('mu000_01', 6)
    sprite('mu000_02', 6)
    sprite('mu000_03', 6)
    sprite('mu000_04', 6)
    sprite('mu000_05', 6)
    sprite('mu000_06', 6)
    sprite('mu000_07', 6)
    sprite('mu000_08', 6)
    sprite('mu000_09', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mu003_00', 3)
    Unknown2005()
    sprite('mu003_01', 3)
    sprite('mu003_02', 3)
    sprite('mu032_00', 2)
    Unknown2034(0)
    Collidable(0)
    physicsXImpulse(24000)
    SFX_0('000_airdash_0')
    GFX_1('muef_ny030', -1)
    sprite('mu032_01', 4)
    sprite('mu032_02', 4)
    sprite('mu032_03', 4)
    GFX_1('muef_ny032', 106)
    sprite('mu032_04', 4)
    GFX_1('muef_ny032', 106)
    sprite('mu032_01', 4)
    sprite('mu032_02', 4)
    sprite('mu032_03', 4)
    GFX_1('muef_ny032', 106)
    sprite('mu032_04', 4)
    SFX_3('muse_10')
    GFX_1('muef_ny032', 106)

@State
def Noise():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ef_eventnoise.DIG', '')
        Unknown4015()
        Unknown23032(50)
        Unknown23033(50)
    sprite('null', 30)
    SFX_0('014_electric_ml')
    loopRest()

@State
def Eventoffset_Sosai_arvskk():

    def upon_IMMEDIATE():
        Unknown1001(0)
        Unknown1006(150000)
        Unknown1010(-20000, 20000)
    sprite('null', 4)
    GFX_1('ef_offset', 0)
    SFX_0('108_attack_offset')
    ScreenShake(30000, 30000)