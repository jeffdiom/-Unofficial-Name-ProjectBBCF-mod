@State
def EMB():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(300000)
        GFX_Scale(1100)
        Unknown2054(1)
        IsInvisibility(1)
        Unknown4003('ef_emb_JB.DIG', '')
        Unknown23015(5)
    sprite('null', 10)
    Unknown3026(4278190080)
    Unknown3025(4278190335, 10)
    sprite('null', 10)
    Unknown3025(4286625023, 10)
    sprite('null', 10)
    Unknown3025(4294967295, 10)
    sprite('null', 10)
    Unknown3025(4286625023, 10)
    sprite('null', 80)

@State
def EMB_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(240000)
        GFX_Scale(1250)
        Unknown2054(1)
        IsInvisibility(1)
        Unknown4003('ef_emb_JB.DIG', '')
        Unknown23015(5)
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
def EMB_JB_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(240000)
        GFX_Scale(1250)
        Unknown2054(1)
        Unknown4003('ef_emb_JB.DIG', '')
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
def jb611_Tail():

    def upon_IMMEDIATE():
        Unknown4010(3)
    sprite('jb611_00s', 8)
    sprite('jb611_01s', 8)
    sprite('jb611_02s', 8)
    label(0)
    sprite('jb611_03s', 10)
    sprite('jb611_04s', 10)
    sprite('jb611_05s', 10)
    sprite('jb611_06s', 10)
    loopRest()
    gotoLabel(0)

@Subroutine
def zanzou():
    Unknown3053(1)
    Unknown3040(2)
    Unknown3042(240)
    Unknown3043(241)
    Unknown3041(242)
    Unknown3044(0)

@Subroutine
def zanzou2():
    Unknown3053(1)
    Unknown3040(2)
    Unknown3042(240)
    Unknown3043(241)
    Unknown3041(242)
    Unknown3044(1)

@State
def jbef202_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
        GFX_OffsetX(-88000)
    sprite('vrefjb202_00', 3)
    sprite('vrefjb202_01', 4)

@State
def jbef202_zanzou_2nd():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        GFX_OffsetX(-88000)
        callSubroutine('zanzou')
    sprite('vrefjb202_10', 3)
    sprite('vrefjb202_11', 4)

@State
def jbef232_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb232_00', 6)
    sprite('vrefjb232_01', 4)

@State
def jbef212_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb212_00', 10)
    GFX_OffsetX(64000)

@State
def jbef235_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        GFX_OffsetX(-38000)
        callSubroutine('zanzou')
    sprite('vrefjb235_00', 3)
    sprite('vrefjb235_01', 3)
    Unknown4007(0)

@State
def jbef235_zanzou_2nd():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        GFX_OffsetX(-199000)
        Unknown3053(1)
        callSubroutine('zanzou')
    sprite('vrefjb235_10', 2)
    GFX_OffsetX(192000)
    sprite('vrefjb235_10', 8)
    Unknown4007(0)

@State
def jbef252_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb252_00', 2)
    sprite('vrefjb252_01', 4)
    sprite('vrefjb252_01', 4)
    Unknown4007(0)

@State
def jbef252_zanzou_2nd():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb252_10', 2)
    sprite('vrefjb252_10', 4)
    sprite('vrefjb252_10', 4)
    Unknown4007(0)

@State
def jbef255_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb255_00', 2)
    sprite('vrefjb255_01', 3)
    sprite('vrefjb255_01', 4)
    Unknown4007(0)

@State
def jbef340_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb340_00', 3)
    GFX_OffsetX(128000)
    sprite('vrefjb340_01', 7)

@State
def jbef210_atemi():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        Unknown2019(100)
    sprite('vrefjb210_00', 3)
    GFX_0('jbef_210_bloom', 0)
    Unknown3007(0)
    Unknown3001(0)
    Unknown3004(85)
    sprite('keep', 1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('keep', 15)
    Unknown3004(-16)

@State
def jbef211_atemi():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        Unknown2019(100)
    sprite('vrefjb211_00', 3)
    GFX_0('jbef_210_bloom', 0)
    Unknown3007(0)
    Unknown3001(0)
    Unknown3004(85)
    sprite('keep', 1)
    Unknown3001(255)
    Unknown3004(0)
    sprite('keep', 15)
    Unknown3004(-16)

@State
def jbef_210_bloom():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        GFX_2('jbef_210bloom')
    sprite('null', 30)

@State
def jbef311_claw():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_SetPalette(1)
        Unknown3033()
        GFX_OffsetX(90000)
        Unknown2019(100)
    sprite('vrefjb311_00', 10)
    sprite('vrefjb311_01', 10)
    Unknown3004(-25)

@State
def jbef_DashSmoke():

    def upon_IMMEDIATE():
        pass
    sprite('null', 15)
    GFX_1('jbef_403smoke', 100)

@State
def jbef_claw_pt():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_2('jbef_claw')
    sprite('null', 3)
    sprite('null', 60)
    Unknown4007(0)

@State
def jbef400_slash():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        GFX_OffsetX(-40000)
    sprite('vrefjb400_00', 2)
    GFX_0('jbef_claw_pt', 0)
    sprite('vrefjb400_00', 4)
    Unknown4007(0)
    sprite('vrefjb400_01', 12)
    Unknown3004(-21)

@State
def jbef400_slash2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        Unknown1073(3000)
    sprite('vrefjb400_10', 2)
    GFX_1('jbef_claw_pt', 0)
    sprite('vrefjb400_10', 4)
    Unknown4007(0)
    sprite('vrefjb400_11', 12)
    Unknown3004(-21)

@State
def jbef401_slash():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        GFX_OffsetY(96000)
        GFX_OffsetX(-32000)
        Unknown1064(1050)
        Unknown1056(1200)
    sprite('vrefjb401_00', 2)
    sprite('vrefjb401_00', 4)
    Unknown4007(0)
    sprite('vrefjb401_01', 12)
    Unknown3004(-21)

@State
def jbef402_slash():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_SetPalette(1)
        Unknown3033()
        GFX_OffsetX(100000)
        GFX_OffsetY(4294957296)
        GFX_0('jbef402_slash2', 100)
    sprite('vrefjb402_00', 2)
    sprite('vrefjb402_00', 4)
    Unknown4007(0)
    sprite('vrefjb402_01', 12)
    Unknown3004(-21)

@State
def jbef402_slash2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_SetPalette(1)
        Unknown3033()
    sprite('vrefjb402_10', 2)
    sprite('vrefjb402_10', 4)
    Unknown4007(0)
    sprite('vrefjb402_11', 12)
    Unknown3004(-21)

@State
def jbef403_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou2')
    sprite('vrefjb403_00', 3)
    sprite('vrefjb403_01', 10)

@State
def jbef403_zanzou2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou2')
    sprite('vrefjb403_10', 3)
    sprite('vrefjb403_11', 10)

@State
def jbef404_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb404_00', 4)
    sprite('vrefjb404_01', 10)
    Unknown4007(0)

@State
def jbef404_zanzou_air():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb404_00ex', 3)
    sprite('vrefjb404_01ex', 10)
    Unknown4007(0)

@State
def jbef405_loop():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 32767)
    GFX_0('jbef405_loop_swords', 100)
    GFX_0('jbef405_loop_claws', 100)

@State
def jbef405_loop_swords():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
    label(0)
    sprite('null', 3)
    GFX_0('jbef405_loop_sword', 100)
    SFX_0('010_swing_sword_0')
    sprite('null', 3)
    GFX_0('jbef405_loop_sword2', 100)
    SFX_0('010_swing_sword_0')
    sprite('null', 3)
    GFX_0('jbef405_loop_sword3', 100)
    SFX_0('010_swing_sword_0')
    sprite('null', 3)
    GFX_0('jbef405_loop_sword4', 100)
    SFX_0('010_swing_sword_0')
    gotoLabel(0)

@State
def jbef405_loop_claws():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        GFX_OffsetY(9000)
    label(0)
    sprite('null', 4)
    GFX_0('jbef405_loop_claw', 100)
    SFX_3('jbse_02')
    sprite('null', 4)
    GFX_0('jbef405_loop_claw2', 100)
    sprite('null', 4)
    GFX_0('jbef405_loop_claw3', 100)
    SFX_3('jbse_02')
    sprite('null', 4)
    GFX_0('jbef405_loop_claw4', 100)
    gotoLabel(0)

@State
def jbef405_loop_sword():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
        GFX_OffsetX(40000)
    sprite('vrefjb405_00', 3)
    sprite('vrefjb405_01', 3)

@State
def jbef405_loop_sword2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb405_10', 3)
    sprite('vrefjb405_11', 3)

@State
def jbef405_loop_sword3():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb405_20', 3)
    sprite('vrefjb405_21', 3)

@State
def jbef405_loop_sword4():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb405_30', 3)
    sprite('vrefjb405_31', 3)

@State
def jbef405_loop_claw():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        GFX_Rotation(-15000)
        Unknown1056(1050)
        Unknown1064(1250)
        GFX_OffsetX(-80000)
        GFX_OffsetY(200000)
    sprite('vrefjb405_40', 2)
    sprite('vrefjb405_41', 2)
    sprite('vrefjb405_42', 2)

@State
def jbef405_loop_claw2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        Unknown2019(100)
        GFX_Rotation(45000)
        Unknown1056(800)
        Unknown1064(1200)
        GFX_OffsetX(48000)
        GFX_OffsetY(224000)
    sprite('vrefjb405_40', 2)
    sprite('vrefjb405_41', 2)
    sprite('vrefjb405_42', 2)

@State
def jbef405_loop_claw3():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        GFX_Rotation(120000)
        Unknown1056(800)
        Unknown1064(1200)
        GFX_OffsetX(-48000)
        GFX_OffsetY(80000)
    sprite('vrefjb405_40', 2)
    sprite('vrefjb405_41', 2)
    sprite('vrefjb405_42', 2)

@State
def jbef405_loop_claw4():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        GFX_Rotation(65000)
        Unknown1056(700)
        Unknown1064(1050)
        GFX_OffsetX(192000)
        GFX_OffsetY(64000)
    sprite('vrefjb405_40', 2)
    sprite('vrefjb405_41', 2)
    sprite('vrefjb405_42', 2)

@State
def jbef405_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb405_80', 3)
    sprite('vrefjb405_81', 10)

@State
def jbef406_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb406_00', 6)

@State
def jbef406_zanzou2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb406_10', 6)

@State
def jbef600_manto():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_SetPalette(0)
        Unknown3032()
        Unknown13044(1)
        Unknown2019(100)
    sprite('efjb600_00', 3)
    GFX_OffsetX(80000)
    GFX_OffsetY(4294839296)
    physicsXImpulse(-30000)
    physicsYImpulse(8000)
    sprite('efjb600_00', 60)

@State
def __5DStartEff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4007(2)
        Unknown23013(1)
        Unknown3032()
        Unknown4003('jbef_markerMove', '')
        GFX_OffsetX(100000)
        GFX_OffsetY(150000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    Unknown1059(40)
    GFX_0('MAKERMoveEffSumi', 100)
    label(0)
    sprite('null', 6)
    ProjectileDisapperOnHit(0)
    Unknown4007(0)
    Unknown3004(-42)

@State
def AIR5DStartEff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4007(2)
        Unknown23013(1)
        Unknown3032()
        Unknown4003('jbef_markerMove', '')
        GFX_OffsetX(100000)
        GFX_Rotation(60000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    Unknown1059(40)
    GFX_0('MAKERMoveEffSumi', 100)
    label(0)
    sprite('null', 6)
    ProjectileDisapperOnHit(0)
    Unknown4007(0)
    Unknown3004(-42)

@State
def AIR6DStartEff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4007(2)
        Unknown23013(1)
        Unknown3032()
        Unknown4003('jbef_markerMove', '')
        GFX_OffsetX(100000)
        GFX_OffsetY(100000)
        GFX_Rotation(30000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    Unknown1059(40)
    GFX_0('MAKERMoveEffSumi', 100)
    label(0)
    sprite('null', 6)
    ProjectileDisapperOnHit(0)
    Unknown4007(0)
    Unknown3004(-42)

@State
def Drive_AddAtk():

    def upon_IMMEDIATE():
        ProjectileDisapperOnHit(3)
        Unknown2009()
        AttackLevel_(4)
        Damage(880)
        AirPushbackX(30000)
        AirPushbackY(-60000)
        PushbackX(19800)
        SildeDuration(20)
        Unknown11056(0)
        StarterRating(2)
        SlashFX(1)
        Unknown11057(700)
        Unknown11050(4, 'jbef_driveslash_sumi')

        def upon_ON_HIT_OR_BLOCK():
            SLOT_32 = 300
            Unknown21012('NmlAtk5D', 32)
            Unknown21012('NmlAtkAIR5D', 32)
            Unknown21012('AN_NmlAtkAIR6D', 32)
    sprite('null', 25)
    sprite('Drive_Atk', 3)
    Unknown23151(22, 103)
    RefreshMultihit()

@State
def jbef_DriveHit():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('jbef_DriveSlash00.DIG', '')
        GFX_2('jbef_driveslash_speed')
        GFX_Rotation(10000)
        Unknown1086(22)
        GFX_OffsetY(180000)
        Unknown1065(200)
        Unknown23015(11)
        Unknown21010(1)
        Unknown2054(1)
    sprite('null', 20)
    GFX_1('jbef_driveslash_sumi', -1)
    sprite('null', 58)
    Unknown1099(10)
    Unknown4003('jbef_DriveSlashEnd', '')

@State
def jbef_Air5DHit():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('jbef_DriveSlash00.DIG', '')
        GFX_2('jbef_driveslash_speed')
        Unknown23015(11)
        GFX_Rotation(60000)
        Unknown1086(22)
        GFX_OffsetX(-50000)
        GFX_OffsetY(120000)
        Unknown1065(200)
        Unknown21010(1)
        Unknown2054(1)
    sprite('null', 20)
    PFX_Rotation(80000)
    PFX('jbef_driveslash_sumi', -1)
    sprite('null', 58)
    Unknown1099(10)
    Unknown4003('jbef_DriveSlashEnd', '')

@State
def jbef_Air6DHit():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('jbef_DriveSlash00.DIG', '')
        GFX_2('jbef_driveslash_speed')
        Unknown23015(11)
        GFX_Rotation(30000)
        Unknown1086(22)
        GFX_OffsetX(-50000)
        GFX_OffsetY(170000)
        Unknown1065(200)
        Unknown21010(1)
        Unknown2054(1)
    sprite('null', 20)
    PFX_Rotation(80000)
    PFX('jbef_driveslash_sumi', -1)
    sprite('null', 58)
    Unknown1099(10)
    Unknown4003('jbef_DriveSlashEnd', '')

@Subroutine
def DriveAtk_AtkVector():
    if (SLOT_12 >= 90000):
        AirPushbackX(60000)
    elif (SLOT_12 > 0):
        AirPushbackX(30000)
    elif (SLOT_12 == 0):
        AirPushbackX(0)
    elif (SLOT_12 < 0):
        AirPushbackX(-30000)
    elif (SLOT_12 <= (-90000)):
        AirPushbackX(-60000)
    if (SLOT_13 >= 90000):
        AirPushbackY(60000)
    elif (SLOT_13 > 0):
        AirPushbackY(30000)
    elif (SLOT_13 == 0):
        AirPushbackY(0)
    elif (SLOT_13 < 0):
        AirPushbackY(-30000)
    elif (SLOT_13 <= (-90000)):
        AirPushbackY(-60000)

@Subroutine
def DriveAtk():
    AttackLevel_(4)
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    AttackAttributes(1, 0, 0, 0, 0)
    Damage(550)
    AttackP1(80)
    GroundedHitstunAnimation(9)
    PushbackX(80000)
    AirUntechableTime(40)
    SildeDuration(10)
    Hitstop(0)
    Unknown11001(0, 2, 2)
    Unknown11056(0)
    SlashFX(1)
    Unknown11072(1, 0, -110000)
    Unknown11032(200000, -200000, 400000, -400000)
    StarterRating(2)
    callSubroutine('DriveAtk_AtkVector')

    def upon_12():
        SLOT_32 = 300

@Subroutine
def DriveAtkFinish():
    AttackLevel_(4)
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    AttackAttributes(1, 0, 0, 0, 0)
    Damage(550)
    AttackP1(80)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirUntechableTime(60)
    AirPushbackY(30000)
    AirPushbackX(30000)
    Unknown9215()
    Unknown9203()
    Hitstop(0)
    Unknown11001(0, 0, 5)
    Unknown11032(200000, -200000, 400000, -400000)
    Unknown11056(0)
    SlashFX(1)
    StarterRating(2)

@Subroutine
def LeverInput():
    if CheckInput(0x45):
        SLOT_57 = 2
    if CheckInput(0x93):
        SLOT_57 = 8
    SLOT_55 = 1

@Subroutine
def CheckPosY():
    if (SLOT_57 == 2):
        GFX_OffsetY(4294767296)
    elif (SLOT_57 == 8):
        GFX_OffsetY(200000)
    if (SLOT_23 <= 150000):
        Unknown1006(150000)
    elif (SLOT_23 >= 3000000):
        Unknown1006(3000000)

@Subroutine
def CourseSetting():
    ProjectileHitWall(1)
    Unknown48(23, 2, 58, 3, 2, 58)
    if SLOT_51:
        clearUponHandler(32)
        if (SLOT_55 == 1):
            GFX_OffsetX(200000)
            GFX_OffsetY(400000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(5, 1)
        if (SLOT_55 == 2):
            GFX_OffsetX(400000)
            GFX_OffsetY(4294567296)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(6, 1)
        if (SLOT_55 == 3):
            GFX_OffsetX(400000)
            GFX_OffsetY(400000)
            if (SLOT_57 == 2):
                GFX_OffsetY(200000)
            elif (SLOT_57 == 8):
                GFX_OffsetY(4294767296)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(7, 1)
        if (SLOT_55 == 4):
            GFX_OffsetX(400000)
            GFX_OffsetY(4294567296)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(8, 1)
    if SLOT_52:
        clearUponHandler(32)
        if (SLOT_55 == 1):
            GFX_OffsetX(200000)
            GFX_OffsetY(400000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(5, 1)
        if (SLOT_55 == 2):
            GFX_OffsetX(800000)
            GFX_OffsetY(0)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(6, 1)
        if (SLOT_55 == 3):
            GFX_OffsetX(-400000)
            GFX_OffsetY(4294567296)
            if (SLOT_57 == 2):
                GFX_OffsetY(200000)
            elif (SLOT_57 == 8):
                GFX_OffsetY(4294767296)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(7, 1)
        if (SLOT_55 == 4):
            GFX_OffsetX(800000)
            GFX_OffsetY(0)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(8, 1)
    if SLOT_53:
        clearUponHandler(32)
        if (SLOT_55 == 1):
            GFX_OffsetX(200000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(5, 1)
        if (SLOT_55 == 2):
            GFX_OffsetX(400000)
            GFX_OffsetY(400000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(6, 1)
        if (SLOT_55 == 3):
            GFX_OffsetX(400000)
            GFX_OffsetY(4294567296)
            if (SLOT_57 == 2):
                GFX_OffsetY(200000)
            elif (SLOT_57 == 8):
                GFX_OffsetY(4294767296)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(7, 1)
        if (SLOT_55 == 4):
            GFX_OffsetX(400000)
            GFX_OffsetY(400000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(8, 1)
    if SLOT_IsInOverdrive2:
        clearUponHandler(32)
        if (SLOT_55 == 1):
            GFX_OffsetX(200000)
            GFX_OffsetY(0)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(5, 1)
        if (SLOT_55 == 2):
            GFX_OffsetX(400000)
            GFX_OffsetY(0)
            if (SLOT_57 == 2):
                GFX_OffsetX(-100000)
                GFX_OffsetY(4294867296)
            elif (SLOT_57 == 8):
                GFX_OffsetX(-100000)
                GFX_OffsetY(100000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(6, 1)
        if (SLOT_55 == 3):
            GFX_OffsetX(400000)
            GFX_OffsetY(0)
            if (SLOT_57 == 2):
                GFX_OffsetX(-100000)
                GFX_OffsetY(4294867296)
            elif (SLOT_57 == 8):
                GFX_OffsetX(-100000)
                GFX_OffsetY(100000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(7, 1)
        if (SLOT_55 == 4):
            GFX_OffsetX(400000)
            GFX_OffsetY(0)
            if (SLOT_57 == 2):
                GFX_OffsetX(-100000)
                GFX_OffsetY(4294867296)
            elif (SLOT_57 == 8):
                GFX_OffsetX(-100000)
                GFX_OffsetY(100000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(8, 1)
    if (SLOT_55 == 5):
        clearUponHandler(3)
        sendToLabel(0)
    SLOT_55 = (SLOT_55 + 1)

@Subroutine
def DriveSpeed():
    Unknown1019(20)
    YAccel(20)
    Unknown1108(0)
    if SLOT_12:
        if SLOT_13:
            GFX_0('MAKERMoveEff', -1)
    Unknown48(3, 2, 12, 23, 2, 12)
    Unknown48(3, 2, 13, 23, 2, 13)

@State
def __5D_SPMark():

    def upon_IMMEDIATE():
        Unknown2009()
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        if SLOT_113:
            SLOT_55 = 1
            if random_(2, 0, 25):
                SLOT_51 = 1
            elif random_(2, 0, 33):
                SLOT_52 = 1
            elif random_(2, 0, 50):
                SLOT_53 = 1
            else:
                SLOT_54 = 1
            if random_(2, 0, 50):
                SLOT_57 = 0
            elif random_(2, 0, 50):
                SLOT_57 = 2
            else:
                SLOT_57 = 8

        def upon_3():
            if (not SLOT_55):
                if CheckInput(0x1):
                    callSubroutine('LeverInput')
                    SLOT_51 = 1
                    SLOT_52 = 0
                    SLOT_53 = 0
                    SLOT_54 = 0
                elif CheckInput(0xa):
                    callSubroutine('LeverInput')
                    SLOT_51 = 0
                    SLOT_52 = 1
                    SLOT_53 = 0
                    SLOT_54 = 0
                elif CheckInput(0x13):
                    callSubroutine('LeverInput')
                    SLOT_51 = 0
                    SLOT_52 = 0
                    SLOT_53 = 1
                    SLOT_54 = 0
                elif SLOT_11:
                    if CheckInput(0x1c):
                        callSubroutine('LeverInput')
                        SLOT_51 = 0
                        SLOT_52 = 0
                        SLOT_53 = 0
                        SLOT_54 = 1
            else:
                clearUponHandler(32)
                callSubroutine('CourseSetting')

        def upon_32():
            SLOT_51 = 0
            SLOT_52 = 0
            SLOT_53 = 0
            SLOT_54 = 1
            SLOT_55 = 1
            SLOT_11 = 1
    sprite('null', 300)
    GFX_OffsetY(150000)
    label(0)
    sprite('null', 5)
    Unknown21007(3, 32)
    Unknown1086(3)
    GFX_OffsetY(150000)
    SFX_0('000_airdash_0')
    sprite('Drive_TameMoveAtk', 5)
    Unknown48(23, 2, 56, 5, 2, 22)
    if SLOT_38:
        Unknown47(1, 2, 22, 2, 56, 2, 12)
    else:
        Unknown47(1, 2, 56, 2, 22, 2, 12)
    Unknown48(23, 2, 56, 5, 2, 23)
    Unknown47(1, 2, 56, 2, 23, 2, 13)
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown21007(5, 32)
    endMomentum(1)
    Unknown48(3, 2, 12, 23, 2, 12)
    Unknown48(3, 2, 13, 23, 2, 13)
    Unknown1086(5)
    SFX_0('002_highjump_0')
    GFX_0('test1', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48(23, 2, 56, 6, 2, 22)
    if SLOT_38:
        Unknown47(1, 2, 22, 2, 56, 2, 12)
    else:
        Unknown47(1, 2, 56, 2, 22, 2, 12)
    Unknown48(23, 2, 56, 6, 2, 23)
    Unknown47(1, 2, 56, 2, 23, 2, 13)
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown21007(6, 32)
    endMomentum(1)
    Unknown48(3, 2, 12, 23, 2, 12)
    Unknown48(3, 2, 13, 23, 2, 13)
    Unknown1086(6)
    SFX_0('001_airbackdash_0')
    GFX_0('test2', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48(23, 2, 56, 7, 2, 22)
    if SLOT_38:
        Unknown47(1, 2, 22, 2, 56, 2, 12)
    else:
        Unknown47(1, 2, 56, 2, 22, 2, 12)
    Unknown48(23, 2, 56, 7, 2, 23)
    Unknown47(1, 2, 56, 2, 23, 2, 13)
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown21007(7, 32)
    endMomentum(1)
    Unknown48(3, 2, 12, 23, 2, 12)
    Unknown48(3, 2, 13, 23, 2, 13)
    Unknown1086(7)
    SFX_0('000_airdash_0')
    GFX_0('test3', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48(23, 2, 56, 8, 2, 22)
    if SLOT_38:
        Unknown47(1, 2, 22, 2, 56, 2, 12)
    else:
        Unknown47(1, 2, 56, 2, 22, 2, 12)
    Unknown48(23, 2, 56, 8, 2, 23)
    Unknown47(1, 2, 56, 2, 23, 2, 13)
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtkFinish')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown21007(8, 32)
    Unknown21007(3, 33)
    endMomentum(1)
    Unknown1086(8)

@State
def Mark():

    def upon_IMMEDIATE():
        ProjectileHitWall(1)
        Unknown3032()
        Unknown4003('jbef_marker.DIG', '')
        GFX_SetPalette(2)
        Unknown4047(1, 1, 1)
        Unknown23067('jbef_drive_add')
        SFX_3('jbse_06')

        def upon_32():
            GFX_1('jbef_drive_move', -1)
            sendToLabel(0)
        sendToLabelUpon(44, 0)
    sprite('null', 120)
    label(0)
    sprite('null', 6)
    clearUponHandler(32)
    clearUponHandler(44)
    sprite('null', 6)
    Unknown1099(120)
    Unknown3004(-42)

@State
def MAKERMoveEff():

    def upon_IMMEDIATE():
        ProjectileDisapperOnHit(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown1108(0)
        Unknown23013(1)
        Unknown3032()
        Unknown4003('jbef_markerMove', '')

        def upon_32():
            clearUponHandler(32)
            sendToLabel(0)
    label(1)
    sprite('null', 6)
    Unknown1059(-100)
    GFX_0('MAKERMoveEffSumi', 100)
    ExitState()
    label(0)
    sprite('null', 6)
    Unknown3004(-42)

@State
def MAKERMoveEffSumi():

    def upon_IMMEDIATE():
        Unknown4006(2)
        Unknown4007(2)
        Unknown4010(2)
        IsInvisibility(1)
    sprite('vrefjb_markerMoveEXpoints', 1)
    GFX_SetPalette(2)
    PFX('jbef_drive_sumi', 0)
    PFX('jbef_drive_sumi', 1)
    PFX('jbef_drive_sumi', 2)

@State
def jbef203_zanzou():

    def upon_IMMEDIATE():
        Unknown4008(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou2')
    sprite('vrefjb203_00', 10)

@State
def test1():

    def upon_IMMEDIATE():
        ProjectileDisapperOnHit(3)
        GFX_OffsetY(4294767296)
        GFX_Scale(950)
        Unknown3026(4280295424)
        Unknown23022(1)
        Unknown2003(1)
    sprite('jb252_08', 15)
    Unknown3004(30)
    sprite('jb252_08', 10)
    Unknown3004(-20)

@State
def test2():

    def upon_IMMEDIATE():
        ProjectileDisapperOnHit(3)
        GFX_OffsetY(4294867296)
        GFX_Scale(950)
        Unknown3026(4280295424)
        Unknown23022(1)
        Unknown2003(1)
    sprite('jb431_09', 15)
    Unknown3004(30)
    sprite('jb431_09', 10)
    Unknown3004(-20)

@State
def test3():

    def upon_IMMEDIATE():
        ProjectileDisapperOnHit(3)
        GFX_OffsetY(4294767296)
        GFX_Scale(950)
        Unknown3026(4280295424)
        Unknown23022(1)
        Unknown2003(1)
    sprite('jb404_05', 15)
    Unknown3004(30)
    sprite('jb404_05', 10)
    Unknown3004(-20)

@State
def MarkingPoint():

    def upon_IMMEDIATE():
        Unknown4025(22)
        Unknown3032()
        GFX_Scale(700)

        def upon_16():
            Unknown2071(22, 0, 0, 100, 1)

        def upon_32():
            sendToLabel(0)
    sprite('null', 32767)
    Unknown3001(170)
    GFX_2('jbef_marking_hatudo')
    Unknown4003('jbef_marker2.DIG', '')
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def jbeff_warp():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('jbef_shunsin', '')
        Unknown2054(1)
        GFX_Scale(1000)
        GFX_OffsetY(150000)
        Unknown3001(150)
    sprite('null', 7)
    GFX_1('jbef_shunsin', -1)
    Unknown1099(350)
    sprite('null', 14)
    Unknown1099(30)

@State
def Shot_Eff():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(800)
        hitstun(18)
        AirUntechableTime(30)
        blockstun(16)
        AttackP1(80)
        SameMoveProration(80)
        AirPushbackY(18000)
        FireFX(1)
        StarterRating(2)
        if SLOT_137:
            DamageMultiplier(80)
        physicsXImpulse(10000)
        physicsYImpulse(26000)
        setGravity(1600)
        GFX_Scale(2000)

        def upon_32():
            physicsXImpulse(5000)
        ProjectileHitWall(1)
        FireBall(2, 2, 2, 2, 2, 0, 2, 0)
        

        def upon_54():
            sendToLabel(580)

        def upon_3():
            if (SLOT_2 >= 3):
                sendToLabel(0)
        Unknown23026(100000)

        def upon_5():
            Unknown2038(1)
            YAccel(-90)
            if (SLOT_13 <= 26000):
                physicsYImpulse(26000)
            Unknown8000(104, 1, 0)
            SFX_0('015_blaze_1')
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0
    sprite('Shot_Atk', 300)
    IsInvisibility(1)
    GFX_0('jbef407_Nekodama', -1)
    label(0)
    sprite('Shot_Atk', 1)
    clearUponHandler(3)
    label(580)
    sprite('null', 20)
    Unknown23027()
    endMomentum(1)
    clearUponHandler(3)
    clearUponHandler(54)
    Unknown21012('jbef407_Nekodama', 32)

@State
def jbef407_NekodamaRady():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(2)
        if SLOT_95:
            GFX_SetPalette(3)
        Unknown3001(170)
        GFX_OffsetY(4294917296)
    sprite('vrefjb407_00', 5)
    Unknown4047(2, 2, 2)
    PFX('jbef_407_nokosi', 0)
    Unknown4047(2, 2, 2)
    PFX('jbef_407_nokosi', 1)
    Unknown4047(2, 2, 2)
    PFX('jbef_407_nokosi', 2)
    Unknown4047(2, 2, 2)
    PFX('jbef_407_nokosi', 3)
    sprite('vrefjb407_01', 5)
    Unknown4047(2, 2, 2)
    PFX('jbef_407_nokosi', 0)
    Unknown4047(2, 2, 2)
    PFX('jbef_407_nokosi', 1)
    Unknown4047(2, 2, 2)
    PFX('jbef_407_nokosi', 2)
    sprite('vrefjb407_02', 5)
    Unknown4047(2, 2, 2)
    PFX('jbef_407_nokosi', 0)
    Unknown4047(2, 2, 2)
    PFX('jbef_407_nokosi', 1)
    Unknown4047(2, 2, 2)
    PFX('jbef_407_nokosi', 2)
    sprite('vrefjb407_03', 5)
    Unknown4047(2, 2, 2)
    PFX('jbef_407_nokosi', 0)
    Unknown4047(2, 2, 2)
    PFX('jbef_407_nokosi', 1)
    Unknown4047(2, 2, 2)
    PFX('jbef_407_nokosi', 2)
    sprite('vrefjb407_04', 10)
    Unknown4047(2, 2, 2)
    PFX('jbef_407_nokosi', 0)

@State
def jbef407_Nekodama():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        GFX_SetPalette(2)
        if SLOT_95:
            GFX_SetPalette(3)
        Unknown3001(170)
        EnableAfterimage(1)
        AfterimageCount(3)
        Unknown3070(2)
        sendToLabelUpon(32, 1)
    sprite('vrefjb407_10', 1)
    PFX_Scale(800)
    PFX_Rotation(-30000)
    PFX('jbef_407_shock', -1)
    SFX_0('015_blaze_0')
    label(0)
    sprite('vrefjb407_10', 3)
    Unknown1073(45000)
    Unknown4047(2, 2, 2)
    PFX_Scale(1500)
    PFX('jbef_407_nokosi', -1)
    sprite('vrefjb407_10', 3)
    Unknown1073(45000)
    gotoLabel(0)
    label(1)
    sprite('vrefjb407_20', 2)
    EnableAfterimage(0)
    Unknown4010(0)
    Unknown4007(0)
    Unknown4009(0)
    Unknown4047(2, 2, 2)
    PFX_Scale(2000)
    PFX('jbef_407_nokosi', -1)
    GFX_0('jbef407_NekodamaAura', -1)
    sprite('vrefjb407_21', 2)
    sprite('vrefjb407_22', 2)
    sprite('vrefjb407_23', 2)
    sprite('vrefjb407_24', 2)
    loopRest()

@State
def jbef407_NekodamaAura():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        GFX_Scale(1500)
        Unknown1074(1500)
        GFX_SetPalette(2)
        if SLOT_95:
            GFX_SetPalette(3)
        Unknown21004(2)
        Unknown4003('jbef_407Aura00', '')
    sprite('null', 30)
    Unknown4010(0)
    Unknown4007(0)
    Unknown4009(0)
    Unknown3004(-8)
    Unknown1099(15)
    loopRest()

@State
def jbef408_DashEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        GFX_2('jbef_408_dash')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 8)
    Unknown3004(-31)
    loopRest()

@State
def jb430_slashMatome():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown1006(0)
        Unknown3032()
    sprite('null', 3)
    GFX_0('jb430_slash1', 100)
    SFX_0('012_stab_deep')
    sprite('null', 3)
    GFX_0('jb430_slash2', 100)
    SFX_0('012_stab_deep')
    sprite('null', 3)
    GFX_0('jb430_slash3', 100)
    SFX_0('012_stab_deep')
    sprite('null', 3)
    GFX_0('jb430_slashAdd', 100)
    GFX_0('jb430_slash4', 100)
    GFX_1('jbef_430_suminokosi', 100)
    SFX_0('012_stab_deep')
    sprite('null', 15)
    sprite('null', 58)
    Unknown4010(0)
    Unknown21012('jb430_slashAdd', 32)
    GFX_0('jb430_slashEnd', 100)
    GFX_Unload('jb430_slash1')
    GFX_Unload('jb430_slash2')
    GFX_Unload('jb430_slash3')
    GFX_Unload('jb430_slash4')

@State
def jb430_slashEnd():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        GFX_SetPalette(2)
        Unknown21004(1)
        Unknown1006(0)
        Unknown2054(1)
    sprite('null', 58)
    Unknown4003('jbef_430fallslashEnd', '')
    GFX_Unload('jb430_slash1')
    GFX_Unload('jb430_slash2')
    GFX_Unload('jb430_slash3')
    GFX_Unload('jb430_slash4')
    Unknown1067(7)

@State
def jb430_slashAdd():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        GFX_SetPalette(2)
        Unknown21004(1)
        Unknown1006(0)
        GFX_OffsetY(4294947296)
        Unknown1057(400)
        sendToLabelUpon(32, 0)
        Unknown23015(12)
    sprite('null', 32767)
    Unknown4003('jbef_430baclkaura00', '')
    label(0)
    sprite('null', 10)
    Unknown2054(1)
    Unknown1059(20)
    sprite('null', 30)
    Unknown3004(-8)

@State
def jb430_slash1():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4003('jbef_430fallslash00', '')
        Unknown1006(0)
        GFX_SetPalette(2)
        Unknown21004(1)
    sprite('null', 5)
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 32767)

@State
def jb430_slash2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4003('jbef_430fallslash01', '')
        Unknown1006(0)
        GFX_SetPalette(2)
        Unknown21004(1)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 32767)

@State
def jb430_slash3():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4003('jbef_430fallslash02', '')
        Unknown1006(0)
        GFX_SetPalette(2)
        Unknown21004(1)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 32767)

@State
def jb430_slash4():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4003('jbef_430fallslash03', '')
        Unknown1006(0)
        GFX_SetPalette(2)
        Unknown21004(1)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 32767)

@State
def jb430_ODSlash00():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown1006(0)
        GFX_SetPalette(2)
        Unknown21004(1)
        GFX_Scale(800)
    sprite('null', 4)
    Unknown4003('jbef_430OD_slash00', '')
    GFX_0('jb430_ODSlash00BG', 100)
    sprite('null', 4)
    Unknown4003('jbef_430OD_slash01', '')
    sprite('null', 10)
    Unknown4003('jbef_430OD_slash02', '')
    ScreenShake(10000, 10000)
    Unknown1099(5)
    physicsYImpulse(-1250)
    sprite('null', 58)
    Unknown4003('jbef_430OD_slash02End', '')
    Unknown4010(0)

@State
def jb430_ODSlash00BG():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown1006(0)
        GFX_SetPalette(2)
        Unknown4047(1, 1, 1)
        Unknown23067('jbef_431od_slashadd')
    sprite('null', 18)
    sprite('null', 58)
    Unknown3004(-4)
    Unknown4010(0)

@State
def jb431_SlashEndEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1086(22)
        GFX_OffsetY(200000)
        GFX_SetPalette(2)
        Unknown21004(1)
    sprite('null', 6)
    GFX_2('jbef_431crossAdd')
    Unknown4003('jbef_430cross00.DIG', '')
    GFX_Scale(2)
    Unknown1057(100)
    Unknown1099(100)
    SFX_3('jbse_09')
    sprite('null', 20)
    Unknown1099(1)
    sprite('null', 27)
    ScreenShake(10000, 10000)
    GFX_1('jbef_431slashEnd', -1)
    Unknown4003('jbef_430slash00.DIG', '')
    Unknown1099(0)
    Unknown1097(400)
    SFX_0('025_cleanhit_slash')
    sprite('null', 15)
    sprite('null', 15)
    Unknown3004(-17)

@State
def jb431_SlashEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1086(22)
        Unknown1006(0)
        GFX_OffsetY(200000)
        Unknown23067('jbef_431slash')
    sprite('null', 15)
    GFX_0('jb431_SlashBloomEff', 100)

@State
def jb431_SlashBloomEff():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_SetPalette(2)
        Unknown4047(1, 1, 1)
        Unknown23067('jbef_431slashBloom')
    sprite('null', 15)

@State
def jb431_CircleShockEff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        GFX_Scale(2000)
    sprite('null', 15)
    Unknown4003('jbef_430circle00.DIG', '')
    Unknown1099(40)

@State
def jb431OD_SlashEffMatome():

    def upon_IMMEDIATE():
        Unknown4010(2)
        sendToLabelUpon(32, 0)
    sprite('null', 4)
    GFX_0('jb431OD_SlashEff00', -1)
    sprite('null', 4)
    GFX_0('jb431OD_SlashEff01', -1)
    sprite('null', 32767)
    GFX_0('jb431OD_SlashEff02', -1)
    label(0)
    sprite('null', 4)
    Unknown21012('jb431OD_SlashEff00', 32)
    sprite('null', 4)
    Unknown21012('jb431OD_SlashEff01', 32)
    sprite('null', 1)
    Unknown21012('jb431OD_SlashEff02', 32)

@State
def jb431OD_SlashEff00():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        GFX_OffsetY(200000)
        GFX_SetPalette(2)
        Unknown21004(1)
        GFX_OffsetX(-1000000)
        GFX_Scale(1000)
        Unknown4003('jbef_430ODslash00.DIG', '')
        Unknown4047(1, 1, 1)
        Unknown23067('jbef_431od_slashadd')
        sendToLabelUpon(32, 1)
    sprite('null', 5)
    Unknown3001(0)
    ScreenShake(2500, 2500)
    sprite('null', 5)
    Unknown3004(51)
    GFX_0('jb431OD_jubei00', 100)
    sprite('null', 32767)
    label(1)
    sprite('null', 28)
    Unknown4010(0)
    Unknown4003('jbef_430ODslash00End.DIG', '')
    Unknown1099(5)
    sprite('null', 30)
    Unknown3004(-8)

@State
def jb431OD_SlashEff01():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        GFX_OffsetY(200000)
        GFX_SetPalette(2)
        Unknown21004(1)
        GFX_OffsetX(-700000)
        GFX_Scale(800)
        Unknown4047(1, 1, 1)
        Unknown23067('jbef_431od_slashadd')
        Unknown4003('jbef_430ODslash01.DIG', '')
        sendToLabelUpon(32, 1)
    sprite('null', 5)
    Unknown3001(0)
    ScreenShake(2500, 2500)
    sprite('null', 5)
    Unknown3004(51)
    GFX_0('jb431OD_jubei01', 100)
    sprite('null', 32767)
    label(1)
    sprite('null', 28)
    Unknown4010(0)
    Unknown4003('jbef_430ODslash01End.DIG', '')
    Unknown1099(5)
    sprite('null', 30)
    Unknown3004(-8)

@State
def jb431OD_SlashEff02():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        GFX_OffsetY(200000)
        GFX_SetPalette(2)
        Unknown21004(1)
        GFX_OffsetX(-300000)
        GFX_Scale(800)
        Unknown4047(1, 1, 1)
        Unknown23067('jbef_431od_slashadd')
        Unknown4003('jbef_430ODslash02.DIG', '')
        sendToLabelUpon(32, 1)
    sprite('null', 5)
    Unknown3001(0)
    ScreenShake(2500, 2500)
    sprite('null', 5)
    Unknown3004(51)
    GFX_0('jb431OD_jubei02', 100)
    sprite('null', 32767)
    label(1)
    sprite('null', 28)
    Unknown4010(0)
    Unknown4003('jbef_430ODslash02End.DIG', '')
    Unknown1099(5)
    sprite('null', 30)
    Unknown3004(-8)

@State
def jb431OD_jubei00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        GFX_OffsetY(4294867296)
        Unknown23015(1)
    sprite('jb201_03', 10)
    SFX_3('jbse_09')
    SFX_0('000_airdash_0')
    sprite('jb201_03', 10)
    Unknown3004(-26)
    physicsXImpulse(3000)

@State
def jb431OD_jubei01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        GFX_OffsetY(4294867296)
        Unknown23015(1)
    sprite('jb211_06', 10)
    SFX_3('jbse_02')
    sprite('jb211_06', 10)
    Unknown3004(-26)
    physicsXImpulse(3000)

@State
def jb431OD_jubei02():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        GFX_OffsetY(4294867296)
        Unknown23015(1)
    sprite('jb400_03', 10)
    physicsXImpulse(3000)
    SFX_0('000_airdash_0')
    sprite('jb400_03', 10)
    Unknown3004(-26)
    physicsXImpulse(3000)

@State
def jb432_eyerayEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(2)
        Unknown2054(2)
    sprite('vrefjb432_00', 6)
    sprite('vrefjb432_01', 6)
    sprite('vrefjb432_02', 6)
    sprite('vrefjb432_03', 6)
    PFX('jbef_432buff_hatudo', 100)

@State
def jb432_BodyAuraEff():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('jbef_432Aura00.DIG', '')
        GFX_OffsetY(250000)
        GFX_Scale(900)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(25)
    GFX_1('jbef_432_shock', 100)
    GFX_0('jb432_BodyAuraEffCore', 100)
    sprite('null', 10)
    sprite('null', 20)
    Unknown3004(-12)
    sprite('null', 20)
    sprite('null', 20)
    Unknown3004(-12)

@State
def jb432_BodyAuraEffCore():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('jbef_432AuraCore.DIG', '')
        GFX_Scale(400)
        GFX_OffsetY(4294917296)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(25)
    sprite('null', 10)
    sprite('null', 20)
    Unknown3004(-12)

@State
def jb440_startAtk00():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3032()
        GFX_SetPalette(2)
        Unknown21004(1)
        Unknown4003('jbef_440startAtk00', '')
        GFX_Scale(400)
        GFX_OffsetY(300000)
        GFX_OffsetX(150000)
    sprite('null', 3)
    Unknown1057(150)
    Unknown1065(45)
    sprite('null', 3)
    Unknown1057(300)
    Unknown1065(75)
    sprite('null', 3)
    Unknown1057(300)
    Unknown1065(75)
    sprite('null', 3)
    Unknown1057(150)
    Unknown1065(37)
    sprite('null', 3)
    Unknown4003('jbef_440startAtk01', '')
    Unknown4010(0)
    Unknown4007(0)
    Unknown4009(0)
    Unknown1099(5)
    sprite('null', 56)
    Unknown1065(75)
    Unknown4003('jbef_440startAtk01end', '')
    Unknown3004(-4)

@State
def jb440_slash00():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_SetPalette(2)
        Unknown21004(1)
        Unknown4003('jbef_440slash00.DIG', '')
        GFX_Scale(400)
        GFX_OffsetY(300000)
        GFX_OffsetX(200000)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(26)
    Unknown21010(1)
    GFX_SetPalette(2)
    Unknown4047(1, 1, 1)
    PFX('jbef_440suminokosi', 100)
    sprite('null', 5)
    Unknown21010(0)
    sprite('null', 57)
    Unknown4003('jbef_440slash00End.DIG', '')
    Unknown1099(2)

@State
def jb440_AddAtk():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        GFX_Scale(500)
        GFX_OffsetX(50000)
    sprite('null', 4)
    GFX_0('jb440_AddAtk00', 100)
    Unknown21010(1)
    sprite('null', 4)
    GFX_0('jb440_AddAtk01', 100)
    sprite('null', 10)
    Unknown1099(3)
    physicsYImpulse(-2500)
    physicsXImpulse(-1500)
    GFX_SetPalette(2)
    Unknown4047(1, 1, 1)
    PFX('jbef_440suminokosi2', 100)
    Unknown21004(1)
    Unknown4003('jbef_440AddAtk02.DIG', '')
    Unknown21010(0)
    sprite('null', 57)
    Unknown4003('jbef_440AddAtk02End.DIG', '')
    Unknown4010(0)

@State
def jb440_AddAtk00():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown4010(2)
        Unknown3032()
        GFX_SetPalette(2)
        Unknown21004(1)
        Unknown4003('jbef_440AddAtk00.DIG', '')
        GFX_Scale(500)
    sprite('null', 4)
    sprite('null', 5)
    Unknown3001(128)
    Unknown3004(-25)

@State
def jb440_AddAtk01():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown4010(2)
        Unknown3032()
        GFX_SetPalette(2)
        Unknown21004(1)
        Unknown4003('jbef_440AddAtk01.DIG', '')
        GFX_Scale(500)
    sprite('null', 4)
    sprite('null', 5)
    Unknown3001(128)
    Unknown3004(-25)

@State
def jb430_Eff():

    def upon_IMMEDIATE():
        ProjectileDisapperOnHit(3)
        Unknown2054(1)
        Unknown1056(600)
        Unknown1064(6000)
    sprite('null', 30)

@State
def jb430_EffOD():

    def upon_IMMEDIATE():
        ProjectileDisapperOnHit(3)
        Unknown2054(1)
        Unknown1056(1000)
        Unknown1064(10000)
    sprite('null', 30)

@State
def jb430_BunshinA():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        EnableAfterimage(1)
        AfterimageType(2)
        Unknown23022(1)
    sprite('jb430_04', 12)
    physicsXImpulse(25000)
    Unknown3004(-21)

@State
def jb430_BunshinB():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        EnableAfterimage(1)
        AfterimageType(2)
        Unknown23022(1)
    sprite('jb430_04', 12)
    physicsXImpulse(-25000)
    Unknown3004(-21)

@State
def jb431_Eff():

    def upon_IMMEDIATE():
        ProjectileDisapperOnHit(3)
        Unknown2054(1)
        Unknown1056(6000)
        Unknown1064(600)
    sprite('null', 30)
    GFX_2('ef_ukemi')

@State
def jb431_EffOD():

    def upon_IMMEDIATE():
        ProjectileDisapperOnHit(3)
        Unknown2054(1)
        Unknown1064(600)
        Unknown1062(1000, 5000)
        Unknown1077(10000, 60000)
    sprite('null', 3)
    GFX_2('ef_ukemi')

@State
def jb431_BunshinA():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        EnableAfterimage(1)
        AfterimageType(2)
        Unknown23022(1)
    sprite('jb431_01', 12)
    physicsXImpulse(25000)
    Unknown3004(-21)

@State
def jb431_BunshinB():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        EnableAfterimage(1)
        AfterimageType(2)
        Unknown23022(1)
    sprite('jb431_01', 12)
    physicsXImpulse(-25000)
    Unknown3004(-21)

@State
def UltimateChage_Atk():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(1500)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(18)
        AirPushbackX(-1000)
        AirPushbackY(35000)
        YImpluseBeforeWallbounce(1800)
        StunLength(51)
        StunRecoveryLength(41)
        PushbackX(8000)
        AirUntechableTime(60)
        StarterRating(2)
        GFX_Scale(1200)
    sprite('Chage_Atk', 3)

@State
def UltimateChageEX_Atk():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(1500)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(40000)
        AirPushbackY(30000)
        PushbackX(8000)
        AirUntechableTime(60)
        StarterRating(2)
        GFX_Scale(1200)
    sprite('Chage_Atk', 3)

@State
def jb432_Eff():

    def upon_IMMEDIATE():
        ProjectileDisapperOnHit(3)
        Unknown2054(1)
        GFX_Scale(1500)
        Unknown23151(3, 103)
    sprite('null', 30)
    GFX_2('ef_ukemi')

@State
def ChageAuraGenerator():

    def upon_IMMEDIATE():

        def upon_3():
            SLOT_51 = (SLOT_51 + 1)
            if (not op(4, 2, 51, 0, 30)):
                SLOT_52 = 0
                Unknown48(23, 2, 52, 2, 2, 30)
                if (not SLOT_52):
                    Unknown36(3)
                    GFX_0('ChageAura', 103)
                    Unknown35()
    sprite('null', 32767)

@State
def ChageAura():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4025(3)
        ProjectileDisapperOnHit(3)
        Unknown3032()
        Unknown2054(1)
        GFX_Scale(1000)
    sprite('null', 30)
    GFX_2('jbef_432_buffNml')

@State
def ChageAura2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4025(3)
        ProjectileDisapperOnHit(3)
        Unknown3032()
        Unknown2054(1)
        GFX_Scale(1000)
    sprite('null', 30)
    GFX_2('jbef_432_buff2')

@State
def BurstDD_Camera():

    def upon_IMMEDIATE():

        def upon_32():
            sendToLabel(580)
        GFX_OffsetX(350000)
    sprite('null', 3000)
    CameraControlEnable(1)
    Unknown20011('1700000017000000')
    label(580)
    sprite('null', 1)
    CameraControlEnable(0)
    Unknown20011('0000000000000000')

@State
def Astral_Camera():

    def upon_IMMEDIATE():
        Unknown4022(3)
        GFX_OffsetX(300000)

        def upon_32():
            sendToLabel(0)

        def upon_33():
            sendToLabel(1)

        def upon_34():
            sendToLabel(2)

        def upon_35():
            sendToLabel(3)

        def upon_36():
            sendToLabel(4)

        def upon_37():
            sendToLabel(5)

        def upon_38():
            sendToLabel(6)
    sprite('null', 32767)
    CameraControlEnable(1)
    Unknown20003(1)
    Unknown20004(1)
    Unknown20006(1)
    label(0)
    sprite('null', 32767)
    Unknown20009(600)
    GFX_OffsetX(300000)
    label(1)
    sprite('null', 32767)
    Unknown20009(1000)
    GFX_OffsetX(-300000)
    label(2)
    sprite('null', 32767)
    Unknown4022(0)
    physicsXImpulse(50000)
    label(3)
    sprite('null', 32767)
    physicsXImpulse(0)
    GFX_OffsetX(-300000)
    label(4)
    sprite('null', 32767)
    Unknown4007(22)
    label(5)
    sprite('null', 32767)
    Unknown4007(0)
    label(6)
    sprite('null', 110)
    Unknown1000(700000)
    Unknown1006(1000000)
    sprite('null', 20)
    physicsXImpulse(-34000)
    physicsYImpulse(-36000)
    sprite('null', 32767)
    endMomentum(1)

@State
def jb450_ZanEff():

    def upon_IMMEDIATE():
        Unknown4006(2)
    sprite('null', 6)
    SFX_0('006_swing_blade_1')
    SFX_0('010_swing_sword_2')

@State
def jb450_AtkAura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown4003('jbef_450atkaura00', '')
        GFX_2('jbef_450_underlight')
        sendToLabelUpon(32, 0)
    sprite('null', 10)
    Unknown3001(0)
    GFX_0('jb450_AtkAura2', -1)
    SFX_0('016_explode_0')
    sprite('null', 10)
    Unknown3004(13)
    SFX_0('016_explode_0')
    sprite('null', 32767)
    GFX_0('jb450_AtkAura2', -1)
    label(0)
    sprite('null', 20)
    Unknown1099(15)
    Unknown3004(-12)

@State
def jb450_AtkAura2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4003('jbef_450atkaura01', '')
        GFX_Scale(500)
    sprite('null', 39)

@State
def jb450_kaihouAura():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4003('jbef_450kaihoaura00', '')
        GFX_Scale(1200)
        Unknown1065(300)
    sprite('null', 8)
    ScreenShake(10000, 10000)
    GFX_0('jb450_kaihouShock', -1)
    sprite('null', 1)
    sprite('null', 230)
    sprite('null', 15)
    Unknown3004(-17)
    Unknown4007(0)

@State
def jb450_kaihouShock():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown3032()
        Unknown4003('jbef_450kaihoshock', '')
        GFX_Scale(1300)
        Unknown1089(300)
    sprite('null', 10)
    GFX_1('jbef_450shockbrust', -1)
    Unknown1059(30)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown1059(10)

@State
def jb450_kidou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou2')
        EnableAfterimage(1)
        Unknown3001(180)
    sprite('vrefjb450_00kidou', 8)
    sprite('vrefjb450_01kidou', 16)

@State
def jb450_kidou2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_SetPalette(1)
        Unknown3033()
        callSubroutine('zanzou2')
        EnableAfterimage(1)
        Unknown3001(180)
    sprite('vrefjb450_02kidou', 8)
    sprite('vrefjb450_03kidou', 24)

@State
def jbef_450flash():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown3032()
        GFX_2('jbef_450flash')
    sprite('null', 30)

@State
def jbef_450weakpointBG():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown3032()
        Unknown4003('jbef_430weakpointBG', '')
        GFX_Scale(1200)
        Unknown1057(-100)
        Unknown1086(22)
        GFX_OffsetY(180000)
        GFX_OffsetX(-10000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    Unknown1099(120)
    Unknown3004(-12)
    loopRest()

@State
def jbef_450weakpoint():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown3032()
        GFX_2('jbef_450weakpoint')
        sendToLabelUpon(32, 0)
        Unknown23151(22, 109)
        Unknown4007(22)
    sprite('null', 20)
    Unknown3001(0)
    GFX_Scale(10)
    sprite('null', 10)
    Unknown3001(255)
    Unknown1099(100)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 10)
    Unknown1099(-80)
    loopRest()

@State
def jbef_450weakpoint_Terumi():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown3032()
        Unknown2005()
        GFX_SetPalette(4)
        sendToLabelUpon(32, 0)
        Unknown1086(22)
        Unknown4007(22)
        sendToLabelUpon(32, 0)
        Unknown4003('jbef_450terumi', '')
        GFX_OffsetY(25000)
    sprite('null', 30)
    Unknown3001(0)
    sprite('null', 40)
    Unknown3004(8)
    physicsXImpulse(-100)
    physicsYImpulse(100)
    sprite('null', 32767)
    physicsXImpulse(-50)
    physicsYImpulse(25)
    Unknown3004(0)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)
    loopRest()

@State
def jbef_450weakpoint_Hazama():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown3032()
        Unknown2005()
        GFX_SetPalette(4)
        sendToLabelUpon(32, 0)
        Unknown1086(22)
        Unknown4007(22)
        sendToLabelUpon(32, 0)
        Unknown4003('jbef_450terumi', '')
        GFX_OffsetY(25000)
    sprite('null', 30)
    Unknown3001(0)
    sprite('null', 40)
    Unknown3004(2)
    physicsXImpulse(-100)
    physicsYImpulse(100)
    sprite('null', 32767)
    physicsXImpulse(-50)
    physicsYImpulse(25)
    Unknown3004(-6)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)
    loopRest()

@State
def jb450_BG():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('jbef_450wasibg', '')
        Unknown23015(2)
        Unknown1064(800)
        Unknown1088(1000)
        Unknown1056(1000)
        GFX_OffsetY(80000)
        Unknown3001(240)
    sprite('null', 150)
    GFX_0('jb450_BGsub', -1)
    sprite('null', 9)
    Unknown3004(-26)

@State
def jb450_BGsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('jbef_450filmgate', '')
        Unknown23015(1)
        Unknown1064(800)
        Unknown1088(1000)
        Unknown1056(1000)
    sprite('null', 150)
    sprite('null', 9)
    Unknown3004(-26)

@State
def jbef_450ZanzoNokosiMato():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown4007(2)
        Unknown1006(0)
    sprite('null', 3)
    GFX_0('jbef_450ZanzoNokosi', -1)
    Unknown36(1)
    GFX_OffsetX(-400000)
    Unknown35()
    sprite('null', 3)
    GFX_0('jbef_450ZanzoNokosi', -1)
    Unknown36(1)
    GFX_OffsetX(-300000)
    Unknown35()
    sprite('null', 3)
    GFX_0('jbef_450ZanzoNokosi', -1)
    Unknown36(1)
    GFX_OffsetX(-200000)
    Unknown35()
    sprite('null', 60)
    GFX_0('jbef_450ZanzoNokosi', -1)
    Unknown36(1)
    GFX_OffsetX(-100000)
    Unknown35()

@State
def jbef_450ZanzoNokosi():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown4007(2)
        Unknown23015(11)
        Unknown1006(0)
    sprite('jb450_26', 50)
    Unknown3004(-5)

@State
def jb450_RedBG():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown20003(1)
        Unknown20004(1)
        Unknown4003('jbef_450redbg', '')
        Unknown23015(2)
    sprite('null', 30)
    Unknown3001(0)
    sprite('null', 55)
    Unknown3001(255)

@State
def jb450_BG2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('jbef_450_wasibg2', '')
        Unknown23015(2)
        GFX_Scale(400)
        GFX_OffsetX(-325000)
        Unknown3001(225)
        Unknown2054(1)
    sprite('null', 40)
    sprite('null', 50)
    Unknown3004(-12)
    sprite('null', 1)
    GFX_0('jb450_BGEnd', -1)

@State
def jb450_BGEnd():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('jbef_450bgend', '')
        GFX_Rotation(-25000)
        GFX_Scale(1200)
        Unknown23015(4)
        GFX_OffsetX(-1300000)
    sprite('null', 115)

@State
def jb450_Slash():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('jbef_450slash00', '')
        GFX_OffsetX(-50000)
    sprite('null', 5)
    ScreenShake(50000, 50000)
    Unknown1099(5)
    GFX_Scale(800)
    sprite('null', 5)
    ScreenShake(40000, 40000)
    sprite('null', 4)
    GFX_Scale(850)
    sprite('null', 4)
    GFX_Scale(900)
    sprite('null', 6)
    Unknown4003('jbef_450slash01', '')
    GFX_Scale(1100)
    sprite('null', 6)
    Unknown4003('jbef_450slash02', '')
    sprite('null', 40)
    GFX_0('jb450_SlashSub', -1)
    Unknown3001(0)

@State
def jb450_SlashSub():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4003('jbef_450slashRotate', '')
        GFX_Scale(700)
        GFX_OffsetY(1000000)
        GFX_OffsetX(-1250000)
        Unknown2054(1)
        Unknown21010(1)
    sprite('null', 4)
    Unknown1073(600000)
    SFX_3('jbse_08')
    sprite('null', 4)
    Unknown1073(600000)
    sprite('null', 4)
    Unknown1073(600000)
    sprite('null', 4)
    Unknown1073(600000)
    Unknown1097(100)
    sprite('null', 4)
    Unknown1073(600000)
    Unknown1097(100)
    sprite('null', 4)
    Unknown1073(600000)
    Unknown1097(100)
    sprite('null', 4)
    Unknown1073(600000)
    Unknown1097(100)
    sprite('null', 4)
    Unknown1073(600000)
    Unknown1097(100)
    sprite('null', 4)
    Unknown1073(600000)
    Unknown1097(100)
    sprite('null', 4)
    Unknown1073(600000)
    Unknown3004(-31)
    sprite('null', 4)
    Unknown1073(600000)

@State
def jb610_Slash():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('jbef_610slash00', '')
        GFX_OffsetX(100000)
        GFX_OffsetY(75000)
        GFX_Scale(1500)
    sprite('null', 5)
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 20)
    sprite('null', 57)
    Unknown3004(-4)
    Unknown4003('jbef_610slash01', '')

@State
def jb900_Ase():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('jbef_900ase')
    sprite('null', 20)
    Unknown3001(0)
    Unknown3004(12)
    sprite('null', 32767)

@State
def jb611_Tail_Event():

    def upon_IMMEDIATE():
        Unknown2019(500)
    sprite('jb611_00s', 8)
    sprite('jb611_01s', 8)
    sprite('jb611_02s', 8)
    label(0)
    sprite('jb611_03s', 10)
    sprite('jb611_04s', 10)
    sprite('jb611_05s', 10)
    sprite('jb611_06s', 10)
    loopRest()
    gotoLabel(0)

@State
def NOISE():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ef_eventnoise.DIG', '')
        Unknown4015()
        Unknown23015(4)
        Unknown23032(50)
        Unknown23033(50)
    sprite('null', 120)
    loopRest()