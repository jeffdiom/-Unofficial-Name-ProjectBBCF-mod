@State
def EMB():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(240000)
        Unknown2054(1)
        IsInvisibility(1)
        Unknown4003('ef_emb_AZ.DIG', '')
        Unknown23015(5)
        GFX_Scale(1500)
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
def EMB_AZ_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(240000)
        Unknown2054(1)
        IsInvisibility(1)
        Unknown4003('ef_emb_AZ.DIG', '')
        Unknown23015(5)
        GFX_Scale(1500)
    sprite('null', 10)
    Unknown3026(4278190080)
    Unknown3025(4294967295, 10)
    sprite('null', 10)
    Unknown3025(4286625023, 10)
    sprite('null', 10)
    Unknown3025(4278223103, 10)
    sprite('null', 10)
    Unknown3025(4278223103, 10)
    sprite('null', 80)

@State
def EMB_AZ_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(240000)
        Unknown2054(1)
        Unknown4003('ef_emb_AZ.DIG', '')
        Unknown23015(5)
        GFX_Scale(1500)
    sprite('null', 10)
    Unknown3026(4278190080)
    Unknown3025(2533294080, 10)
    sprite('null', 10)
    Unknown3025(2533304360, 10)
    sprite('null', 10)
    Unknown3025(2533340340, 10)
    sprite('null', 10)
    Unknown3025(2533294080, 10)
    sprite('null', 80)

@State
def az406_dummy():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1000)
        AirPushbackX(-3000)
        AirPushbackY(23000)
        AirUntechableTime(40)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        PunchFX(1)
        Hitstop(3)
        IsInvisibility(1)
        SameMoveProration(1)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpluseBeforeWallbounce(20)
            Unknown9346(1)
            Wallbounce(1)
            Wallstick(1)
            WallstickLength(30)
            if (SLOT_4 > 1):
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                GroundedHitstunAnimation(17)
                AirHitstunAnimation(17)
                Unknown1017()
    sprite('null', 2)
    sprite('vr_azef406_col', 3)

@State
def az406_dummy2():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(900)
        AirPushbackX(1000)
        AirPushbackY(26000)
        AirUntechableTime(40)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        PunchFX(1)
        Hitstop(3)
        IsInvisibility(1)
        SameMoveProration(1)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpluseBeforeWallbounce(20)
            Unknown9346(1)
            Wallbounce(1)
            Wallstick(1)
            WallstickLength(30)
            if (SLOT_4 > 1):
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                GroundedHitstunAnimation(17)
                AirHitstunAnimation(17)
                Unknown1017()
    sprite('null', 2)
    sprite('vr_azef406_col', 3)

@State
def rocktest():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_Scale(2000)
        Unknown1006(0)
    sprite('null', 1)
    sprite('null', 0)
    GFX_0('hibiware', -1)
    ScreenShake(8000, 8000)
    sprite('null', 5)
    Unknown4003('azef_406jiware.DIG', '')
    GFX_1('azef_406_stone', -1)
    sprite('null', 5)
    Unknown3004(-10)
    sprite('null', 14)

@State
def hibiware():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_Scale(1500)
        Unknown1006(0)
    sprite('null', 4)
    Unknown4003('azef_hibiware.DIG', '')
    sprite('null', 8)
    Unknown3004(-26)

@State
def __203swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        GFX_Scale(900)
    sprite('null', 14)
    GFX_0('203yugami', -1)
    Unknown4003('azef_203swing00.DIG', '')
    Unknown4015()

@State
def __203yugami():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        GFX_OffsetX(-25000)
        GFX_Scale(900)
    sprite('vr_azef203_yugami', 15)
    Unknown3057(1)
    Unknown3058(35000)
    Unknown3059(-2500)

@State
def __213swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3001(255)
        GFX_Scale(900)
    sprite('null', 14)
    GFX_0('213yugami', -1)
    Unknown4003('azef_213swing00.DIG', '')
    Unknown4015()

@State
def __213yugami():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        GFX_OffsetX(-25000)
        GFX_Scale(900)
    sprite('vr_azef213_yugami', 15)
    Unknown3057(1)
    Unknown3058(35000)
    Unknown3059(-2500)

@State
def __213rock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('azef_402rock.DIG', '')
        GFX_Scale(1000)
        GFX_OffsetX(-20000)
        GFX_OffsetY(15000)
    sprite('null', 5)
    sprite('null', 10)
    PFX_Scale(700)
    PFX('azef_402rocksmoke_pos', -1)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __253swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        Unknown3001(255)
        GFX_Scale(900)
    sprite('null', 6)
    Unknown4003('azef_253swing00.DIG', '')
    Unknown4015()

@State
def __253yugami():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        GFX_OffsetX(-50000)
        GFX_OffsetY(30000)
        GFX_Scale(900)
    sprite('vr_azef203_yugami', 15)
    Unknown3057(1)
    Unknown3058(17500)
    Unknown3059(-2500)

@State
def __232rock():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_Scale(1500)
        GFX_OffsetX(400000)
        Unknown4003('azef_232rock00.DIG', '')
    sprite('null', 1)
    GFX_OffsetY(4294927296)
    ScreenShake(5000, 5000)
    sprite('null', 2)
    GFX_OffsetY(40000)
    sprite('null', 2)
    Unknown3001(0)
    GFX_0('232rock01', -1)
    sprite('null', 4)
    GFX_0('232rock02', -1)
    sprite('null', 2)
    GFX_0('232rock03', -1)
    sprite('null', 20)
    GFX_0('232rock04', -1)

@State
def __232rock01():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_Scale(1500)
        Unknown4003('azef_232rock01.DIG', '')
        Unknown4015()
    sprite('null', 2)

@State
def __232rock02():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_Scale(1500)
        Unknown4003('azef_232rock02.DIG', '')
    sprite('null', 4)

@State
def __232rock03():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_Scale(1500)
        GFX_OffsetX(-150000)
        GFX_OffsetY(4294962296)
        Unknown4003('azef_232rock03.DIG', '')
        GFX_2('azef_rockshadow_00')
    sprite('null', 2)

@State
def __232rock04():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_Scale(1500)
        GFX_OffsetX(-150000)
        GFX_OffsetY(4294962296)
        Unknown4003('azef_232rock04.DIG', '')
        GFX_2('azef_rockshadow_00')
    sprite('null', 5)
    GFX_1('azef_232brokerock_rock2', -1)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __232rock_col():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1100)
        ProjectileDurabilityLvl(1)
        Unknown11034(1)
        AttackAttributes(0, 1, 0, 0, 0)
        Hitstop(0)
        AttackP1(90)
        AttackP2(79)
        BonusProrationPct(110)
        hitstun(22)
        AirUntechableTime(50)
        Unknown11001(12, 0, 5)
        GroundedHitstunAnimation(9)
        AirPushbackX(8800)
        AirPushbackY(43000)
        IsInvisibility(1)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpluseBeforeWallbounce(20)
            Unknown9346(1)
            Wallbounce(1)
            Wallstick(1)
            WallstickLength(30)
            if (SLOT_4 > 1):
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                GroundedHitstunAnimation(17)
                AirHitstunAnimation(17)
                Unknown1017()
        FireBall(1, 1, 1, 0, 1, 0, 1, 1)

        def upon_54():
            sendToLabel(580)
        Unknown2037(0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown21012('NmlAtk2C', 32)
    sprite('null', 5)
    sprite('vr_azef232_00col', 4)
    sprite('vr_azef232_01col', 2)
    label(580)
    sprite('null', 2)

@State
def __255swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3001(0)
        GFX_OffsetY(230000)
    sprite('null', 3)
    sprite('null', 3)
    Unknown3001(255)
    Unknown4003('azef_255swing00.DIG', '')
    Unknown4015()

@State
def __400impact():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('azef_400impact00.DIG', '')
        Unknown4015()
        GFX_OffsetY(280000)
        GFX_OffsetX(200000)
        Unknown3001(255)
        GFX_Scale(1700)
    sprite('null', 10)
    GFX_1('azef_400impact_pos', -1)
    GFX_0('400yugami', -1)
    sprite('null', 5)

@State
def __400yugami():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        GFX_Scale(1200)
        GFX_OffsetX(30000)
        GFX_OffsetY(15000)
    sprite('vr_azef400_yugami', 15)
    Unknown3057(1)
    Unknown3058(50000)
    Unknown3059(-3000)

@State
def __401swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('azef_401impact00.DIG', '')
        Unknown4015()
        GFX_Scale(1700)
        Unknown3001(200)
    sprite('null', 10)
    sprite('null', 5)

@State
def azef_guardcrash():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('azef_401guardcrash00.DIG', '')
        Unknown4015()
        GFX_Scale(1700)
        Unknown3001(200)
        Unknown3007(0)
    sprite('null', 10)
    sprite('null', 5)

@State
def azef_guardcrash_hold():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)
    GFX_1('azef_guardcrash_hold', -1)
    gotoLabel(0)

@State
def azef_dustattack_hold():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)
    GFX_1('azef_dustattack_hold', -1)
    gotoLabel(0)

@State
def __402rock1():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('azef_402rock.DIG', '')
        GFX_Scale(1500)
        GFX_OffsetX(-20000)
        GFX_OffsetY(15000)
    sprite('null', 5)
    sprite('null', 10)
    GFX_1('azef_402rocksmoke_pos', -1)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __402swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('azef_402swing.DIG', '')
        Unknown4015()
        GFX_Scale(1000)
        Unknown3001(255)
        GFX_OffsetY(300000)
        GFX_OffsetX(100000)
    sprite('null', 14)

@State
def __403swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('azef_403swing.DIG', '')
        Unknown4015()
        GFX_Scale(700)
        Unknown3001(255)
    sprite('null', 14)
    GFX_1('azef_403backadd_00', -1)
    GFX_0('403yugami', -1)

@State
def __403yugami():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        GFX_OffsetY(230000)
        GFX_OffsetX(55000)
    sprite('vr_azef403_yugami', 15)
    Unknown3057(1)
    Unknown3058(40000)
    Unknown3059(-2500)

@State
def __404tame():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('azef_404tame_addcircle')
        GFX_OffsetY(250000)
        GFX_OffsetX(-50000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __404swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('azef_404swing.DIG', '')
        GFX_OffsetY(250000)
        GFX_OffsetX(250000)
        Unknown3001(0)
    sprite('null', 1)
    sprite('null', 1)
    Unknown3001(255)
    GFX_1('azef_blood_01', -1)
    sprite('null', 1)
    sprite('null', 1)
    GFX_1('azef_blood_01', -1)
    sprite('null', 1)
    sprite('null', 8)
    GFX_1('azef_blood_01', -1)

@State
def __404nigiyakasi():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        GFX_OffsetY(250000)
        GFX_OffsetX(250000)
    sprite('null', 5)
    GFX_2('azef_404impact_thunder')
    sprite('null', 10)
    Unknown3004(-26)

@State
def __405smoke():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
    GFX_1('azef_405tossin_smoke', -1)
    label(0)
    sprite('null', 1)
    GFX_1('azef_405tossin', -1)
    gotoLabel(0)

@State
def __405rock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('azef_405rock00.DIG', '')
        GFX_Scale(1125)
        GFX_OffsetX(-15000)
        GFX_OffsetY(15000)
    sprite('null', 5)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __405punch():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        Unknown3001(255)
        GFX_Scale(800)
    sprite('null', 15)
    Unknown4003('azef_405punch00.DIG', '')
    Unknown4015()

@State
def __405yugami():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
        Unknown4010(2)
        GFX_OffsetY(248000)
        GFX_OffsetX(-64000)
        GFX_Scale(1200)
    sprite('vr_azef405_yugami', 15)
    Unknown3057(1)
    Unknown3058(35000)
    Unknown3059(-2500)

@State
def __032rock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('azef_405rock00.DIG', '')
        GFX_Scale(625)
        GFX_OffsetX(-20000)
        GFX_OffsetY(15000)
    sprite('null', 5)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3004(-51)

@State
def azef_rlah_circle():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 30)
    Unknown3001(0)
    sprite('null', 32767)
    GFX_2('rlef_ah_az_circle')
    Unknown3004(16)

@State
def __407aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        IsInvisibility(1)
        Unknown4003('azef_aura00', '')
        Unknown4015()
    label(1)
    sprite('vr_azef407_efpos00', 1)
    GFX_0('407yugami', -1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 0)
    Unknown4054(12)
    PFX('azef_407backaura_02', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 2)
    Unknown4054(12)
    PFX('azef_407backaura_02', 3)
    Unknown4054(12)
    PFX('azef_407backaura_02', 4)
    Unknown4054(12)
    PFX('azef_407backaura_02', 5)
    GFX_0('407boya2', 2)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 3)
    Unknown4054(12)
    PFX('azef_407backaura_02', 4)
    Unknown4054(12)
    PFX('azef_407backaura_02', 5)
    GFX_0('407boya2', 5)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 6)
    Unknown4054(12)
    PFX('azef_407backaura_02', 7)
    Unknown4054(12)
    PFX('azef_407backaura_02', 8)
    GFX_0('407boya2', 8)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 9)
    Unknown4054(12)
    PFX('azef_407backaura_02', 10)
    Unknown4054(12)
    PFX('azef_407backaura_02', 11)
    GFX_0('407boya2', 11)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 12)
    Unknown4054(12)
    PFX('azef_407backaura_02', 13)
    GFX_0('407boya2', 13)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 14)
    Unknown4054(12)
    PFX('azef_407backaura_02', 15)
    GFX_0('407boya2', 15)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 16)
    Unknown4054(12)
    PFX('azef_407backaura_02', 17)
    GFX_0('407boya2', 17)
    sprite('vr_azef407_efpos00', 5)
    Unknown4054(12)
    PFX('azef_407backaura_02', 18)
    Unknown4054(12)
    PFX('azef_407backaura_02', 19)
    GFX_0('407boya2', 19)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 0)
    Unknown4054(12)
    PFX('azef_407backaura_02', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 2)
    Unknown4054(12)
    PFX('azef_407backaura_02', 3)
    Unknown4054(12)
    PFX('azef_407backaura_02', 4)
    Unknown4054(12)
    PFX('azef_407backaura_02', 5)
    GFX_0('407boya', 1)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 3)
    Unknown4054(12)
    PFX('azef_407backaura_02', 4)
    Unknown4054(12)
    PFX('azef_407backaura_02', 5)
    GFX_0('407boya', 2)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 6)
    Unknown4054(12)
    PFX('azef_407backaura_02', 7)
    Unknown4054(12)
    PFX('azef_407backaura_02', 8)
    GFX_0('407boya', 7)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 9)
    Unknown4054(12)
    PFX('azef_407backaura_02', 10)
    Unknown4054(12)
    PFX('azef_407backaura_02', 11)
    GFX_0('407boya', 8)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 12)
    Unknown4054(12)
    PFX('azef_407backaura_02', 13)
    GFX_0('407boya', 11)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 14)
    Unknown4054(12)
    PFX('azef_407backaura_02', 15)
    GFX_0('407boya', 14)
    sprite('vr_azef407_efpos00', 1)
    Unknown4054(12)
    PFX('azef_407backaura_02', 16)
    Unknown4054(12)
    PFX('azef_407backaura_02', 17)
    GFX_0('407boya', 16)
    sprite('vr_azef407_efpos00', 5)
    Unknown4054(12)
    PFX('azef_407backaura_02', 18)
    Unknown4054(12)
    PFX('azef_407backaura_02', 19)
    GFX_0('407boya', 18)
    gotoLabel(1)
    label(0)
    sprite('vr_azef407_efpos00', 5)
    Unknown3004(-51)

@State
def __407boya():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        GFX_Scale(500)
        Unknown4003('azef_aura01', '')
        Unknown4015()
        Unknown4010(2)
        Unknown23015(11)
        Unknown3001(0)
    sprite('null', 19)
    Unknown3004(26)
    Unknown1067(20)
    Unknown1070(-300, 500)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __407boya2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        GFX_Scale(500)
        Unknown4003('azef_aura01', '')
        Unknown4015()
        Unknown4010(2)
        Unknown23015(11)
        Unknown2005()
        Unknown3001(0)
    sprite('null', 19)
    Unknown3004(26)
    Unknown1067(20)
    Unknown1070(-300, 500)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __407yugami():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        GFX_OffsetY(180000)
        GFX_OffsetX(40000)
    sprite('vr_azef407_yugami', 60)
    Unknown1099(10)
    physicsYImpulse(-2000)
    Unknown3004(-9)
    Unknown3057(1)
    Unknown3058(10000)
    Unknown3059(-1500)

@State
def __407Kyushu():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        GFX_OffsetY(250000)
        GFX_OffsetX(140000)
        GFX_Scale(1300)
    sprite('null', 25)
    GFX_2('azef_407kyushu_tubusub')
    SFX_0('022_magiccircle_b')

@State
def __407Mutekicol():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(3)
        IsInvisibility(1)
        setInvincible(1)
        Unknown22006(1)
        Unknown22032(1)
        Unknown22022(0)
        Unknown22036(0)
        GuardPoint_(1)

        def upon_42():
            Unknown21007(3, 32)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(42)
            setInvincible(0)
            sendToLabel(0)
    sprite('az407_03ex', 32767)
    label(0)
    sprite('null', 3)

@State
def azef_409_fall():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        GFX_2('azef_409punch')
    label(0)
    sprite('null', 2)
    GFX_1('azef_409punch_add', -1)
    gotoLabel(0)

@State
def azef_409_rock():

    def upon_IMMEDIATE():
        Unknown4003('azef_406jiware.DIG', '')
        Unknown3032()
        GFX_Scale(1750)
        Unknown1006(50000)
        GFX_OffsetX(100000)
    sprite('null', 5)
    GFX_0('azef_409_hibiware', -1)
    PFX_Scale(845)
    PFX('azef_406_stone', -1)
    sprite('null', 20)
    Unknown3004(-10)

@State
def azef_409_hibiware():

    def upon_IMMEDIATE():
        Unknown4003('azef_hibiware.DIG', '')
        Unknown3032()
        GFX_Scale(1500)
        Unknown1006(100000)
        Unknown23015(2)
    sprite('null', 4)
    sprite('null', 8)
    Unknown3004(-26)

@State
def weakhit00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1086(22)
        Unknown4010(2)
        GFX_OffsetY(150000)
        GFX_Scale(2400)
        Unknown23015(4)
        Unknown2007()
    sprite('null', 30)
    GFX_2('azef_weakhit_red')

@State
def weakhit01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1086(22)
        Unknown4010(2)
        GFX_OffsetY(150000)
        GFX_Scale(2400)
        Unknown23015(4)
        Unknown2007()
    sprite('null', 30)
    GFX_2('azef_weakhit_yellow')

@State
def weakpoint01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(255)
        GFX_Scale(2300)
        GFX_SetPalette(1)
        Unknown21004(16)
        Unknown4003('azef_weakpoint00.DIG', '')
        Unknown4015()

        def upon_16():
            Unknown2071(22, 0, 60000, 100, 1)
        Unknown4025(22)
        sendToLabelUpon(32, 0)
    sprite('null', 20)
    GFX_0('weakstart01', -1)
    Unknown1099(-27)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown1099(300)

@State
def weakpoint00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(255)
        GFX_Rotation(180000)
        GFX_Scale(2300)
        GFX_SetPalette(1)
        Unknown21004(17)
        Unknown4003('azef_weakpoint00.DIG', '')
        Unknown4015()

        def upon_16():
            Unknown2071(22, 0, -80000, 100, 1)
        Unknown4025(22)
        sendToLabelUpon(32, 0)
    sprite('null', 20)
    GFX_0('weakstart00', -1)
    Unknown1099(-25)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 10)
    Unknown3004(-27)
    Unknown1099(300)

@State
def weakstart00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
    sendToLabelUpon(32, 0)
sprite('null', 5)
sprite('null', 30)
GFX_2('azef_weakhit_02')
endState()

@State
def weakstart01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
    sendToLabelUpon(32, 0)
sprite('null', 5)
sprite('null', 30)
GFX_2('azef_weakhit_03')
endState()

@State
def __408sphere():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_OffsetY(230000)
        GFX_OffsetX(20000)
        Unknown4003('azef_408tama', '')
        Unknown4015()
        Unknown3001(0)
        Unknown2010()
        AttackLevel_(3)
        AttackP1(80)
        ProjectileDurabilityLvl(2)
        Damage(1400)
        AirUntechableTime(30)
        AirPushbackX(54000)
        AirPushbackY(18000)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        StarterRating(2)
        PunchFX(1)
        Hitstop(3)
        sendToLabelUpon(10, 580)
        ProjectileDisapperOnHit(3)
        IsInvisibility(1)
        GFX_2('azef_408_ambient00')
        SameMoveProration(1)

        def upon_32():
            AttackLevel_(3)
            ProjectileDurabilityLvl(2)
            Damage(1000)
            AirUntechableTime(40)
            AirPushbackX(54000)
            AirPushbackY(18000)
            GroundedHitstunAnimation(19)
            AirHitstunAnimation(19)
            Wallbounce(1)
            WallbounceReboundTime(1)

        def upon_33():
            Unknown2037(1)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpluseBeforeWallbounce(20)
            Unknown9346(1)
            Wallbounce(1)
            Wallstick(1)
            WallstickLength(30)
            if (SLOT_4 > 1):
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                GroundedHitstunAnimation(17)
                AirHitstunAnimation(17)
                Unknown1017()
    label(0)
    sprite('vr_azef408_col', 1)
    StartMultihit()
    GFX_OffsetX(60000)
    sprite('vr_azef408_col', 1)
    if SLOT_2:
        GuardPoint_(1)
        defineInvincibility(0, 0, 0, 1, 0)
        Unknown22032(1)
        Unknown23142(1)
    sprite('vr_azef408_col', 7)
    Unknown22006(0)
    sprite('vr_azef408_col', 1)
    GFX_0('408JizokuSmoke', -1)
    Unknown3004(51)
    RefreshMultihit()
    sprite('vr_azef408_col', 3)
    physicsXImpulse(80000)
    gotoLabel(9)
    label(9)
    sprite('vr_azef408_col', 4)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    sprite('vr_azef408_col', 4)
    GFX_0('408sphereJizoku', -1)
    RefreshMultihit()
    label(580)
    sprite('vr_azef408_col', 5)
    GFX_Unload('408JizokuSmoke')
    physicsXImpulse(0)
    GFX_1('azef_408_brake_tubu', -1)
    sprite('vr_azef408_col', 5)
    Unknown3004(-51)

@State
def __408sphereStart():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        GFX_OffsetY(230000)
        GFX_OffsetX(130000)
    sprite('null', 5)
    GFX_1('azef_407kyushu_tubusub', -1)
    sprite('null', 8)
    GFX_2('azef_408_sub')
    Unknown1099(30)
    physicsXImpulse(1500)

@State
def __408JizokuSmoke():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 2)
    GFX_1('azef_408_jizokuaura_tubu', -1)
    gotoLabel(0)

@State
def __408sphereJizoku():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('azef_408tama2', '')
        Unknown4015()
        Unknown1077(-5000, 5000)
        Unknown1011(-15000, 15000)
        Unknown1102(0, 2500)
        Unknown1064(1500)
        Unknown1056(2000)
        Unknown3001(255)
    sprite('null', 7)
    Unknown1067(-30)
    Unknown3004(-37)

@State
def __430Cam():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
    sprite('null', 5)
    CameraControlEnable(1)
    Unknown20003(1)
    physicsXImpulse(14800)
    sprite('null', 30)
    physicsXImpulse(0)
    sprite('null', 20)
    physicsXImpulse(-3700)

@State
def __430HandAura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown23015(2)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 0)
    GFX_1('azef_408handaura_add', 1)
    GFX_0('430Hand01', 0)
    GFX_0('430Hand01', 1)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 2)
    GFX_1('azef_408handaura_add', 3)
    GFX_0('430Hand01', 2)
    GFX_0('430Hand01', 3)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 4)
    GFX_1('azef_408handaura_add', 5)
    GFX_0('430Hand01', 4)
    GFX_0('430Hand01', 5)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 6)
    GFX_1('azef_408handaura_add', 7)
    GFX_0('430Hand01', 6)
    GFX_0('430Hand01', 7)
    sprite('vr_azef430_efpos00', 2)
    GFX_1('azef_408handaura_add', 8)
    GFX_1('azef_408handaura_add', 9)
    GFX_0('430Hand01', 8)
    GFX_0('430Hand01', 9)
    sprite('vr_azef430_efpos00', 2)
    GFX_1('azef_408handaura_add', 10)
    GFX_1('azef_408handaura_add', 11)
    GFX_0('430Hand01', 10)
    GFX_0('430Hand01', 11)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 12)
    GFX_1('azef_408handaura_add', 13)
    GFX_0('430Hand01', 12)
    GFX_0('430Hand01', 13)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 14)
    GFX_1('azef_408handaura_add', 15)
    GFX_0('430Hand01', 14)
    GFX_0('430Hand01', 15)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 16)
    GFX_1('azef_408handaura_add', 17)
    GFX_0('430Hand01', 16)
    GFX_0('430Hand01', 17)
    sprite('vr_azef430_efpos00', 3)
    GFX_1('azef_408handaura_add', 18)
    GFX_1('azef_408handaura_add', 19)
    GFX_0('430Hand01', 18)
    GFX_0('430Hand01', 19)
    sprite('vr_azef430_efpos00', 6)
    GFX_1('azef_408handaura_add', 20)
    GFX_1('azef_408handaura_add', 21)
    sprite('vr_azef430_efpos00', 6)
    GFX_1('azef_408handaura_add', 22)
    GFX_1('azef_408handaura_add', 23)
    sprite('vr_azef430_efpos00', 6)
    GFX_1('azef_408handaura_add', 24)
    sprite('vr_azef430_efpos00', 7)
    GFX_1('azef_408handaura_add', 25)
    GFX_1('azef_408handaura_add', 26)
    sprite('vr_azef430_efpos00', 6)
    GFX_1('azef_408handaura_add', 27)
    GFX_1('azef_408handaura_add', 28)

@State
def __430BodyAura():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(2)
    sprite('vr_azef430_efpos01', 3)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    Unknown4054(12)
    PFX('azef_408handaura_add', 106)
    sprite('vr_azef430_efpos01', 3)
    GFX_0('430Hand02', 0)
    GFX_0('430Hand02', 1)
    GFX_0('430Hand02', 2)
    GFX_0('430Hand02', 3)
    GFX_0('430Hand02', 4)
    GFX_0('430Hand02', 5)
    GFX_0('430Hand02', 6)
    GFX_0('430Hand02', 7)

@State
def __430Hand01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        GFX_Scale(400)
        Unknown4003('azef_aura01', '')
        Unknown4015()
    sprite('null', 19)
    Unknown1099(10)
    Unknown1077(-45000, 45000)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __430Hand02():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        GFX_Scale(400)
        Unknown4003('azef_aura01', '')
        Unknown4015()
        Unknown3001(0)
    sprite('null', 5)
    sprite('null', 14)
    Unknown3004(26)
    Unknown1099(10)
    Unknown1077(-45000, 45000)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __430aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        IsInvisibility(1)
        sendToLabelUpon(32, 0)
    label(1)
    sprite('vr_azef430_efpos02', 2)
    Unknown4054(2)
    PFX('azef_407backaura_02', 0)
    Unknown4054(2)
    PFX('azef_407backaura_02', 1)
    Unknown4054(2)
    PFX('azef_407backaura_02', 2)
    GFX_0('407boya', 0)
    GFX_0('430boya', 1)
    GFX_0('407boya', 2)
    sprite('vr_azef430_efpos02', 2)
    Unknown4054(2)
    PFX('azef_407backaura_02', 3)
    Unknown4054(2)
    PFX('azef_407backaura_02', 4)
    Unknown4054(2)
    PFX('azef_407backaura_02', 5)
    GFX_0('407boya', 3)
    GFX_0('430boya', 4)
    GFX_0('407boya', 5)
    sprite('vr_azef430_efpos02', 2)
    Unknown4054(2)
    PFX('azef_407backaura_02', 6)
    Unknown4054(2)
    PFX('azef_407backaura_02', 7)
    Unknown4054(2)
    PFX('azef_407backaura_02', 8)
    GFX_0('430boya', 6)
    GFX_0('407boya', 7)
    GFX_0('407boya2', 8)
    sprite('vr_azef430_efpos02', 3)
    Unknown4054(2)
    PFX('azef_407backaura_02', 9)
    Unknown4054(2)
    PFX('azef_407backaura_02', 10)
    Unknown4054(2)
    PFX('azef_407backaura_02', 11)
    GFX_0('407boya', 9)
    GFX_0('430boya', 10)
    GFX_0('407boya', 11)
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 1)
    Unknown3004(-51)

@State
def __430boya():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        GFX_Scale(500)
        Unknown4003('azef_aura01', '')
        Unknown4015()
        Unknown4010(2)
        Unknown23015(12)
        Unknown3001(0)
    sprite('null', 19)
    Unknown3004(26)
    Unknown1067(20)
    Unknown1070(500, 1000)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __430Atk():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('azef_430shock01', '')
        GFX_OffsetY(200000)
        GFX_OffsetX(200000)
        GFX_Scale(300)
    sprite('null', 5)
    ScreenShake(6000, 6000)
    Unknown1099(50)
    sprite('null', 5)
    ScreenShake(6000, 6000)
    sprite('null', 4)
    ScreenShake(6000, 6000)
    Unknown1099(5)
    sprite('null', 4)
    ScreenShake(6000, 6000)
    sprite('null', 5)
    ScreenShake(6000, 6000)
    Unknown3004(-51)
    Unknown1099(-90)

@State
def __430shock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('azef_430shock00', '')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        GFX_OffsetY(200000)
        GFX_OffsetX(200000)
        Unknown23015(2)
    sprite('null', 5)
    ScreenShake(3000, 3000)
    GFX_0('430shock01', -1)
    GFX_0('430Speed', -1)
    sprite('null', 5)
    Unknown3004(-26)
    sprite('null', 10)
    Unknown21012('430Speed', 32)
    sprite('null', 15)

@State
def __430shock01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown23015(2)
    sprite('null', 45)
    GFX_2('azef_408_tukihit_add2')

@State
def __430Speed():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(2)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    GFX_2('azef_408_speedline_down')
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __431ODAura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        IsInvisibility(1)
        sendToLabelUpon(32, 0)
        Unknown4003('azef_431aura.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(0)
        GFX_Scale(950)
    sprite('null', 10)
    GFX_0('431Odaura', -1)
    Unknown3004(17)
    label(1)
    sprite('vr_azef610_efpos00', 2)
    Unknown3004(0)
    PFX('azef_407backaura_02', 0)
    PFX('azef_407backaura_02', 1)
    PFX('azef_407backaura_02', 2)
    PFX('azef_407backaura_02', 3)
    PFX('azef_407backaura_02', 4)
    PFX('azef_407backaura_02', 5)
    sprite('vr_azef610_efpos00', 2)
    PFX('azef_407backaura_02', 6)
    PFX('azef_407backaura_02', 7)
    PFX('azef_407backaura_02', 8)
    PFX('azef_407backaura_02', 9)
    PFX('azef_407backaura_02', 10)
    sprite('vr_azef610_efpos00', 2)
    PFX('azef_407backaura_02', 11)
    PFX('azef_407backaura_02', 13)
    PFX('azef_407backaura_02', 14)
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 10)
    Unknown21012('431Odaura', 32)
    Unknown3004(-51)

@State
def __431Odaura():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4007(2)
        Unknown4010(2)
        GFX_SetPalette(1)
        Unknown3001(170)
        sendToLabelUpon(32, 0)
        Unknown2019(100)
    sprite('null', 5)
    label(1)
    sprite('vr_azef431_00', 3)
    sprite('vr_azef431_01', 3)
    sprite('vr_azef431_02', 3)
    gotoLabel(1)
    label(0)
    sprite('vr_azef431_00', 3)
    Unknown3004(-26)
    sprite('vr_azef431_01', 3)
    sprite('vr_azef431_02', 3)

@State
def __431swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('azef_431swing00', '')
        GFX_OffsetY(160000)
        GFX_OffsetX(350000)
        GFX_Scale(2000)
    sprite('null', 10)
    GFX_0('431yugami', -1)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __431yugami():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
    sprite('vr_azef431_yugami', 15)
    Unknown1099(10)
    physicsYImpulse(-2000)
    Unknown3004(-9)
    Unknown3057(1)
    Unknown3058(30000)
    Unknown3059(-1500)

@State
def __450neppaMatome():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        GFX_OffsetX(150000)
    sprite('null', 1)
    GFX_0('450neppa00', -1)
    GFX_1('azef_450neppa_circle', -1)
    sprite('null', 7)
    GFX_0('450neppa01', -1)
    sprite('null', 7)
    GFX_0('450neppa01', -1)
    sprite('null', 7)

@State
def __450neppa00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('azef_450neppa00', '')
        Unknown4010(2)
    sprite('null', 20)
    sprite('null', 7)
    Unknown3004(-51)

@State
def __450neppa01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('azef_450neppa00', '')
        Unknown4010(2)
    sprite('null', 7)
    sprite('null', 7)
    Unknown3004(-51)
endState()

@State
def nepparock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown2054(1)
        GFX_Scale(2000)
        GFX_OffsetX(160000)
        Unknown4003('azef_406jiware.DIG', '')
    sprite('null', 10)
    GFX_1('azef_406_stone', -1)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __450swing():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4010(2)
        Unknown4003('azef_400impact00.DIG', '')
        Unknown4015()
        GFX_OffsetX(30000)
        Unknown3001(255)
        Unknown1064(3200)
        Unknown1056(2400)
        Unknown2005()
        Unknown1073(100000)
    sprite('null', 10)

@State
def __450rock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('azef_rock', '')
        GFX_OffsetX(280000)
    sprite('null', 6)
    GFX_0('450smoke', -1)
    Unknown36(22)
    GFX_OffsetY(15000)
    setGravity(0)
    Unknown35()
    Unknown1073(3250)
    GFX_OffsetY(70000)
    sprite('null', 50)
    Unknown1073(1625)
    GFX_OffsetY(35000)
    Unknown36(22)
    GFX_OffsetY(30000)
    Unknown35()
    sprite('null', 40)
    Unknown1073(812)
    GFX_OffsetY(40000)
    Unknown36(22)
    GFX_OffsetY(30000)
    Unknown35()
    sprite('null', 40)
    Unknown1073(406)
    GFX_OffsetY(20000)
    Unknown36(22)
    GFX_OffsetY(15000)
    Unknown35()
    sprite('null', 60)
    Unknown36(22)
    GFX_OffsetY(15000)
    Unknown35()
    Unknown1073(203)
    GFX_OffsetY(10000)
    sprite('null', 20)
    GFX_0('AHsection', -1)
    physicsYImpulse(60000)
    Unknown36(22)
    GFX_OffsetY(15000)
    physicsYImpulse(100000)
    Unknown23015(2)
    Unknown35()

@State
def __450smoke():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown23015(4)
        GFX_OffsetY(4294937296)
        GFX_OffsetX(-20000)
    sprite('null', 6)
    GFX_0('450smokeb', -1)
    Unknown4054(4)
    PFX('azef_450stonesmoke_brust', -1)
    sprite('null', 50)
    Unknown4054(4)
    PFX('azef_450stonesmoke_stone2', -1)
    sprite('null', 40)
    Unknown4054(4)
    PFX('azef_450stonesmoke_stone2', -1)
    sprite('null', 40)
    Unknown4054(4)
    PFX('azef_450stonesmoke_stone2', -1)
    sprite('null', 60)
    Unknown4054(4)
    PFX('azef_450stonesmoke_stone2', -1)

@State
def __450smokeb():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown23015(2)
        GFX_OffsetY(4294937296)
        GFX_OffsetX(-20000)
    sprite('null', 6)
    Unknown4054(2)
    PFX('azef_450stonesmoke_bbrust', -1)
    sprite('null', 50)
    Unknown4054(2)
    PFX('azef_450stonesmoke_b', -1)
    sprite('null', 40)
    Unknown4054(2)
    PFX('azef_450stonesmoke_b', -1)
    sprite('null', 40)
    Unknown4054(2)
    PFX('azef_450stonesmoke_b', -1)
    sprite('null', 60)
    Unknown4054(2)
    PFX('azef_450stonesmoke_b', -1)

@State
def __450smokec():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown23015(2)
        GFX_OffsetY(4294867296)
        GFX_OffsetX(300000)
        GFX_Scale(1500)
        GFX_2('azef_utiagesmoke_02')
    sprite('null', 50)

@State
def IrezumiRay():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4007(2)
        GFX_SetPalette(1)
        Unknown3001(0)
        GFX_OffsetY(7000)
    sprite('vr_azef450_00', 20)
    Unknown3004(26)
    GFX_0('IrezumiRayLine', -1)
    sprite('vr_azef450_00', 30)
    Unknown3004(-26)

@State
def IrezumiRayLine():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4007(2)
        GFX_SetPalette(1)
        Unknown3001(0)
    sprite('vr_azef450_01', 20)
    Unknown3004(26)
    sprite('vr_azef450_01', 20)
    Unknown3004(-13)

@State
def az450_dummy():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown11064(3)
        AttackLevel_(5)
        Damage(32000)
        MinimumDamagePct(100)
        Unknown11056(3)
        Unknown11071(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(10000)
        Unknown11023(1)
        Unknown1086(22)
        IsInvisibility(1)
        GFX_Scale(3000)
sprite('null', 7)
sprite('vr_azef450_col', 10)
Unknown11023(1)
sprite('az450cutin_01', 3000)
endState()

@State
def __450Cam():

    def upon_IMMEDIATE():
        Unknown3032()
        CameraControlEnable(1)
        GFX_OffsetY(300000)
    sprite('null', 6)
    Unknown20009(990)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(980)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(970)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(960)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(950)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(940)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(930)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(920)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(910)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(900)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(890)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(880)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(870)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(860)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(850)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(840)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(830)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(820)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(810)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(800)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(790)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(780)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(770)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    Unknown20009(760)
    ScreenShake(4000, 4000)
    sprite('null', 6)
    sprite('null', 6)
    sprite('null', 4)
    Unknown20009(100)
    GFX_1('azef_ahanten05', -1)
    ScreenShake(1275, 1275)
    sprite('null', 11)
    Unknown20009(1000)
    GFX_OffsetY(4294167296)
    CameraControlEnable(0)

@State
def AHshadow():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        GFX_2('azef_ahshadow_00')
        GFX_OffsetY(300000)
    sprite('null', 165)

@State
def AHanten00():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        GFX_2('azef_ahanten01')
        Unknown23032(50)
    sprite('null', 90)

@State
def AHanten01():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        GFX_2('azef_ahanten04')
    sprite('null', 90)

@State
def AHanten02():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        GFX_2('azef_lastanten01')
        GFX_OffsetY(300000)
        Unknown23032(50)
    sprite('null', 90)

@State
def AHsection():

    def upon_IMMEDIATE():
        Unknown4003('azef_section', '')
        Unknown4015()
    sprite('null', 60)

@State
def AHSmoke():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        GFX_2('azef_ahfinishbg03')
    sprite('null', 32767)

@State
def AHaura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        IsInvisibility(1)
        sendToLabelUpon(32, 0)
        Unknown4003('azef_aura02', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(200)
    label(1)
    sprite('vr_azef610_efpos00', 2)
    PFX('azef_407backaura_02', 0)
    PFX('azef_407backaura_02', 1)
    PFX('azef_407backaura_02', 2)
    PFX('azef_407backaura_02', 3)
    PFX('azef_407backaura_02', 4)
    PFX('azef_407backaura_02', 5)
    sprite('vr_azef610_efpos00', 2)
    PFX('azef_407backaura_02', 6)
    PFX('azef_407backaura_02', 7)
    PFX('azef_407backaura_02', 8)
    PFX('azef_407backaura_02', 9)
    PFX('azef_407backaura_02', 10)
    sprite('vr_azef610_efpos00', 2)
    PFX('azef_407backaura_02', 11)
    PFX('azef_407backaura_02', 13)
    PFX('azef_407backaura_02', 14)
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 1)
    Unknown3004(-51)

@State
def __610aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        IsInvisibility(1)
        sendToLabelUpon(32, 0)
        Unknown4003('azef_610aura00', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(200)
    label(1)
    sprite('vr_azef610_efpos00', 2)
    PFX('azef_407backaura_02', 0)
    PFX('azef_407backaura_02', 1)
    PFX('azef_407backaura_02', 2)
    PFX('azef_407backaura_02', 3)
    PFX('azef_407backaura_02', 4)
    PFX('azef_407backaura_02', 5)
    GFX_0('407boya', 1)
    GFX_0('407boya', 5)
    sprite('vr_azef610_efpos00', 2)
    PFX('azef_407backaura_02', 6)
    PFX('azef_407backaura_02', 7)
    PFX('azef_407backaura_02', 8)
    PFX('azef_407backaura_02', 9)
    PFX('azef_407backaura_02', 10)
    GFX_0('407boya2', 6)
    GFX_0('407boya2', 9)
    GFX_0('407boya2', 10)
    sprite('vr_azef610_efpos00', 2)
    PFX('azef_407backaura_02', 11)
    PFX('azef_407backaura_02', 13)
    PFX('azef_407backaura_02', 14)
    GFX_0('407boya2', 11)
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 1)
    Unknown3004(-51)

@State
def dashEff():

    def upon_IMMEDIATE():
        Unknown4008(2)
        Unknown2054(1)
        GFX_2('azef_newdash2')
    sprite('null', 50)

@State
def dashEff2():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown2054(1)
        GFX_2('azef_newdash3')
    sprite('null', 50)

@State
def BrustDD_SlashEff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown2005()
        Unknown1056(900)
        Unknown1064(1100)
        Unknown3001(255)
        GFX_OffsetY(100000)
        GFX_OffsetX(-100000)
        Unknown3032()
    sprite('vr_azef440_00', 4)
    sprite('vr_azef440_01', 4)
    sprite('vr_azef440_02', 4)
    sprite('vr_azef440_03', 5)
    Unknown3004(-51)

@State
def BrustDD_SlashEffEx():

    def upon_IMMEDIATE():
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown2005()
        Unknown1056(1300)
        Unknown1064(1560)
        Unknown3001(255)
        GFX_OffsetY(10000)
        GFX_OffsetX(-100000)
        Unknown3032()
    sprite('vr_azef440_00', 4)
    GFX_0('BrustDD_EXeff', -1)
    Unknown36(1)
    Unknown1073(-10000)
    GFX_OffsetX(-125000)
    Unknown1097(500)
    Unknown35()
    GFX_0('BrustDD_EXeff', -1)
    Unknown36(1)
    Unknown1073(-45000)
    GFX_OffsetX(-125000)
    Unknown35()
    GFX_0('BrustDD_EXeff', -1)
    Unknown36(1)
    Unknown1073(-90000)
    GFX_OffsetX(-125000)
    Unknown35()
    sprite('vr_azef440_01', 4)
    sprite('vr_azef440_02', 4)
    sprite('vr_azef440_03', 5)
    Unknown3004(-51)

@State
def BrustDD_SlashEff2():

    def upon_IMMEDIATE():
        GFX_SetPalette(1)
        Unknown3032()
        Unknown2005()
        GFX_OffsetY(250000)
        GFX_OffsetX(-180000)
        Unknown4007(2)
        EnableAfterimage(1)
        Unknown21010(1)
    sprite('vr_azef440_10', 6)
    GFX_Scale(1200)
    sprite('vr_azef440_11', 5)
    GFX_Scale(1400)
    Unknown21010(0)
    sprite('vr_azef440_12', 12)
    GFX_Scale(1500)
    Unknown1099(20)
    sprite('vr_azef440_13', 4)
    GFX_1('azef_440brust_00', -1)
    sprite('vr_azef440_14', 4)
    Unknown3004(-51)

@State
def BrustDD_SlashEff2Ex():

    def upon_IMMEDIATE():
        GFX_SetPalette(1)
        Unknown3032()
        Unknown2005()
        GFX_OffsetY(250000)
        GFX_OffsetX(-180000)
        Unknown4007(2)
        EnableAfterimage(1)
        Unknown21010(1)
    sprite('vr_azef440_10', 6)
    GFX_Scale(1400)
    sprite('vr_azef440_11', 5)
    GFX_Scale(1700)
    Unknown21010(0)
    sprite('vr_azef440_12', 12)
    GFX_Scale(1800)
    Unknown1099(40)
    GFX_0('BrustDD_EXeff', -1)
    Unknown36(1)
    Unknown1073(450000)
    Unknown1097(250)
    Unknown23015(6)
    Unknown35()
    GFX_0('BrustDD_EXeff', -1)
    Unknown36(1)
    Unknown1073(-450000)
    Unknown1097(500)
    Unknown23015(6)
    Unknown35()
    GFX_0('BrustDD_EXeff', -1)
    Unknown36(1)
    Unknown1073(1800000)
    Unknown1097(500)
    Unknown23015(6)
    Unknown35()
    sprite('vr_azef440_13', 4)
    GFX_1('azef_440brust_01', -1)
    sprite('vr_azef440_14', 4)
    Unknown3004(-51)

@State
def BrustDD_SlashEff3():

    def upon_IMMEDIATE():
        GFX_SetPalette(1)
        Unknown3032()
        Unknown2005()
        GFX_OffsetY(290000)
        Unknown4007(2)
        Unknown21010(1)
        GFX_Scale(1700)
    sprite('vr_azef440_20', 2)
    GFX_0('BrustDD_brust', -1)
    Unknown23015(11)
    sprite('vr_azef440_21', 2)
    sprite('vr_azef440_22', 2)
    GFX_OffsetX(35000)
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(20000)
    Unknown35()
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(150000)
    Unknown35()
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(-45000)
    Unknown23015(11)
    Unknown35()
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(-140000)
    Unknown23015(11)
    Unknown35()
    sprite('vr_azef440_22', 4)
    GFX_OffsetX(35000)
    sprite('vr_azef440_23', 4)
    GFX_OffsetX(35000)
    Unknown21010(0)
    sprite('vr_azef440_24', 4)
    GFX_OffsetX(35000)
    sprite('vr_azef440_25', 4)
    GFX_OffsetX(35000)
    Unknown3004(-26)
    sprite('vr_azef440_26', 5)
    GFX_OffsetX(35000)

@State
def BrustDD_SlashEff3Ex():

    def upon_IMMEDIATE():
        GFX_SetPalette(1)
        Unknown3032()
        Unknown2005()
        GFX_OffsetY(290000)
        Unknown4007(2)
        Unknown21010(1)
        GFX_Scale(2000)
    sprite('vr_azef440_20', 2)
    GFX_0('BrustDD_brust', -1)
    Unknown23015(11)
    sprite('vr_azef440_21', 2)
    sprite('vr_azef440_22', 2)
    GFX_OffsetX(35000)
    sprite('vr_azef440_22', 4)
    GFX_OffsetX(35000)
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(45000)
    Unknown1097(700)
    Unknown35()
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(120000)
    Unknown1097(700)
    Unknown35()
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(-45000)
    Unknown23015(11)
    Unknown35()
    GFX_0('BrustDD_EXeff2', -1)
    Unknown36(1)
    Unknown1073(-140000)
    Unknown23015(11)
    Unknown35()
    sprite('vr_azef440_23', 4)
    GFX_OffsetX(35000)
    Unknown21010(0)
    sprite('vr_azef440_24', 4)
    GFX_OffsetX(35000)
    sprite('vr_azef440_25', 4)
    GFX_OffsetX(35000)
    Unknown3004(-26)
    sprite('vr_azef440_26', 5)
    GFX_OffsetX(35000)

@State
def BrustDD_brust():

    def upon_IMMEDIATE():
        GFX_2('azef_440brust2_00')
        Unknown21010(1)
    sprite('null', 10)
    sprite('null', 50)
    Unknown21010(0)

@State
def BrustDD_EXeff():

    def upon_IMMEDIATE():
        GFX_SetPalette(1)
        GFX_Scale(1500)
        Unknown3033()
    sprite('vr_azef440_30', 2)
    sprite('vr_azef440_31', 2)
    sprite('vr_azef440_32', 8)
    sprite('vr_azef440_33', 3)
    sprite('vr_azef440_34', 3)
    sprite('vr_azef440_35', 3)
    Unknown3004(-26)
    sprite('vr_azef440_36', 3)
    sprite('vr_azef440_37', 3)

@State
def BrustDD_EXeff2():

    def upon_IMMEDIATE():
        GFX_SetPalette(1)
        GFX_Scale(1500)
        Unknown3033()
    sprite('vr_azef440_32', 8)
    sprite('vr_azef440_33', 3)
    sprite('vr_azef440_34', 3)
    sprite('vr_azef440_35', 3)
    Unknown3004(-26)
    sprite('vr_azef440_36', 3)
    sprite('vr_azef440_37', 3)

@State
def __440Aura():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown2054(1)
        IsInvisibility(1)
        sendToLabelUpon(32, 0)
        Unknown4003('azef_aura02', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(0)
        GFX_Scale(950)
    sprite('null', 5)
    Unknown3004(51)
    label(1)
    sprite('vr_azef610_efpos00', 2)
    Unknown3004(0)
    PFX('azef_407backaura_02', 0)
    PFX('azef_407backaura_02', 1)
    PFX('azef_407backaura_02', 2)
    PFX('azef_407backaura_02', 3)
    PFX('azef_407backaura_02', 4)
    PFX('azef_407backaura_02', 5)
    sprite('vr_azef610_efpos00', 2)
    PFX('azef_407backaura_02', 6)
    PFX('azef_407backaura_02', 7)
    PFX('azef_407backaura_02', 8)
    PFX('azef_407backaura_02', 9)
    sprite('vr_azef610_efpos00', 2)
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('vr_azef430_efpos02', 10)
    Unknown3004(-51)

@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    SFX_0('019_quake_0')
    loopRest()
    gotoLabel(0)

@State
def Eventoffset_Sosai():

    def upon_IMMEDIATE():
        Unknown1001(0)
        Unknown1006(500000)
        Unknown1010(-100000, 80000)
    sprite('null', 4)
    GFX_1('ef_offset', 0)
    SFX_0('108_attack_offset')
    ScreenShake(30000, 30000)

@State
def Act2Event_Bang():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown2034(0)
        Unknown30012(0)
        Unknown1000(360000)
        Unknown2005()
        Unknown2004(1, 0)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(2, 9)
    sprite('bn070_03', 32767)
    loopRest()
    label(0)
    sprite('bn070_03', 20)
    sprite('bn070_04', 4)
    sprite('bn070_05', 4)
    sprite('bn070_06', 4)
    sprite('bn070_07', 4)
    sprite('bn070_08', 4)
    sprite('bn070_09', 4)
    sprite('bn063_11', 4)
    GFX_OffsetX(130000)
    Unknown8000(0, 1, 1)
    SFX_0('209_down_normal_0')
    sprite('bn063_11', 32767)
    loopRest()
    label(1)
    sprite('bn064_00', 3)
    sprite('bn064_01', 3)
    sprite('bn064_03', 3)
    sprite('bn064_05', 3)
    sprite('bn064_07', 3)
    sprite('bn064_09', 3)
    sprite('bn064_11', 3)
    loopRest()
    label(100)
    sprite('bn000_00', 7)
    sprite('bn000_01', 7)
    sprite('bn000_02', 7)
    sprite('bn000_03', 7)
    sprite('bn000_04', 7)
    sprite('bn000_05', 7)
    sprite('bn000_06', 7)
    sprite('bn000_07', 7)
    sprite('bn000_08', 7)
    sprite('bn000_09', 7)
    sprite('bn000_11', 7)
    loopRest()
    gotoLabel(100)
    label(2)
    sprite('keep', 2)
    sprite('bn022_00', 5)
    physicsXImpulse(-30000)
    physicsYImpulse(36000)
    setGravity(1800)
    Unknown8001(0, 0)
    SFX_0('001_airbackdash_0')
    sprite('bn022_01', 5)
    sprite('bn022_02', 5)
    label(101)
    sprite('bn022_02', 5)
    loopRest()
    gotoLabel(101)
    label(9)
    sprite('null', 2)
    loopRest()

@State
def Act3Event_ar():

    def upon_IMMEDIATE():
        Unknown13040('vraref000_00', 160, 0, 0, 500, 0, 2147483647, 1000, 1000)
        Unknown30012(0)
        GFX_OffsetX(-80000)
        Unknown2019(-1000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('ar000_00', 5)
    sprite('ar000_01', 5)
    sprite('ar000_02', 5)
    sprite('ar000_03', 5)
    sprite('ar000_04', 5)
    sprite('ar000_05', 5)
    sprite('ar000_06', 5)
    sprite('ar000_07', 5)
    sprite('ar000_08', 5)
    sprite('ar000_09', 5)
    sprite('ar000_11', 5)
    sprite('ar000_12', 5)
    sprite('ar000_13', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ar060_01', 10)
    PFX_Scale(1500)
    PFX('ef_hitmd', 103)
    SFX_0('100_hit_grap_3')
    ScreenShake(1000, 20000)
    sprite('ar060_02', 4)
    physicsXImpulse(-45000)
    physicsYImpulse(27000)
    setGravity(2700)
    sendToLabelUpon(2, 4)
    sprite('ar060_03', 4)
    sprite('ar060_04', 32767)
    sendToLabelUpon(2, 2)
    loopRest()
    label(2)
    sprite('keep', 2)
    SFX_0('012_stab_deep')
    SFX_0('209_down_normal_0')

@State
def Act3Event_ar_01():

    def upon_IMMEDIATE():
        Unknown13040('vraref000_00', 160, 0, 0, 500, 0, 2147483647, 1000, 1000)
        Unknown30012(0)
        Unknown2034(0)
        Collidable(0)
        Unknown2005()

        def upon_32():
            sendToLabel(2)

            def upon_3():
                if (SLOT_50 < 350000):
                    clearUponHandler(3)
                    sendToLabel(0)

        def upon_33():
            sendToLabel(2)

            def upon_3():
                if (SLOT_19 < 240000):
                    clearUponHandler(3)
                    sendToLabel(0)
        sendToLabelUpon(36, 4)
    sprite('null', 32767)
    Unknown1000(-920000)
    label(0)
    sprite('ar030_10', 4)
    endMomentum(1)
    label(1)
    sprite('ar000_00', 5)
    sprite('ar000_01', 5)
    sprite('ar000_02', 5)
    sprite('ar000_03', 5)
    sprite('ar000_04', 5)
    sprite('ar000_05', 5)
    sprite('ar000_06', 5)
    sprite('ar000_07', 5)
    sprite('ar000_08', 5)
    sprite('ar000_09', 5)
    sprite('ar000_11', 5)
    sprite('ar000_12', 5)
    sprite('ar000_13', 5)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ar030_00', 7)
    Unknown2015(200)
    physicsXImpulse(7200)
    sprite('ar030_01', 7)
    label(3)
    sprite('ar030_02', 7)
    sprite('ar030_03', 7)
    sprite('ar030_04', 7)
    sprite('ar030_05', 7)
    sprite('ar030_06', 7)
    sprite('ar030_07', 7)
    sprite('ar030_08', 7)
    sprite('ar030_09', 7)
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('ar610_09', 1)
    Unknown1086(22)
    endMomentum(1)
    clearUponHandler(3)
    sprite('ar610_09', 1)
    sprite('ar610_10', 2)
    sprite('ar610_11', 2)
    loopRest()
    label(5)
    sprite('ar610_09', 2)
    sprite('ar610_10', 2)
    sprite('ar610_11', 2)
    loopRest()
    gotoLabel(5)

@State
def Act3Event_ar_02():

    def upon_IMMEDIATE():
        Unknown13040('vraref000_00', 160, 0, 0, 500, 0, 2147483647, 1000, 1000)
        Unknown30012(0)
        Unknown2034(0)
        Unknown1086(22)
        sendToLabelUpon(36, 4)
    label(0)
    sprite('ar610_09', 2)
    sprite('ar610_10', 2)
    sprite('ar610_11', 2)
    loopRest()
    gotoLabel(0)

@State
def Act3Event_ar_03():

    def upon_IMMEDIATE():
        Unknown13040('vraref000_00', 160, 0, 0, 500, 0, 2147483647, 1000, 1000)
        Unknown30012(0)
        Unknown2034(0)
        Collidable(0)
        Unknown1086(2)
        Unknown2019(1000)
        sendToLabelUpon(32, 0)
    sprite('ar060_15', 32767)
    GFX_OffsetX(-50000)
    loopRest()
    label(0)
    sprite('ar060_01', 10)
    PFX_Scale(1500)
    PFX('ef_hitmd', 103)
    SFX_0('100_hit_grap_3')
    ScreenShake(1000, 20000)
    sprite('ar060_02', 4)
    physicsXImpulse(-45000)
    physicsYImpulse(27000)
    setGravity(2700)
    sendToLabelUpon(2, 4)
    sprite('ar060_03', 4)
    sprite('ar060_04', 32767)
    sendToLabelUpon(2, 2)
    loopRest()
    label(2)
    sprite('keep', 2)
    SFX_0('012_stab_deep')
    SFX_0('209_down_normal_0')