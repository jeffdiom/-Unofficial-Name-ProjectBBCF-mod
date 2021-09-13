@State
def EMB_BN():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(240000)
        Unknown2054(1)
        IsInvisibility(1)
        Unknown4003('ef_emb_BN.DIG', 'ef_emb_BN_motion_000.mmot')
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
def EMB_BN_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(240000)
        Unknown2054(1)
        IsInvisibility(1)
        Unknown4003('ef_emb_BN.DIG', 'ef_emb_BN_motion_000.mmot')
        Unknown23015(5)
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
def EMB_BN_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(240000)
        Unknown2054(1)
        Unknown4003('ef_emb_BN.DIG', 'ef_emb_BN_motion_000.mmot')
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
def bn_win():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    Unknown1006(488000)
    PFX('bnef_win_smoke', -1)
    loopRest()

@State
def bn_bomber():

    def upon_IMMEDIATE():
        Unknown4007(3)
    sprite('null', 1)
    ScreenShake(0, 16000)
    Unknown1000(0)
    PFX_Scale(1500)
    PFX('bnef_bomber', -1)
    loopRest()

@State
def bn_perfect_ray():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown1000(0)
        Unknown1006(288000)
    label(0)
    sprite('null', 1)
    Unknown4054(1)
    PFX('ef_speed_center', -1)
    gotoLabel(0)

@State
def bn_perfect_font00():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown6001(1)
        Unknown2007()
        GFX_SetPalette(2)
        Unknown3032()
        Unknown1000(-1040000)
        Unknown1006(-208000)
        Unknown23015(4)
    sprite('bnef611_00', 32767)

@State
def bn_perfect_font01():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown6001(1)
        Unknown2007()
        GFX_SetPalette(2)
        Unknown3032()
        Unknown1000(-1040000)
        Unknown1006(-576000)
        Unknown23015(4)
    sprite('bnef611_01', 32767)

@State
def bn_perfect_font02():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown6001(1)
        Unknown2007()
        GFX_SetPalette(2)
        Unknown3032()
        Unknown1000(-244000)
        Unknown1006(-172000)
        Unknown23015(4)
    sprite('bnef611_02', 32767)

@State
def bn_perfect_font03():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown6001(1)
        Unknown2007()
        GFX_SetPalette(2)
        Unknown3032()
        Unknown1000(-244000)
        Unknown1006(-592000)
        Unknown23015(4)
    sprite('bnef611_03', 32767)

@State
def bn_perfect_font00b():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown6001(1)
        Unknown2007()
        GFX_SetPalette(2)
        Unknown3033()
        Unknown1000(-1040000)
        Unknown1006(-208000)
        Unknown2054(1)
        Unknown23015(4)
    sprite('bnef611_10', 32767)

@State
def bn_perfect_font01b():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown6001(1)
        Unknown2007()
        GFX_SetPalette(2)
        Unknown3033()
        Unknown1000(-1040000)
        Unknown1006(-576000)
        Unknown2054(1)
        Unknown23015(4)
    sprite('bnef611_11', 32767)

@State
def bn_perfect_font02b():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown6001(1)
        Unknown2007()
        GFX_SetPalette(2)
        Unknown3033()
        Unknown1000(-244000)
        Unknown1006(-172000)
        Unknown2054(1)
        Unknown23015(4)
    sprite('bnef611_12', 32767)

@State
def bn_perfect_font03b():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown6001(1)
        Unknown2007()
        GFX_SetPalette(2)
        Unknown3033()
        Unknown1000(-244000)
        Unknown1006(-592000)
        Unknown2054(1)
        Unknown23015(4)
    sprite('bnef611_13', 32767)

@State
def bn_throw():

    def upon_IMMEDIATE():
        Unknown4007(3)
    sprite('null', 1)
    GFX_OffsetY(150000)
    GFX_1('bnef_throw_smoke', -1)
    GFX_1('bnef_throw_leaf', -1)
    loopRest()

@State
def bn_throw_b():

    def upon_IMMEDIATE():
        Unknown4007(3)
    sprite('null', 1)
    GFX_OffsetY(150000)
    GFX_1('bnef_throw_smoke', -1)
    loopRest()

@State
def bn_throw_air():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_OffsetY(288000)
    GFX_1('bnef_throw_smoke', -1)
    GFX_1('bnef_throw_leaf', -1)
    loopRest()

@State
def bn_throw_air_b():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_OffsetY(288000)
    Unknown4054(4)
    PFX('bnef_throw_smoke', -1)
    loopRest()

@State
def bn_sp_throw():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_OffsetY(155000)
    GFX_1('bnef_sp_throw_speed', -1)
    GFX_1('bnef_sp_throw_leaf', -1)
    loopRest()

@State
def bn_sp_throw_b():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_OffsetY(280000)
    GFX_1('bnef_sp_throw_speed', -1)
    loopRest()

@State
def bn_sp_throw_c():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_OffsetY(260000)
    GFX_1('bnef_sp_throw_speed', -1)
    GFX_1('bnef_sp_throw_leaf', -1)
    loopRest()

@State
def bn_sp_throw_d():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_OffsetY(245000)
    GFX_1('bnef_sp_throw_speed', -1)
    loopRest()

@State
def bn_sp_air_throw():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_OffsetY(295000)
    GFX_1('bnef_sp_throw_speed', -1)
    GFX_1('bnef_sp_throw_leaf', -1)
    loopRest()

@State
def bn_sp_air_throw_b():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_OffsetY(360000)
    GFX_1('bnef_sp_throw_speed', -1)
    loopRest()

@State
def bn_sp_air_throw_c():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_OffsetY(365000)
    GFX_1('bnef_sp_throw_speed', -1)
    GFX_1('bnef_sp_throw_leaf', -1)
    loopRest()

@State
def bn_sp_air_throw_d():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_OffsetY(350000)
    GFX_1('bnef_sp_throw_speed', -1)
    loopRest()

@State
def bn_strike():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown4007(3)
        Unknown4010(3)
        GFX_SetPalette(1)
        Unknown3033()
    sprite('vrbnef404_00', 2)
    Unknown3001(0)
    Unknown3004(192)
    sprite('vrbnef404_01', 2)
    Unknown3001(255)
    Unknown3004(0)
    sprite('vrbnef404_02', 2)
    sprite('vrbnef404_03', 4)
    GFX_1('bnef_knuckle', 0)
    GFX_1('bnef_knuckle', 1)
    GFX_1('bnef_knuckle', 2)
    GFX_1('bnef_knuckle', 3)
    GFX_1('bnef_knuckle', 4)
    sprite('vrbnef404_04', 3)
    sprite('vrbnef404_05', 2)
    sprite('vrbnef404_06', 2)
    sprite('vrbnef404_07', 2)

@State
def bn_strike_air():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown4007(3)
        Unknown4010(3)
        GFX_Scale(1000)
        GFX_SetPalette(1)
        Unknown3033()
    sprite('vrbnef405_00', 3)
    Unknown3001(0)
    Unknown3004(128)
    sprite('vrbnef405_01', 3)
    Unknown3001(255)
    Unknown3004(0)
    sprite('vrbnef405_02', 3)
    GFX_1('bnef_knuckle_air', 0)
    GFX_1('bnef_knuckle_air', 1)
    GFX_1('bnef_knuckle_air', 2)
    GFX_1('bnef_knuckle_air', 3)
    GFX_1('bnef_knuckle_air', 4)
    GFX_1('bnef_knuckle_air', 5)
    GFX_1('bnef_knuckle_air', 6)
    sprite('vrbnef405_03', 3)
    sprite('vrbnef405_04', 2)
    sprite('vrbnef405_05', 2)

@State
def GuardCrash():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown4007(3)
        Unknown4010(3)
        GFX_SetPalette(1)
        Unknown3033()
    sprite('vrbnef410_00', 3)
    sprite('vrbnef410_01', 3)
    GFX_1('bnef_guardcrash', 0)
    sprite('vrbnef410_02', 3)
    GFX_1('bnef_guardcrash', 0)
    GFX_1('bnef_guardcrash', 1)
    GFX_1('bnef_guardcrash', 2)
    sprite('vrbnef410_03', 3)
    sprite('vrbnef410_04', 3)

@State
def shotAD_Matome():
    sprite('shot_expoint', 60)
    GFX_0('bn_shot_A', 0)
    Unknown21007(1, 33)
    SLOT_31 = (SLOT_31 + (-1))
    PFX_Rotation(45000)
    PFX('bnef_kugi_pitch', 1)
    if (SLOT_31 >= 1):
        GFX_0('bn_shot_A', 0)
        Unknown21007(1, 32)
        SLOT_31 = (SLOT_31 + (-1))
        PFX_Rotation(60000)
        PFX('bnef_kugi_pitch', 2)
    if (SLOT_31 >= 1):
        GFX_0('bn_shot_A', 0)
        Unknown21007(1, 34)
        SLOT_31 = (SLOT_31 + (-1))
        PFX_Rotation(30000)
        PFX('bnef_kugi_pitch', 0)

@State
def bn_shot_A():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        AttackP2(74)
        AirUntechableTime(18)
        Hitstop(0)
        Unknown11001(5, 5, 5)
        AttackAttributes(0, 0, 0, 1, 0)
        SlashFX(1)
        Unknown53(1)
        Unknown2055(120)
        GFX_Scale(1250)
        GFX_SetPalette(0)
        Unknown2035(1)
        StarterRating(2)
        Unknown11057(500)
        Unknown12052(1)
        Unknown23182(2)
        Unknown11075(300, 120)
        GFX_Rotation(30000)
        AirPushbackX(16000)
        AirPushbackY(5000)
        physicsXImpulse(32000)
        physicsYImpulse(-18000)

        def upon_32():
            GFX_Rotation(15000)
            physicsXImpulse(48000)
            physicsYImpulse(-9000)

        def upon_33():
            GFX_Rotation(30000)
            physicsXImpulse(32000)
            physicsYImpulse(-18000)

        def upon_34():
            GFX_Rotation(45000)
            physicsXImpulse(16000)
            physicsYImpulse(-27000)

        def upon_12():
            GFX_0('bn_shot_A_hit', -1)
            clearUponHandler(12)
        sendToLabelUpon(10, 2)
        sendToLabelUpon(2, 2)

        def upon_39():
            Unknown2003(1)
        if SLOT_137:
            DamageMultiplier(80)
    label(0)
    sprite('vrbnef406_002', 4)
    sprite('vrbnef406_003', 4)
    loopRest()
    gotoLabel(0)
    label(2)
    clearUponHandler(10)
    clearUponHandler(2)
    sprite('null', 1)
    GFX_0('bn_shot_reflect', -1)

@State
def bn_shot_A_hit():

    def upon_IMMEDIATE():
        Unknown2035(1)
        GFX_SetPalette(0)
        GFX_Scale(1250)
        Unknown3032()
    sprite('null', 2)
    Unknown4051(0)
    PFX('bnef_kugi_poison', -1)

@State
def bn_shot_reflect():

    def upon_IMMEDIATE():
        Unknown2035(1)
        GFX_SetPalette(0)
        GFX_Scale(1250)
        Unknown3032()
    sprite('vrbnef406_001', 60)
    Unknown3001(255)
    Unknown3004(-4)
    Unknown1074(15000)
    physicsYImpulse(20000)
    physicsXImpulse(5000)
    setGravity(2000)
    GFX_1('bnef_kugi_hit', -1)

@State
def shotBD_Matome():
    sprite('shot_expoint', 60)
    GFX_0('bn_shot_B', 0)
    Unknown21007(1, 33)
    SLOT_31 = (SLOT_31 + (-1))
    PFX_Rotation(45000)
    PFX('bnef_kugi_pitch', 1)
    if (SLOT_31 >= 1):
        GFX_0('bn_shot_B', 0)
        Unknown21007(1, 32)
        SLOT_31 = (SLOT_31 + (-1))
        PFX_Rotation(60000)
        PFX('bnef_kugi_pitch', 2)
    if (SLOT_31 >= 1):
        GFX_0('bn_shot_B', 0)
        Unknown21007(1, 34)
        SLOT_31 = (SLOT_31 + (-1))
        PFX_Rotation(30000)
        PFX('bnef_kugi_pitch', 0)

@State
def bn_shot_B():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        AttackP2(94)
        Unknown11092(1)
        AirUntechableTime(14)
        Hitstop(0)
        Unknown11001(5, 5, 5)
        AirPushbackX(16000)
        AirPushbackY(7000)
        AttackAttributes(0, 0, 0, 1, 0)
        SlashFX(1)
        StarterRating(2)
        Unknown12052(1)
        Unknown11057(500)

        def upon_3():
            if SLOT_51:
                clearUponHandler(3)
                AttackLevel_(3)
                AirUntechableTime(17)
                Hitstop(11)
                Unknown11001(0, 0, 2)
                GroundedHitstunAnimation(9)
                AirHitstunAnimation(9)
                AirPushbackX(5400)
                AirPushbackY(24000)
                SlashFX(0)
                FireFX(1)
                Unknown11057(1000)
                ProjectileHitWall(1)
                Unknown2035(1)
                Unknown3032()
                GFX_Scale(1250)
                Unknown3001(255)
                Unknown3004(-4)
                Unknown1074(36000)
                ProjectileDisapperOnHit(3)
        ProjectileHitWall(1)
        Unknown2055(120)
        GFX_Scale(1250)
        GFX_SetPalette(0)
        Unknown2035(1)
        physicsXImpulse(38000)
        GFX_Rotation(65000)
        physicsXImpulse(21111)
        physicsYImpulse(-38000)

        def upon_32():
            GFX_Rotation(10000)
            physicsXImpulse(38000)
            physicsYImpulse(-8444)

        def upon_33():
            GFX_Rotation(20000)
            physicsXImpulse(38000)
            physicsYImpulse(-16888)

        def upon_34():
            GFX_Rotation(30000)
            physicsXImpulse(38000)
            physicsYImpulse(-25333)
        sendToLabelUpon(10, 1)
        sendToLabelUpon(2, 2)
        sendToLabelUpon(7, 3)

        def upon_39():
            Unknown2003(1)
    label(0)
    sprite('vrbnef406_004', 4)
    sprite('vrbnef406_005', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(7)
    sprite('null', 2)
    StartMultihit()
    sprite('vrbnef406_001', 24)
    SLOT_51 = 1
    Unknown1019(-33)
    YAccel(-50)
    PFX_Rotation(90000)
    PFX('bnef_kugi_hit', -1)
    sprite('null', 2)
    PFX_Scale(2000)
    PFX('bnef_kugi_fire', -1)
    Unknown1074(0)
    endMomentum(1)
    sprite('vrbnef406_006_dummy', 3)
    RefreshMultihit()
    IsInvisibility(1)
    ExitState()
    label(2)
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(7)
    sprite('vrbnef406_001', 24)
    SLOT_51 = 1
    Unknown1019(33)
    YAccel(-50)
    GFX_1('bnef_kugi_hit', -1)
    sprite('null', 2)
    PFX_Scale(2000)
    PFX('bnef_kugi_fire', -1)
    Unknown1074(0)
    endMomentum(1)
    sprite('vrbnef406_006_dummy', 3)
    RefreshMultihit()
    IsInvisibility(1)
    ExitState()
    label(3)
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(7)
    sprite('vrbnef406_001', 24)
    SLOT_51 = 1
    Unknown1019(-33)
    YAccel(75)
    PFX_Rotation(90000)
    PFX('bnef_kugi_hit', -1)
    sendToLabelUpon(2, 2)
    sprite('null', 2)
    PFX_Scale(2000)
    PFX('bnef_kugi_fire', -1)
    clearUponHandler(2)
    Unknown1074(0)
    endMomentum(1)
    sprite('vrbnef406_006_dummy', 3)
    RefreshMultihit()
    IsInvisibility(1)

@State
def bn_shot_B_Event():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(300)
        AttackP1(70)
        AttackP2(90)
        Hitstop(5)
        AirPushbackX(16000)
        AirPushbackY(5000)
        AttackAttributes(0, 0, 0, 1, 0)
        SlashFX(1)
        StarterRating(2)

        def upon_3():
            if SLOT_51:
                Unknown9000()
                AttackLevel_(3)
                Unknown11034(0)
                ProjectileDurabilityLvl(1)
                AttackAttributes(0, 0, 0, 1, 0)
                Damage(300)
                AttackP1(70)
                AttackP2(90)
                AirHitstunAnimation(9)
                GroundedHitstunAnimation(9)
                Unknown2035(1)
                StarterRating(2)
                GFX_SetPalette(0)
                GFX_Scale(1250)
                Unknown3032()
                ProjectileHitWall(1)
                ProjectileDisapperOnHit(3)
                Unknown3001(255)
                Unknown3004(-4)
                Unknown1074(36000)
                clearUponHandler(3)
        ProjectileHitWall(1)
        Unknown2055(120)
        GFX_Scale(1250)
        GFX_SetPalette(0)
        Unknown2035(1)
        GFX_Rotation(45000)
        physicsXImpulse(28000)
        physicsYImpulse(-28000)
        sendToLabelUpon(10, 1)
        sendToLabelUpon(2, 2)
        sendToLabelUpon(7, 3)
    label(0)
    sprite('vrbnef406_004', 4)
    sprite('vrbnef406_005', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(7)
    sprite('null', 2)
    StartMultihit()
    sprite('vrbnef406_001', 24)
    SLOT_51 = 1
    Unknown1019(-33)
    YAccel(-150)
    PFX_Rotation(90000)
    PFX('bnef_kugi_hit', -1)
    sprite('null', 2)
    PFX_Scale(2000)
    PFX('bnef_kugi_fire', -1)
    sprite('vrbnef406_006_dummy', 3)
    IsInvisibility(1)
    loopRest()
    ExitState()
    label(2)
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(7)
    sprite('null', 2)
    StartMultihit()
    sprite('vrbnef406_001', 24)
    SLOT_51 = 1
    Unknown1019(33)
    YAccel(-100)
    GFX_1('bnef_kugi_hit', -1)
    sprite('null', 2)
    PFX_Scale(2000)
    PFX('bnef_kugi_fire', -1)
    sprite('vrbnef406_006_dummy', 3)
    IsInvisibility(1)
    loopRest()
    ExitState()
    label(3)
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(7)
    sprite('null', 2)
    StartMultihit()
    sprite('vrbnef406_001', 24)
    SLOT_51 = 1
    Unknown1019(-33)
    YAccel(150)
    PFX_Rotation(90000)
    PFX('bnef_kugi_hit', -1)
    sendToLabelUpon(2, 2)
    sprite('null', 2)
    PFX_Scale(2000)
    PFX('bnef_kugi_fire', -1)
    clearUponHandler(2)
    sprite('vrbnef406_006_dummy', 3)
    IsInvisibility(1)
    loopRest()

@State
def shotCD_Matome():
    sprite('shot_expoint', 60)
    GFX_0('bn_shot_C', 1)
    Unknown21007(1, 33)
    SLOT_31 = (SLOT_31 + (-1))
    PFX_Rotation(45000)
    PFX('bnef_kugi_pitch', 1)
    if (SLOT_31 >= 1):
        GFX_0('bn_shot_C', 1)
        Unknown21007(1, 32)
        SLOT_31 = (SLOT_31 + (-1))
        PFX_Rotation(60000)
        PFX('bnef_kugi_pitch', 2)
    if (SLOT_31 >= 1):
        GFX_0('bn_shot_C', 1)
        Unknown21007(1, 34)
        SLOT_31 = (SLOT_31 + (-1))
        PFX_Rotation(30000)
        PFX('bnef_kugi_pitch', 0)

@State
def bn_shot_C():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        AttackP2(84)
        hitstun(21)
        AirPushbackX(2500)
        AirPushbackY(10000)
        Hitstop(0)
        Unknown11001(20, 40, 40)
        AttackAttributes(0, 0, 0, 1, 0)
        SlashFX(1)
        Unknown53(1)
        Unknown2055(120)
        GFX_Scale(1250)
        GFX_SetPalette(0)
        Unknown2035(1)
        StarterRating(3)
        Unknown11057(500)
        Unknown12052(1)
        Unknown23182(2)
        PushbackX(1000)
        GFX_Rotation(45000)
        physicsXImpulse(18000)
        physicsYImpulse(-18000)
        GFX_Rotation(70000)
        physicsXImpulse(12000)
        physicsYImpulse(-48000)

        def upon_32():
            GFX_Rotation(60000)
            physicsXImpulse(14000)
            physicsYImpulse(-24248)

        def upon_33():
            GFX_Rotation(45000)
            physicsXImpulse(18000)
            physicsYImpulse(-18000)

        def upon_34():
            GFX_Rotation(30000)
            physicsXImpulse(24248)
            physicsYImpulse(-14000)

        def upon_11():
            GFX_0('bn_shot_C_hit', -1)
        sendToLabelUpon(10, 2)
        sendToLabelUpon(2, 2)

        def upon_39():
            Unknown2003(1)
    label(0)
    sprite('vrbnef406_006', 4)
    sprite('vrbnef406_007', 4)
    loopRest()
    gotoLabel(0)
    label(2)
    clearUponHandler(10)
    clearUponHandler(2)
    sprite('null', 1)
    GFX_0('bn_shot_reflect', -1)

@State
def bn_shot_C_hit():

    def upon_IMMEDIATE():
        Unknown2035(1)
        GFX_Scale(1250)
        Unknown3032()
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
    sprite('null', 60)
    GFX_1('bnef_kugi_web_bom', -1)
    GFX_0('bn_shot_C_web1', -1)
    GFX_0('bn_shot_C_web2', -1)
    GFX_0('bn_shot_C_web3', -1)
    GFX_0('bn_shot_C_web4', -1)
    GFX_0('bn_shot_C_web5', -1)
    GFX_0('bn_shot_C_web6', -1)

@State
def bn_shot_C_web1():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown4007(22)
        Unknown2007()
        Unknown3033()
        Unknown2055(60)
    sprite('vrbnef406_090', 15)
    Unknown1000(128000)
    Unknown1006(192000)
    Unknown1010(0, 64000)
    Unknown1011(-16000, 16000)
    Unknown1079()
    GFX_Scale(0)
    Unknown1099(50)
    GFX_0('bn_kugi_web_smoke', 2)
    sprite('vrbnef406_090', 30)
    Unknown1099(0)
    sprite('vrbnef406_090', 15)
    Unknown3004(-16)

@State
def bn_shot_C_web2():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown4007(22)
        Unknown2007()
        Unknown3033()
        Unknown2055(60)
    sprite('vrbnef406_090', 10)
    Unknown1000(-128000)
    Unknown1006(192000)
    Unknown1010(-64000, 0)
    Unknown1011(-16000, 16000)
    Unknown1079()
    GFX_Scale(0)
    Unknown1099(50)
    GFX_0('bn_kugi_web_smoke', 2)
    sprite('vrbnef406_090', 35)
    Unknown1099(0)
    sprite('vrbnef406_090', 15)
    Unknown3004(-16)

@State
def bn_shot_C_web3():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown4007(22)
        Unknown2007()
        Unknown3033()
        Unknown2055(60)
    sprite('vrbnef406_090', 15)
    Unknown1000(64000)
    Unknown1006(128000)
    Unknown1010(0, 32000)
    Unknown1011(-16000, 16000)
    Unknown1079()
    GFX_Scale(0)
    Unknown1099(50)
    GFX_0('bn_kugi_web_smoke', 2)
    sprite('vrbnef406_090', 30)
    Unknown1099(0)
    sprite('vrbnef406_090', 15)
    Unknown3004(-16)

@State
def bn_shot_C_web4():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown4007(22)
        Unknown2007()
        Unknown3033()
        Unknown2055(60)
    sprite('vrbnef406_090', 10)
    Unknown1000(-64000)
    Unknown1006(128000)
    Unknown1010(-32000, 0)
    Unknown1011(-16000, 16000)
    Unknown1079()
    GFX_Scale(0)
    Unknown1099(50)
    GFX_0('bn_kugi_web_smoke', 2)
    sprite('vrbnef406_090', 35)
    Unknown1099(0)
    sprite('vrbnef406_090', 15)
    Unknown3004(-16)

@State
def bn_shot_C_web5():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown4007(22)
        Unknown2007()
        Unknown3033()
        Unknown2055(60)
    sprite('vrbnef406_090', 10)
    Unknown1000(64000)
    Unknown1006(320000)
    Unknown1010(32000, 0)
    Unknown1011(-16000, 16000)
    Unknown1079()
    GFX_Scale(0)
    Unknown1099(50)
    GFX_0('bn_kugi_web_smoke', 2)
    sprite('vrbnef406_090', 25)
    Unknown1099(0)
    sprite('vrbnef406_090', 15)
    Unknown3004(-16)

@State
def bn_shot_C_web6():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown4007(22)
        Unknown2007()
        Unknown3033()
        Unknown2055(60)
    sprite('vrbnef406_090', 10)
    Unknown1000(-64000)
    Unknown1006(256000)
    Unknown1010(-32000, 0)
    Unknown1011(-16000, 16000)
    Unknown1079()
    GFX_Scale(0)
    Unknown1099(50)
    GFX_0('bn_kugi_web_smoke', 2)
    sprite('vrbnef406_090', 35)
    Unknown1099(0)
    sprite('vrbnef406_090', 15)
    Unknown3004(-16)

@State
def bn_kugi_web_smoke():

    def upon_IMMEDIATE():
        Unknown2055(60)
    sprite('null', 1)
    GFX_1('bnef_kugi_web_smoke', -1)

@State
def shotD_Matome():
    sprite('shot_expoint', 60)
    GFX_0('bn_shot_D', 1)
    Unknown21007(1, 33)
    SLOT_31 = (SLOT_31 + (-1))
    PFX_Rotation(45000)
    PFX('bnef_kugi_pitch', 1)
    if (SLOT_31 >= 1):
        GFX_0('bn_shot_D', 2)
        Unknown21007(1, 32)
        SLOT_31 = (SLOT_31 + (-1))
        PFX_Rotation(60000)
        PFX('bnef_kugi_pitch', 2)
    if (SLOT_31 >= 1):
        GFX_0('bn_shot_D', 0)
        Unknown21007(1, 34)
        SLOT_31 = (SLOT_31 + (-1))
        PFX_Rotation(30000)
        PFX('bnef_kugi_pitch', 0)

@State
def bn_shot_D():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown2010()
        AttackLevel_(1)
        Damage(300)
        AttackP1(80)
        AttackP2(94)
        Hitstop(0)
        Unknown11001(5, 5, 5)
        AttackAttributes(0, 0, 0, 1, 0)
        SlashFX(1)
        Unknown53(1)
        Unknown2055(360)
        GFX_Scale(1250)
        GFX_SetPalette(0)
        Unknown2035(1)
        StarterRating(2)
        Unknown11057(500)
        Unknown12052(1)
        Unknown23182(2)
        GFX_Scale(1250)
        AirPushbackX(14000)
        AirPushbackY(-10000)

        def upon_32():
            GFX_Rotation(60000)
            physicsXImpulse(14000)
            physicsYImpulse(-24248)

            def upon_LANDING():
                GFX_Rotation(-60000)
                Unknown47(2, 2, 13, 0, -1, 2, 13)
                GFX_1('bnef_kugi_hit', -1)
                AirPushbackY(12000)

        def upon_33():
            GFX_Rotation(45000)
            physicsXImpulse(18000)
            physicsYImpulse(-18000)

            def upon_LANDING():
                GFX_Rotation(-45000)
                Unknown47(2, 2, 13, 0, -1, 2, 13)
                GFX_1('bnef_kugi_hit', -1)
                AirPushbackY(12000)

        def upon_34():
            GFX_Rotation(30000)
            physicsXImpulse(24248)
            physicsYImpulse(-14000)

            def upon_LANDING():
                GFX_Rotation(-30000)
                Unknown47(2, 2, 13, 0, -1, 2, 13)
                GFX_1('bnef_kugi_hit', -1)
                AirPushbackY(12000)
        sendToLabelUpon(10, 2)

        def upon_39():
            Unknown2003(1)
        if SLOT_137:
            DamageMultiplier(80)
    label(0)
    sprite('vrbnef406_008', 4)
    sprite('vrbnef406_009', 4)
    loopRest()
    gotoLabel(0)
    label(2)
    clearUponHandler(10)
    clearUponHandler(2)
    sprite('null', 1)
    GFX_0('bn_shot_reflect', -1)

@State
def bn_shot_E():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown2010()
        AttackLevel_(1)
        Hitstop(0)
        GFX_SetPalette(0)
        Unknown53(1)
        Unknown2055(120)
        sendToLabelUpon(10, 1)
        sendToLabelUpon(2, 2)
    GFX_Scale(1250)
    GFX_Rotation(30000)
    physicsXImpulse(24248)
    physicsYImpulse(-14000)
    label(0)
    sprite('vrbnef406_010', 4)
    sprite('vrbnef406_011', 4)
    gotoLabel(0)
    label(1)
    GFX_0('bn_shot_reflect', -1)
    gotoLabel(3)
    label(2)
    GFX_0('bn_shot_reflect', -1)
    label(3)

@State
def bn_stuck_wheel():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        ProjectileDisapperOnHit(2)
        Unknown2035(1)
        Unknown2007()
        GFX_SetPalette(4)
        Unknown3033()
        Unknown2019(3999)
        Unknown1000(13000)
        Unknown1006(29000)
        SystemGFX('cmn_judgment', 65535)
        Unknown36(1)
        Unknown1006(100000)
        Unknown35()
        sendToLabelUpon(32, 90)

        def upon_33():
            Unknown1074(1000)

        def upon_34():
            Unknown1074(200)

        def upon_53():
            IsInvisibility(1)
    sprite('vrbnef407_90', 16)
    GFX_Scale(0)
    Unknown1099(31)
    Unknown1074(3000)
    sprite('vrbnef407_90', 2)
    GFX_Scale(500)
    Unknown1099(0)
    label(10)
    sprite('vrbnef407_90', 1)
    loopRest()
    gotoLabel(10)
    label(90)
    clearUponHandler(32)
    sprite('vrbnef407_90', 16)
    Unknown3004(-16)
    Unknown1099(31)

@State
def bn_stuck_Big():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        ProjectileDisapperOnHit(2)
        Unknown2035(1)
        Unknown2007()
        GFX_SetPalette(4)
        Unknown3033()
        Unknown2019(3999)
        Unknown1000(13000)
        Unknown1006(29000)
    sprite('vrbnef407_90', 15)
    GFX_Scale(500)
    Unknown1099(80)
    Unknown1074(6000)
    Unknown3004(-17)

@State
def bn_stuck():

    def upon_IMMEDIATE():
        Unknown2035(1)
        GFX_SetPalette(0)
        Unknown3032()
        Unknown2019(4000)
        ProjectileHitWall(1)
        sendToLabelUpon(32, 90)

        def upon_34():
            GFX_OffsetX(-180000)
            GFX_OffsetY(450000)

        def upon_35():
            GFX_OffsetX(200000)
            GFX_OffsetY(450000)

        def upon_36():
            GFX_OffsetX(580000)
            GFX_OffsetY(450000)

        def upon_37():
            GFX_OffsetX(200000)
            GFX_OffsetY(200000)
            Unknown48(23, 2, 51, 3, 2, 25)
            if (SLOT_51 < 370000):
                Unknown1000(1750000)

        def upon_39():
            GFX_OffsetX(-380000)
            GFX_OffsetY(270000)
            Unknown48(23, 2, 51, 3, 2, 23)
            if (SLOT_51 < 350000):
                Unknown1006(350000)

        def upon_40():
            GFX_OffsetY(270000)
            Unknown48(23, 2, 51, 3, 2, 23)
            if (SLOT_51 < 350000):
                Unknown1006(350000)

        def upon_41():
            GFX_OffsetX(380000)
            GFX_OffsetY(270000)
            Unknown48(23, 2, 51, 3, 2, 23)
            if (SLOT_51 < 350000):
                Unknown1006(350000)

        def upon_33():
            GFX_OffsetY(120000)
            Unknown48(23, 2, 51, 3, 2, 23)
            if (SLOT_51 < 350000):
                Unknown1006(350000)

        def upon_38():
            GFX_0('bn_stuck_Big', -1)
            SLOT_2 = (SLOT_2 + 5)
            SLOT_52 = (SLOT_52 + 1)
            if (SLOT_52 == 1):
                Unknown21007(4, 33)
                sendToLabel(1)
            if (SLOT_52 == 2):
                Unknown21007(4, 34)
                sendToLabel(2)
            if (SLOT_52 == 3):
                sendToLabel(90)

        def upon_45():
            if SLOT_2:
                Unknown23029(23, 38, 0)
                SLOT_2 = (SLOT_2 + (-1))

        def upon_53():
            IsInvisibility(1)
    sprite('null', 1)
    sprite('vrbnef407_001', 4)
    Unknown2007()
    GFX_Scale(1000)
    Unknown3001(0)
    Unknown3004(16)
    SFX_3('bnse_00')
    GFX_2('bnef_kugi_stuck')
    GFX_0('bn_stuck_wheel', -1)
    Unknown38(4, 1)
    sprite('vrbnef407_002', 4)
    sprite('vrbnef407_003', 4)
    label(0)
    sprite('vrbnef407_001', 4)
    sprite('vrbnef407_002', 4)
    sprite('vrbnef407_003', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrbnef407_004', 6)
    sprite('vrbnef407_005', 6)
    sprite('vrbnef407_006', 6)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('vrbnef407_007', 32767)
    label(90)
    sprite('vrbnef407_007', 12)
    Unknown3004(-21)
    Unknown21007(4, 32)
    clearUponHandler(32)
    clearUponHandler(44)

@State
def bn_DD_1_ray_speed():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown2054(1)
        Unknown1000(0)
        Unknown1006(288000)
        Unknown2055(44)
    label(0)
    sprite('null', 1)
    Unknown4051(2)
    PFX('bnef_DD_1_ray', -1)
    gotoLabel(0)

@State
def bn_DD_1_ray_center():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown2055(12)
    label(0)
    sprite('null', 1)
    GFX_0('bn_DD_1_ray_center_line', -1)
    gotoLabel(0)

@State
def bn_DD_1_ray_center2():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown2055(113)
    label(0)
    sprite('null', 1)
    GFX_0('bn_DD_1_ray_center_line', -1)
    gotoLabel(0)

@State
def bn_DD_1_ray_center_line():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23032(50)
        Unknown1006(288000)
    Unknown4054(1)
    PFX('ef_speed_center', -1)

@State
def bn_DD_1_bomber():

    def upon_IMMEDIATE():
        Unknown4007(3)
    sprite('null', 1)
    SFX_0('016_explode_2')
    SFX_0('015_blaze_2')
    ScreenShake(0, 128000)
    Unknown1000(0)
    GFX_1('bnef_DD_1_bomber', -1)

@State
def bn_DD_3_cutin():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown4007(3)
        Unknown2007()
        Unknown23015(3)
        Unknown1006(256000)
        Unknown2054(1)
        Unknown3032()
    sprite('vrbnef432_21', 4)
    Unknown1064(0)
    Unknown1067(250)
    Unknown3001(0)
    Unknown3004(14)
    Unknown23118(16777215)
    Unknown23117(-16777216, 20)
    sprite('vrbnef432_21', 16)
    Unknown1067(0)
    sprite('vrbnef432_21', 57)
    Unknown23120()
    Unknown1064(1000)

@State
def bn_DD_3_face():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown4007(3)
        Unknown2007()
        Unknown23015(3)
        GFX_SetPalette(0)
        Unknown1006(256000)
        Unknown2054(1)
        Unknown3032()
    sprite('null', 7)
    sprite('vrbnef432_20', 15)
    Unknown3001(0)
    Unknown3004(20)
    sprite('vrbnef432_20', 55)
    GFX_0('eyefire_l', 0)
    GFX_0('eyefire_r', 1)
    sprite('null', 1)

@State
def eyefire_l():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('null', 55)
    Unknown4054(1)
    Unknown23067('bnef_DD_3_eyefire')
    SFX_0('015_blaze_1')

@State
def eyefire_r():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('null', 55)
    Unknown4054(1)
    Unknown23067('bnef_DD_3_eyefire')

@State
def bn_DD_3_ray():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown2055(150)
    label(0)
    sprite('null', 1)
    GFX_0('bn_DD_3_ray_line', -1)
    gotoLabel(0)

@State
def bn_DD_3_ray_line():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(3)
        Unknown1006(320000)
    Unknown4054(1)
    PFX('ef_speed_center', -1)

@State
def bn_DD_3_rock():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(3)
    sprite('null', 1)
    Unknown4054(2)
    PFX('bnef_DD_3_rock', -1)

@State
def bn_DD_3_fire():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(3)
        Unknown1006(41000)
    sprite('null', 10)
    sprite('null', 1)
    Unknown4054(2)
    PFX('bnef_DD_3_fire', -1)

@State
def FuRinKaZan():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown6001(1)
        Unknown2054(1)
        Unknown2055(150)
        GFX_Scale(1950)
    sprite('null', 2)
    sprite('null', 10)
    GFX_0('3DEFF_Fu', -1)
    GFX_0('3DEFF_Rin', -1)
    GFX_0('3DEFF_Ka', -1)
    GFX_0('3DEFF_Zan', -1)
    Unknown1099(-2)
    sprite('null', 6)
    Unknown1099(-120)
    sprite('null', 2)
    Unknown1099(0)
    GFX_Scale(900)
    sprite('null', 2)
    GFX_Scale(1000)
    sprite('null', 2)
    GFX_Scale(900)
    sprite('null', 90)
    sprite('null', 30)
    Unknown1099(100)

@State
def __3DEFF_Fu():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4008(2)
        Unknown3032()
        GFX_OffsetX(-360000)
        Unknown1006(520000)
        Unknown23015(4)
        Unknown4003('ef_fu_BN.DIG', 'ef_fu_BN_motion_000.mmot')
    sprite('null', 15)
    Unknown3001(0)
    Unknown3004(10)
    Unknown23118(0)
    Unknown23119(16777215, 30, 2)
    sprite('null', 15)
    GFX_1('bnef_moji_tataki', -1)
    sprite('null', 70)
    sprite('null', 30)
    Unknown3004(-10)
    physicsXImpulse(-80000)
    physicsYImpulse(60000)

@State
def __3DEFF_Rin():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4008(2)
        Unknown3032()
        GFX_OffsetX(-380000)
        Unknown1006(150000)
        Unknown23015(4)
        Unknown4003('ef_rin_BN.DIG', 'ef_rin_BN_motion_000.mmot')
    sprite('null', 15)
    Unknown3001(0)
    Unknown3004(10)
    Unknown23118(0)
    Unknown23119(16777215, 30, 2)
    sprite('null', 15)
    GFX_1('bnef_moji_tataki', -1)
    sprite('null', 70)
    sprite('null', 30)
    Unknown3004(-10)
    physicsXImpulse(-80000)
    physicsYImpulse(-60000)

@State
def __3DEFF_Ka():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4008(2)
        Unknown3032()
        GFX_OffsetX(360000)
        Unknown1006(520000)
        Unknown23015(4)
        Unknown4003('ef_ka_BN.DIG', 'ef_ka_BN_motion_000.mmot')
    sprite('null', 15)
    Unknown3001(0)
    Unknown3004(10)
    Unknown23118(0)
    Unknown23119(16777215, 30, 2)
    sprite('null', 15)
    GFX_1('bnef_moji_tataki', -1)
    sprite('null', 70)
    sprite('null', 30)
    Unknown3004(-10)
    physicsXImpulse(80000)
    physicsYImpulse(60000)

@State
def __3DEFF_Zan():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4008(2)
        Unknown3032()
        GFX_OffsetX(380000)
        Unknown1006(160000)
        Unknown23015(4)
        Unknown4003('ef_zan_BN.DIG', 'ef_zan_BN_motion_000.mmot')
    sprite('null', 15)
    Unknown3001(0)
    Unknown3004(10)
    Unknown23118(0)
    Unknown23119(16777215, 30, 2)
    sprite('null', 15)
    GFX_1('bnef_moji_tataki', -1)
    sprite('null', 70)
    sprite('null', 30)
    Unknown3004(-10)
    physicsXImpulse(80000)
    physicsYImpulse(-60000)

@State
def bn_DD_2_hold():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown2035(1)
        GFX_SetPalette(0)
        Unknown2054(1)
    sprite('vrbnef431_000', 3)
    GFX_Rotation(60000)

@State
def bn_DD_2():

    def upon_IMMEDIATE():
        Unknown2035(1)
        GFX_SetPalette(0)
        Unknown3032()
        Unknown2054(1)
        sendToLabelUpon(44, 99)
        physicsYImpulse(9629)
        Unknown48(23, 2, 51, 22, 2, 22)
        Unknown47(1, 2, 22, 2, 51, 2, 51)
        if SLOT_38:
            Unknown47(3, 2, 51, 0, 40, 2, 12)
        else:
            Unknown47(3, 2, 51, 0, -40, 2, 12)
    sprite('vrbnef431_000', 27)
    Unknown1074(-27000)
    sprite('null', 1)
    clearUponHandler(44)
    Unknown2006()
    Unknown1074(0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    GFX_0('bn_DD_2_open', -1)
    SFX_0('019_cloth_b')
    SFX_0('019_cloth_b')
    Unknown2054(0)
    loopRest()
    ExitState()
    label(99)
    clearUponHandler(44)
    sprite('vrbnef431_005', 3)
    SFX_0('019_cloth_b')
    physicsYImpulse(0)
    sprite('vrbnef431_000', 3)
    sprite('vrbnef431_000', 10)
    GFX_Rotation(30000)
    Unknown1074(1000)
    physicsYImpulse(10000)
    setGravity(2000)
    sprite('vrbnef431_000', 30)
    Unknown3004(-12)

@State
def bn_DD_2_open():

    def upon_IMMEDIATE():
        Unknown2035(1)
        GFX_SetPalette(0)
        Unknown3032()
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0
        if (SLOT_31 == 0):
            SLOT_51 = 0
        if (SLOT_31 >= 1):
            SLOT_31 = (SLOT_31 + (-1))
            SLOT_51 = 6
        Unknown2007()

        def upon_3():
            Unknown48(23, 2, 52, 22, 2, 22)
            Unknown47(1, 2, 22, 2, 52, 2, 52)
            Unknown47(3, 2, 52, 0, 50, 2, 12)

        def upon_14():
            Unknown23090(23)
        FireBall(1, 0, 0, 0, 0, 0, 1, 0)

        def upon_54():
            clearUponHandler(54)
            clearUponHandler(3)
            clearUponHandler(39)
            SLOT_51 = 0
            Unknown1019(0)
            sendToLabel(580)

        def upon_53():
            sendToLabel(99)
        sendToLabelUpon(39, 99)
    sprite('vrbnef431_001', 4)
    sprite('vrbnef431_002', 4)
    sprite('vrbnef431_003', 4)
    sprite('vrbnef431_004', 4)
    sprite('vrbnef431_001', 4)
    sprite('vrbnef431_002', 4)
    sprite('vrbnef431_003', 4)
    sprite('vrbnef431_004', 4)
    sprite('vrbnef431_001', 4)
    sprite('vrbnef431_002', 4)
    sprite('vrbnef431_003', 4)
    sprite('vrbnef431_004', 3)
    sprite('vrbnef431_004', 1)
    Unknown19(99, 2, 51)
    label(1)
    sprite('vrbnef431_001', 2)
    GFX_0('bn_DD_2_kugi', -1)
    SFX_0('007_swing_knife_0')
    sprite('vrbnef431_002', 2)
    GFX_0('bn_DD_2_kugi', -1)
    sprite('vrbnef431_003', 2)
    GFX_0('bn_DD_2_kugi', -1)
    SFX_0('007_swing_knife_1')
    sprite('vrbnef431_004', 1)
    GFX_0('bn_DD_2_kugi', -1)
    sprite('vrbnef431_004', 1)
    SLOT_51 = (SLOT_51 + (-1))
    if (not SLOT_51):
        if (SLOT_53 < 3):
            if (SLOT_31 >= 1):
                SLOT_31 = (SLOT_31 + (-1))
                SLOT_51 = (SLOT_51 + 3)
                SLOT_53 = (SLOT_53 + 1)
    Unknown19(99, 2, 51)
    loopRest()
    gotoLabel(1)
    label(99)
    SLOT_51 = 0
    clearUponHandler(54)
    clearUponHandler(3)
    clearUponHandler(39)
    sprite('vrbnef431_001', 3)
    Unknown1019(90)
    sprite('vrbnef431_002', 3)
    Unknown1019(90)
    sprite('vrbnef431_003', 3)
    Unknown1019(90)
    sprite('vrbnef431_004', 3)
    Unknown1019(90)
    sprite('vrbnef431_001', 4)
    Unknown1019(60)
    sprite('vrbnef431_002', 4)
    sprite('vrbnef431_003', 4)
    sprite('vrbnef431_004', 4)
    sprite('vrbnef431_005', 3)
    SFX_0('019_cloth_b')
    Unknown1019(0)
    physicsYImpulse(0)
    sprite('vrbnef431_000', 3)
    label(580)
    sprite('vrbnef431_000', 10)
    GFX_Rotation(30000)
    Unknown1074(1000)
    physicsYImpulse(10000)
    setGravity(2000)
    sprite('vrbnef431_000', 30)
    Unknown3004(-12)

@State
def bn_DD_2_kugi():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown2035(1)
        GFX_SetPalette(0)
        Unknown3032()
        SlashFX(1)
        AttackLevel_(1)
        Damage(100)
        MinimumDamagePct(1)
        AttackP2(60)
        Unknown11092(1)
        Unknown23182(2)
        Unknown11001(1, 1, 1)
        Hitstop(0)
        AirPushbackX(1000)
        AirPushbackY(1000)
        PushbackX(4000)
        Unknown11056(2)
        AttackAttributes(0, 0, 0, 1, 0)
        Unknown11057(250)
        StarterRating(2)
        Unknown12052(1)
        GFX_OffsetY(80000)
        Unknown1010(-160000, 160000)
        GFX_Rotation(90000)
        Unknown1056(875)
        Unknown1064(800)
        physicsYImpulse(-48000)
        Unknown2055(180)
        zIndexInterval(0, 10)
        sendToLabelUpon(10, 1)
        sendToLabelUpon(2, 2)

        def upon_39():
            Unknown2003(1)
        if SLOT_137:
            DamageMultiplier(80)
    label(0)
    sprite('vrbnef406_000', 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrbnef406_001', 1)
    Unknown3001(255)
    Unknown3004(-4)
    Unknown1074(-15000)
    Unknown1021(30000)
    Unknown1015(-10000)
    setGravity(2400)
    sprite('vrbnef406_001', 32767)
    loopRest()
    label(2)
    clearUponHandler(10)
    clearUponHandler(2)
    sprite('null', 1)
    GFX_1('bnef_kugi_hit', -1)

@State
def bn_Warp():

    def upon_IMMEDIATE():
        Unknown4007(3)
    sprite('null', 1)
    GFX_OffsetY(180000)
    GFX_1('bnef_sp_throw_speed', -1)
    GFX_1('bnef_sp_throw_leaf', -1)
    sprite('null', 1)
    GFX_1('bnef_sp_throw_speed', -1)

@State
def bn_D_stand():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4008(3)
        GFX_SetPalette(1)
        Unknown3033()
    sprite('vrbnef203_00', 5)
    Unknown3001(0)
    Unknown3004(51)
    sprite('vrbnef203_00', 6)
    Unknown3001(255)
    Unknown3004(-42)

@State
def bn_D_stand2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4008(3)
        GFX_SetPalette(1)
        Unknown3033()
    sprite('vrbnef203_10', 2)
    sprite('vrbnef203_11', 2)
    sprite('vrbnef203_12', 3)
    sprite('vrbnef203_13', 3)

@State
def bn_D_front():

    def upon_IMMEDIATE():
        GFX_OffsetX(56000)
        Unknown4007(3)
        Unknown4010(3)
        Unknown4008(3)
        GFX_SetPalette(1)
        Unknown3033()
    sprite('vrbnef213_00', 4)
    Unknown3001(0)
    Unknown3004(42)
    sprite('vrbnef213_00', 4)
    Unknown3001(255)
    Unknown3004(-42)

@State
def bn_D_front2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4010(3)
        Unknown4008(3)
        GFX_SetPalette(1)
        Unknown3033()
    sprite('vrbnef213_10', 2)
    sprite('vrbnef213_11', 2)
    sprite('vrbnef213_12', 2)
    sprite('vrbnef213_13', 2)
    sprite('vrbnef213_14', 1)

@State
def bn_D_crouch():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4008(3)
        GFX_SetPalette(1)
        Unknown3033()
    sprite('vrbnef233_00', 6)
    Unknown3001(0)
    Unknown3004(42)
    sprite('vrbnef233_00', 6)
    Unknown3001(255)
    Unknown3004(-42)

@State
def bn_D_crouch2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4008(3)
        GFX_SetPalette(1)
        Unknown3033()
    sprite('vrbnef233_10', 3)
    sprite('vrbnef233_11', 2)
    sprite('vrbnef233_12', 2)
    sprite('vrbnef233_13', 2)
    sprite('vrbnef233_14', 2)

@State
def bn_D_jump():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4008(3)
        GFX_SetPalette(1)
        Unknown3033()
        GFX_OffsetY(4294954296)
    sprite('vrbnef253_00', 6)
    Unknown3001(0)
    Unknown3004(42)
    sprite('vrbnef253_00', 3)
    Unknown3001(255)
    Unknown3004(-42)

@State
def bn_D_jump2():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4008(3)
        GFX_SetPalette(1)
        Unknown3033()
    sprite('vrbnef253_10', 1)
    sprite('vrbnef253_11', 2)
    sprite('vrbnef253_12', 2)
    sprite('vrbnef253_13', 2)
    sprite('vrbnef253_14', 2)

@State
def bn_D_1():

    def upon_IMMEDIATE():
        Unknown23015(1)
        GFX_SetPalette(2)
    sprite('vrbnef432_50', 16)
    Unknown3032()
    Unknown2007()
    GFX_Scale(1000)
    Unknown1099(40)
    Unknown3001(255)
    Unknown3004(-21)
    Unknown4054(1)
    PFX('bnef_D_flash', 0)

@State
def bn_D_2():

    def upon_IMMEDIATE():
        Unknown23015(1)
        GFX_SetPalette(2)
    sprite('vrbnef432_51', 16)
    Unknown3032()
    Unknown2007()
    GFX_Scale(1000)
    Unknown1099(40)
    Unknown3001(255)
    Unknown3004(-21)
    Unknown4054(1)
    PFX('bnef_D_flash', 0)

@State
def bn_D_3():

    def upon_IMMEDIATE():
        Unknown23015(1)
        GFX_SetPalette(2)
    sprite('vrbnef432_52', 16)
    Unknown3032()
    Unknown2007()
    GFX_Scale(1000)
    Unknown1099(40)
    Unknown3001(255)
    Unknown3004(-21)
    Unknown4054(1)
    PFX('bnef_D_flash', 0)

@State
def bn_D_4():

    def upon_IMMEDIATE():
        Unknown23015(1)
        GFX_SetPalette(2)
    sprite('vrbnef432_53', 16)
    Unknown3032()
    Unknown2007()
    GFX_Scale(1000)
    Unknown1099(40)
    Unknown3001(255)
    Unknown3004(-21)
    Unknown4054(1)
    PFX('bnef_D_flash', 0)

@State
def bn_D_max():

    def upon_IMMEDIATE():
        Unknown23015(1)
        GFX_SetPalette(2)
        if (SLOT_23 <= 204000):
            Unknown1006(205000)
    sprite('vrbnef432_90', 16)
    Unknown3032()
    Unknown2007()
    GFX_Scale(1000)
    Unknown3001(255)
    Unknown4054(1)
    PFX('bnef_D_flash2', 0)
    sprite('vrbnef432_90', 16)
    Unknown3004(-16)

@State
def EventBN01_iblc():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 1)
        GFX_SetPalette(3)
    label(0)
    sprite('lc000_00', 5)
    sprite('lc000_01', 5)
    sprite('lc000_02', 5)
    sprite('lc000_03', 5)
    sprite('lc000_04', 5)
    sprite('lc000_05', 5)
    sprite('lc000_06', 5)
    sprite('lc000_07', 5)
    sprite('lc000_08', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('lc003_00', 2)
    Unknown2005()
    sprite('lc003_01', 2)
    sprite('lc003_02', 2)
    sprite('lc032_00', 3)
    physicsXImpulse(20000)
    sprite('lc032_01', 3)
    sprite('lc032_02', 3)
    sprite('lc032_03', 3)
    sprite('lc032_04', 3)
    Unknown8006(100, 1, 1)
    sprite('lc032_05', 3)
    sprite('lc032_06', 3)
    sprite('lc032_07', 3)
    sprite('lc032_08', 3)
    sprite('lc032_09', 3)
    sprite('lc032_10', 3)
    Unknown8006(100, 1, 1)
    sprite('lc032_11', 3)
    sprite('lc032_12', 3)

@State
def BunshinAttackObject1():

    def upon_IMMEDIATE():
        zIndexInterval(0, 50)
        GFX_0('BunshinAttackObject2', -1)
        Unknown23015(4)
        EnableAfterimage(1)
    sprite('bn022_00', 2)
    physicsYImpulse(60000)
    physicsXImpulse(-30000)
    setGravity(0)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)

@State
def BunshinAttackObject2():

    def upon_IMMEDIATE():
        Unknown2005()
        zIndexInterval(0, 50)
        Unknown23015(4)
        EnableAfterimage(1)
    sprite('bn022_00', 2)
    physicsYImpulse(60000)
    physicsXImpulse(-30000)
    setGravity(0)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)

@State
def BN433WhiteOut():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown2054(1)
        Unknown1006(900000)
        Unknown3032()
        GFX_Scale(20000)
        Unknown3001(0)
    sprite('vr_white', 20)
    Unknown3004(12)
    sprite('vr_white', 40)
    sprite('vr_white', 20)
    Unknown3004(-15)

@State
def BunshinX2():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1006(0)
        GFX_OffsetX(-228000)
        Unknown1006(880000)
        physicsYImpulse(22000)
    sprite('null', 30)
    GFX_0('BunshinAttackObject3', -1)
    GFX_0('BunshinAttackObject4', -1)
    sprite('null', 200)
    physicsYImpulse(0)

@State
def BunshinAttackObject3():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(22)
        Unknown2019(500)
        Unknown3032()
        GFX_OffsetX(-320000)
        physicsYImpulse(50000)
        setGravity(0)
        EnableAfterimage(1)
        AfterimageType(2)
        AfterimageCount(12)
    sprite('bn022_01', 1)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    YAccel(50)
    sprite('bn022_02', 4)
    YAccel(50)
    Unknown1019(50)
    SFX_0('019_cloth_a')
    sprite('bn022_03', 4)
    YAccel(50)
    Unknown1019(50)
    sprite('bn022_04', 4)
    YAccel(0)
    Unknown1019(50)
    sprite('bn022_05', 4)
    Unknown1019(0)
    sprite('bn022_06', 5)
    sprite('bn433_11', 5)
    sprite('bn433_12', 5)
    SFX_0('019_cloth_b')
    sprite('bn433_13', 5)
    sprite('bn433_14', 28)
    sprite('bn433_15', 4)
    physicsYImpulse(-35000)
    physicsXImpulse(90000)
    sprite('bn433_16', 2)
    sprite('bn433_16', 2)
    AfterimageCount(6)
    sprite('bn433_15', 4)
    sprite('bn433_16', 4)
    sprite('bn433_15', 4)

@State
def BunshinAttackObject4():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4007(2)
        Unknown4009(22)
        Unknown2019(-500)
        Unknown3032()
        GFX_OffsetX(-780000)
        physicsYImpulse(50000)
        setGravity(0)
        EnableAfterimage(1)
        AfterimageType(2)
        AfterimageCount(12)
    sprite('bn022_01', 1)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    sprite('bn022_00', 2)
    sprite('bn022_01', 2)
    YAccel(50)
    sprite('bn022_02', 4)
    YAccel(50)
    Unknown1019(50)
    SFX_0('019_cloth_c')
    sprite('bn022_03', 4)
    YAccel(50)
    Unknown1019(50)
    sprite('bn022_04', 4)
    YAccel(0)
    Unknown1019(50)
    sprite('bn022_05', 4)
    Unknown1019(0)
    sprite('bn022_06', 5)
    sprite('bn433_11', 5)
    SFX_0('019_cloth_b')
    sprite('bn433_12', 5)
    sprite('bn433_13', 5)
    sprite('bn433_14', 28)
    sprite('bn433_15', 4)
    physicsYImpulse(-35000)
    physicsXImpulse(90000)
    sprite('bn433_16', 2)
    sprite('bn433_16', 2)
    AfterimageCount(6)
    sprite('bn433_15', 4)
    sprite('bn433_16', 4)
    sprite('bn433_15', 4)

@State
def BunshinTodomeEff():

    def upon_IMMEDIATE():
        GFX_2('bnef_xatk')
        GFX_OffsetY(160000)
    sprite('null', 8)
    GFX_0('BN433WhiteOut', -1)

@State
def BunshinTodome():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(3)
        Damage(3700)
        MinimumDamagePct(25)
        AirUntechableTime(300)
        GroundUntechableTime(65)
        Hitstop(15)
        AttackP2(40)
        AirHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(1000)
        YImpluseBeforeWallbounce(1000)
        Unknown11108(3)
        StarterRating(2)
        Unknown1086(22)
        IsInvisibility(1)
    sprite('vrdmy_bunshin', 3)
    GFX_0('BunshinTodomeEff', -1)

@State
def BunshinX2OD():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1006(0)
        GFX_OffsetX(-228000)
        Unknown1006(880000)
        physicsYImpulse(22000)
    sprite('null', 30)
    GFX_0('BunshinAttackObject3OD', -1)
    GFX_0('BunshinAttackObject4OD', -1)
    sprite('null', 200)
    physicsYImpulse(0)

@State
def BunshinAttackObject3OD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(22)
        Unknown2019(500)
        Unknown3032()
        GFX_OffsetX(-320000)
        physicsYImpulse(50000)
        setGravity(0)
        EnableAfterimage(1)
        AfterimageType(2)
        AfterimageCount(12)
        Collidable(0)
    sprite('bn352_00', 2)
    physicsXImpulse(72000)
    physicsYImpulse(64000)
    sprite('bn352_01', 2)
    SFX_0('000_airdash_2')
    sprite('bn352_02', 2)
    sprite('bn352_01', 2)
    sprite('bn352_02', 2)
    sprite('bn352_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn352_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn352_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn352_03', 2)
    Unknown1019(50)
    YAccel(50)
    SFX_3('bnse_09')
    sprite('bn355_00', 2)
    Unknown2005()
    physicsXImpulse(120000)
    physicsYImpulse(-70000)
    sprite('bn355_01', 2)
    SFX_0('000_airdash_2')
    sprite('bn355_02', 2)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    SFX_3('bnse_09')
    sprite('bn358_00', 2)
    Unknown2005()
    physicsXImpulse(170000)
    physicsYImpulse(0)
    sprite('bn358_01', 2)
    SFX_0('000_airdash_2')
    sprite('bn358_02', 2)
    sprite('bn358_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn358_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn358_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn358_03', 2)
    Unknown1019(50)
    YAccel(50)
    SFX_3('bnse_09')
    sprite('bn355_00', 2)
    Unknown2005()
    physicsXImpulse(120000)
    physicsYImpulse(-40000)
    sprite('bn355_01', 2)
    SFX_0('000_airdash_2')
    sprite('bn355_02', 2)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    SFX_3('bnse_09')
    sprite('bn352_00', 2)
    Unknown2005()
    physicsXImpulse(52000)
    physicsYImpulse(35000)
    sprite('bn352_01', 2)
    SFX_0('000_airdash_2')
    sprite('bn352_02', 2)
    sprite('bn352_01', 2)
    sprite('bn352_00', 2)
    sprite('bn352_01', 2)
    sprite('bn352_02', 2)
    sprite('bn352_03', 2)
    SFX_3('bnse_09')
    sprite('bn022_00', 2)
    Unknown2005()
    physicsXImpulse(0)
    physicsYImpulse(22000)
    sprite('bn022_01', 2)
    YAccel(50)
    sprite('bn022_02', 4)
    YAccel(50)
    Unknown1019(50)
    sprite('bn022_03', 4)
    YAccel(50)
    Unknown1019(50)
    sprite('bn022_04', 4)
    YAccel(0)
    Unknown1019(50)
    sprite('bn022_05', 4)
    Unknown1019(0)
    sprite('bn022_06', 3)
    sprite('bn433_11', 3)
    sprite('bn433_12', 3)
    sprite('bn433_13', 3)
    sprite('bn433_14', 23)
    sprite('bn433_15', 4)
    physicsYImpulse(-35000)
    physicsXImpulse(90000)
    sprite('bn433_16', 2)
    sprite('bn433_16', 2)
    AfterimageCount(6)
    sprite('bn433_15', 4)
    sprite('bn433_16', 4)
    sprite('bn433_15', 4)

@State
def BunshinAttackObject4OD():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4007(2)
        Unknown4009(22)
        Unknown2019(-500)
        Unknown3032()
        GFX_OffsetX(-780000)
        physicsYImpulse(50000)
        setGravity(0)
        EnableAfterimage(1)
        AfterimageType(2)
        AfterimageCount(12)
    sprite('bn352_00', 2)
    physicsXImpulse(72000)
    physicsYImpulse(64000)
    sprite('bn352_01', 2)
    SFX_0('000_airdash_1')
    sprite('bn352_02', 2)
    sprite('bn352_01', 2)
    sprite('bn352_02', 2)
    sprite('bn352_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn352_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn352_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn352_03', 2)
    Unknown1019(50)
    YAccel(50)
    SFX_3('bnse_09')
    sprite('bn355_00', 2)
    Unknown2005()
    physicsXImpulse(120000)
    physicsYImpulse(-70000)
    sprite('bn355_01', 2)
    SFX_0('000_airdash_1')
    sprite('bn355_02', 2)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    SFX_3('bnse_09')
    sprite('bn358_00', 2)
    Unknown2005()
    physicsXImpulse(170000)
    physicsYImpulse(0)
    sprite('bn358_01', 2)
    SFX_0('000_airdash_1')
    sprite('bn358_02', 2)
    sprite('bn358_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn358_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn358_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn358_03', 2)
    Unknown1019(50)
    YAccel(50)
    SFX_3('bnse_09')
    sprite('bn355_00', 2)
    Unknown2005()
    physicsXImpulse(120000)
    physicsYImpulse(-40000)
    sprite('bn355_01', 2)
    SFX_0('000_airdash_1')
    sprite('bn355_02', 2)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    sprite('bn355_03', 2)
    Unknown1019(50)
    YAccel(50)
    SFX_3('bnse_09')
    sprite('bn352_00', 2)
    Unknown2005()
    physicsXImpulse(52000)
    physicsYImpulse(35000)
    sprite('bn352_01', 2)
    SFX_0('000_airdash_1')
    sprite('bn352_02', 2)
    sprite('bn352_01', 2)
    sprite('bn352_00', 2)
    sprite('bn352_01', 2)
    sprite('bn352_02', 2)
    sprite('bn352_03', 2)
    SFX_3('bnse_09')
    sprite('bn022_00', 2)
    Unknown2005()
    physicsXImpulse(0)
    physicsYImpulse(22000)
    sprite('bn022_01', 2)
    YAccel(50)
    sprite('bn022_02', 4)
    YAccel(50)
    Unknown1019(50)
    sprite('bn022_03', 4)
    YAccel(50)
    Unknown1019(50)
    sprite('bn022_04', 4)
    YAccel(0)
    Unknown1019(50)
    sprite('bn022_05', 4)
    Unknown1019(0)
    sprite('bn022_06', 3)
    sprite('bn433_11', 3)
    sprite('bn433_12', 3)
    sprite('bn433_13', 3)
    sprite('bn433_14', 23)
    sprite('bn433_15', 4)
    physicsYImpulse(-35000)
    physicsXImpulse(90000)
    sprite('bn433_16', 2)
    sprite('bn433_16', 2)
    AfterimageCount(6)
    sprite('bn433_15', 4)
    sprite('bn433_16', 4)
    sprite('bn433_15', 4)

@State
def BunshinTodomeOD():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(3)
        Damage(4167)
        MinimumDamagePct(25)
        AirUntechableTime(300)
        GroundUntechableTime(65)
        Hitstop(15)
        AttackP2(40)
        AirHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(1000)
        YImpluseBeforeWallbounce(1000)
        Unknown11108(3)
        Unknown1086(22)
        IsInvisibility(1)
        Unknown9001(4)
        StarterRating(2)
    sprite('vrdmy_bunshin', 3)
    GFX_0('BunshinTodomeEff', -1)

@State
def Hibashira():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4010(3)
        GFX_2('bnef_hibashira')
        GFX_0('Hibashira_front', -1)
        GFX_Rotation(10000)
        GFX_OffsetX(64000)
        Unknown1064(1500)
        Unknown1056(1500)
    sprite('null', 3)
    Unknown1064(500)
    sprite('null', 200)
    Unknown1064(1500)
    GFX_0('Terikaeshi', -1)

@State
def Hibashira_front():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4009(2)
        Unknown4006(2)
        GFX_2('bnef_hibashira_front')
        Unknown3001(200)
    sprite('null', 32767)

@State
def Hibashira_option():

    def upon_IMMEDIATE():
        Unknown4009(2)
        GFX_2('bnef_hibashira_yuka')
        Unknown1056(1250)
    sprite('null', 300)

@State
def Terikaeshi():

    def upon_IMMEDIATE():
        GFX_Scale(10000)
        Unknown3001(255)
        Unknown3004(-10)
        Unknown1006(64000)
    sprite('vref_env', 300)

@State
def LookAtPosBN433():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown20002(1)
        Unknown20003(1)
        Unknown20001(1)
        CameraControlEnable(1)
    sprite('null', 32767)

@State
def __434TRetrunKugi():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_SetPalette(0)
        Unknown4007(22)
        Unknown4009(2)
        GFX_OffsetY(340000)
        GFX_Rotation(-180000)
    sprite('vrbnef434_kugi00', 12)
    physicsYImpulse(-15000)
    Unknown1074(-28000)

@State
def __434ThrowKubi():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_SetPalette(0)
        Unknown4007(22)
        Unknown4009(2)
        GFX_OffsetY(4294727296)
        Unknown2019(500)
    sprite('vrbnef434_kugi00', 12)
    sprite('vrbnef434_kugi01', 29)
    GFX_OffsetY(4294732296)
    sprite('vrbnef434_kugi01', 20)
    IsInvisibility(1)
    sprite('vrbnef434_kugi01', 70)
    IsInvisibility(0)
    sprite('vrbnef434_kugi01', 21)
    physicsYImpulse(30000)
    physicsXImpulse(-5000)
    Unknown1074(-10000)

@State
def __434PowNacEfff():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('bnef_434pownac_add')
        sendToLabelUpon(32, 0)
        Unknown2054(1)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __434rock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ef_rock', '')
        GFX_Scale(1200)
        GFX_OffsetY(150000)
        Unknown1086(22)
        Unknown2054(1)
        Unknown21010(1)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __434HitImpact():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ef_hitfire', '')
        GFX_Scale(1200)
        GFX_OffsetY(4294817296)
        Unknown3001(0)
        Unknown2054(1)
        Unknown21010(1)
        Unknown4010(2)
    sprite('null', 5)
    PFX_Rotation(180000)
    PFX('bnef_434atk00_smoke', -1)
    sprite('null', 5)
    GFX_1('bnef_434lstatk_pos', -1)
    Unknown4009(2)
    Unknown2054(0)
    Unknown3001(255)
    sprite('null', 35)
    sprite('null', 14)
    Unknown3004(-26)

@State
def bn_AH_fusuma_r():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown6001(1)
        Unknown2008()
        Unknown1000(640000)
        Unknown1006(640000)
        Unknown2019(-100)
        GFX_SetPalette(4)
    sprite('vrbnef450_00', 8)
    Unknown1056(-2000)
    Unknown1064(2000)
    physicsYImpulse(-128000)
    sprite('vrbnef450_00', 30)
    ScreenShake(0, 16000)
    physicsYImpulse(0)
    sprite('vrbnef450_00', 16)
    Unknown1059(-93)
    Unknown1067(93)
    physicsXImpulse(48000)

@State
def bn_AH_fusuma_l():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown6001(1)
        Unknown2008()
        Unknown1056(-1000)
        Unknown1000(640000)
        Unknown1006(640000)
        Unknown2019(-100)
        GFX_SetPalette(4)
    sprite('vrbnef450_00', 8)
    Unknown1056(2000)
    Unknown1064(2000)
    physicsYImpulse(-128000)
    sprite('vrbnef450_00', 30)
    physicsYImpulse(0)
    ScreenShake(0, 16000)
    sprite('vrbnef450_00', 16)
    Unknown1059(93)
    Unknown1067(93)
    physicsXImpulse(-48000)

@State
def bn_AH_fusuma_r_open():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown6001(1)
        Unknown2008()
        Unknown2019(0)
        Unknown1000(640000)
        Unknown1006(-384000)
        GFX_SetPalette(4)
    sprite('vrbnef450_00', 16)
    Unknown1056(-1500)
    Unknown1064(1500)
    Unknown1059(-93)
    Unknown1067(93)
    sprite('vrbnef450_00', 16)
    Unknown2019(-100)
    physicsXImpulse(48000)

@State
def bn_AH_fusuma_l_open():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown6001(1)
        Unknown2008()
        Unknown2019(0)
        Unknown1000(640000)
        Unknown1006(-384000)
        GFX_SetPalette(4)
    sprite('vrbnef450_00', 16)
    Unknown1056(1500)
    Unknown1064(1500)
    Unknown1059(93)
    Unknown1067(93)
    sprite('vrbnef450_00', 16)
    Unknown2019(-100)
    physicsXImpulse(-48000)

@State
def bn_AH_faceup():

    def upon_IMMEDIATE():
        sendToLabelUpon(17, 1)
        if SLOT_43:
            loopRelated(17, 70)
            Unknown2055(110)
        else:
            loopRelated(17, 200)
            Unknown2055(240)
        Unknown23015(11)
        Unknown2035(1)
        Unknown6001(1)
        Unknown2007()
        GFX_SetPalette(2)
        GFX_Scale(1050)
        Unknown1000(-640000)
        Unknown1006(-384000)
    GFX_0('bn_AH_ray2', -1)
    label(0)
    sprite('vrbnef450_face00', 2)
    sprite('vrbnef450_face01', 2)
    sprite('vrbnef450_face02', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    GFX_0('AstFaceCutinWhiteOut', -1)
    label(2)
    sprite('vrbnef450_face01', 2)
    sprite('vrbnef450_face02', 2)
    sprite('vrbnef450_face00', 2)
    loopRest()
    gotoLabel(2)

@State
def AstFaceCutinWhiteOut():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
        Unknown4010(2)
        Unknown23015(4)
        Unknown3033()
        Unknown3001(0)
        GFX_Scale(20000)
    sprite('vr_white', 25)
    Unknown3004(10)
    sprite('vr_white', 32767)

@State
def bn_AH_kugi():

    def upon_IMMEDIATE():
        Unknown2035(1)
        GFX_SetPalette(0)
        GFX_OffsetX(-16000)
        GFX_OffsetY(216000)
    sprite('vrbnef450_kugi', 60)

@State
def bn_AH_kugi2():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown4007(2)
        GFX_SetPalette(0)
    sprite('vrbnef450_kugi', 120)

@State
def bn_AH_Thunder():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown6001(1)
        Unknown2007()
        GFX_SetPalette(5)
        Unknown3033()
        Unknown2019(4000)
        Unknown1000(-1280000)
        Unknown1006(-360000)
        GFX_Scale(3000)
        Unknown1067(-100)
    sprite('vrbnef450_90', 2)
    SFX_0('015_blaze_2')
    SFX_0('006_swing_blade_2')
    SFX_0('010_swing_sword_2')
    SFX_0('006_swing_blade_1')
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    GFX_Scale(0)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)
    sprite('vrbnef450_90', 2)
    sprite('vrbnef450_91', 2)

@State
def bn_AH_bomber():

    def upon_IMMEDIATE():
        Unknown23032(80)
    sprite('null', 1)
    PFX_Scale(2000)
    PFX('bnef_astbomber', -1)
    ScreenShake(0, 16000)
    SFX_0('016_explode_2')
    SFX_0('015_blaze_2')
    sprite('null', 1)
    PFX_Scale(1500)
    PFX('bnef_astbomber', -1)
    sprite('null', 1)
    PFX_Scale(2000)
    PFX('bnef_astbomber', -1)

@State
def bn_AH_UnderFire():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(3)
        GFX_OffsetY(240000)
        Unknown23067('bnef_ast_groundfire')
    sprite('null', 32767)

@State
def bn_AH_ray():

    def upon_IMMEDIATE():
        Unknown23032(50)
        Unknown1006(308000)
        Unknown4054(4)
        Unknown23067('ef_speedline_wt')
    sprite('null', 120)

@State
def bn_AH_ray2():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4007(2)
        Unknown4008(2)
        Unknown23032(50)
        GFX_OffsetX(1790000)
        Unknown1006(580000)
        GFX_Scale(1250)
        Unknown4054(4)
        Unknown23067('ef_speedline_bk')
    sprite('null', 60)

@State
def bn_AH_HandFire():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown2055(30)
        Unknown4007(2)
        Unknown23067('bnef_ast_handfire')
    sprite('null', 1)

@State
def AstStartBlackOut():

    def upon_IMMEDIATE():
        Unknown23032(50)
        Unknown1006(256000)
        Unknown2019(500)
        Unknown3032()
        Unknown3001(0)
        Unknown1056(5000)
        Unknown1064(1500)
        Unknown3026(4278190080)
    sprite('vr_white', 10)
    sprite('vr_white', 20)
    Unknown3004(13)
    sprite('vr_white', 128)
    sprite('vr_white', 30)
    Unknown3004(-9)

@State
def AstStartWhiteOut():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
        Unknown3033()
        Unknown3001(0)
        GFX_Scale(20000)
    sprite('vr_white', 20)
    Unknown3004(15)
    sprite('vr_white', 45)
    sprite('vr_white', 20)
    Unknown3001(200)
    Unknown3004(-10)

@State
def AstWhiteOut():

    def upon_IMMEDIATE():
        Unknown1000(0)
        Unknown1006(2048000)
        Unknown2019(5)
        Unknown3033()
        Unknown3001(255)
        GFX_Scale(20000)
    sprite('vr_white', 15)
    sprite('vr_white', 20)
    Unknown3001(200)
    Unknown3004(-10)

@State
def AstFinishWhiteOut():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown23032(50)
        Unknown1006(256000)
        Unknown2019(-1000)
        Unknown3033()
        Unknown3001(255)
        Unknown1056(5000)
        Unknown1064(1500)
    sprite('vr_white', 90)
    sprite('vr_white', 30)
    Unknown3004(-9)

@State
def AstFinishAtk():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown2055(100)
        Unknown1000(-6400000)
        Unknown23118(0)
        Unknown23117(16777215, 100)
        EnableAfterimage(0)
        AfterimageType(2)
        Unknown3070(2)
        AfterimageCount(8)
        AfterimageMask_1(0, 255, 0, 0)
        AfterimageMask_2(0, 0, 0, 0)
        AfterimageSize_1(1010)
        AfterimageSize_2(1100)
    sprite('bn450_13', 4)
    GFX_0('LookAtPosAtk', -1)
    sprite('bn450_14', 4)
    SFX_0('000_airdash_2')
    label(0)
    physicsXImpulse(64000)
    EnableAfterimage(1)
    sprite('bn450_17', 1)
    GFX_0('bn_AH_HandFire', 1)
    PFX_Scale(2000)
    PFX('bnef_ast_handfire', 2)
    ScreenShake(0, 5000)
    SFX_0('015_blaze_0')
    SFX_0('015_blaze_1')
    SFX_0('016_explode_0')
    sprite('bn450_17', 1)
    GFX_0('bn_AH_HandFire', 1)
    PFX_Scale(2000)
    PFX('bnef_ast_handfire', 2)
    sprite('bn450_16', 1)
    GFX_0('bn_AH_HandFire', 1)
    PFX_Scale(2000)
    PFX('bnef_ast_handfire', 2)
    sprite('bn450_16', 1)
    GFX_0('bn_AH_HandFire', 1)
    PFX_Scale(2000)
    PFX('bnef_ast_handfire', 2)
    loopRest()
    gotoLabel(0)

@State
def LookAtPosAtk():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown20002(1)
        Unknown20003(1)
        Unknown20001(1)
        CameraControlEnable(1)
        Unknown20005(40, 150)
        GFX_OffsetX(512000)
        GFX_OffsetY(220000)
    sprite('null', 40)

@State
def LookAtPos():

    def upon_IMMEDIATE():
        Unknown20001(1)
        CameraControlEnable(1)
        Unknown20004(1)
        Unknown1000(0)
        Unknown1006(0)
    sprite('null', 32767)

@State
def RLAstLockmc():

    def upon_IMMEDIATE():
        IsInvisibility(1)
        Unknown4054(5)
        Unknown23067('rlef_ashlock_mc')
        Unknown4010(3)
    sprite('null', 120)
    Unknown3001(0)
    Unknown3004(2)
    sprite('null', 32767)
    Unknown3004(0)

@State
def RLAstLockAura():

    def upon_IMMEDIATE():
        IsInvisibility(1)
        Unknown23067('rlef_ashlock_aura')
        Unknown4010(3)
    sprite('null', 120)
    Unknown3001(0)
    Unknown3004(2)
    sprite('null', 32767)
    Unknown3004(0)

@State
def BurstDD_Matome():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown48(23, 2, 51, 3, 2, 51)
        Unknown2037(2)
    if SLOT_51:
        _gotolabel(1)
    label(0)
    sprite('null', 5)
    GFX_0('BurstDD_Shot', 0)
    Unknown21007(1, 32)
    sprite('null', 5)
    GFX_0('BurstDD_Shot', 0)
    Unknown21007(1, 33)
    sprite('null', 5)
    GFX_0('BurstDD_Shot', 0)
    Unknown21007(1, 34)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    Unknown2037(2)
    label(2)
    sprite('null', 5)
    Unknown2038(-1)
    GFX_0('BurstDD_Shot', 0)
    Unknown21007(1, 32)
    sprite('null', 5)
    GFX_0('BurstDD_Shot', 0)
    Unknown21007(1, 33)
    sprite('null', 5)
    GFX_0('BurstDD_Shot', 0)
    Unknown21007(1, 34)
    loopRest()
    if SLOT_2:
        _gotolabel(2)
    sprite('null', 1)
    Unknown2037(2)
    label(3)
    sprite('null', 3)
    Unknown2038(-1)
    GFX_0('BurstDD_Shot', 0)
    Unknown21007(1, 32)
    sprite('null', 3)
    GFX_0('BurstDD_Shot', 0)
    Unknown21007(1, 33)
    sprite('null', 3)
    GFX_0('BurstDD_Shot', 0)
    Unknown21007(1, 34)
    loopRest()
    if SLOT_2:
        _gotolabel(3)
    label(4)
    sprite('null', 2)
    GFX_0('BurstDD_Shot', 0)
    Unknown21007(1, 32)
    sprite('null', 2)
    GFX_0('BurstDD_Shot', 0)
    Unknown21007(1, 33)
    sprite('null', 2)
    GFX_0('BurstDD_Shot', 0)
    Unknown21007(1, 34)
    loopRest()
    gotoLabel(4)

@State
def BurstDD_Shot():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(3)
        Damage(50)
        MinimumDamagePct(10)
        AttackP2(100)
        ChipPercentage(0)
        HeatGainMultiplier(0)
        Hitstop(0)
        PushbackX(1000)
        hitstun(60)
        StunLength(100)
        StunRecoveryLength(100)
        GroundUntechableTime(100)
        SlashFX(1)
        Unknown11057(400)
        Unknown11084(1)
        Unknown11064(1)
        Unknown23182(2)
        Unknown11108(3)
        Unknown11069('BurstDD_Shot')
        Unknown11066(1)
        Unknown2055(120)
        ScreenShake(4000, 4000)
        Unknown4010(3)
        if random_(2, 0, 16):
            Unknown1011(70000, 90000)
            GFX_Rotation(356000)
            GroundedHitstunAnimation(5)
            AirHitstunAnimation(5)
        elif random_(2, 0, 20):
            Unknown1011(100000, 120000)
            GFX_Rotation(356000)
            GroundedHitstunAnimation(5)
            AirHitstunAnimation(5)
        elif random_(2, 0, 25):
            Unknown1011(150000, 170000)
            GFX_Rotation(0)
            GroundedHitstunAnimation(5)
            AirHitstunAnimation(5)
        elif random_(2, 0, 33):
            Unknown1011(200000, 220000)
            GFX_Rotation(0)
            GroundedHitstunAnimation(4)
            AirHitstunAnimation(4)
        elif random_(2, 0, 50):
            Unknown1011(250000, 270000)
            GFX_Rotation(4000)
            GroundedHitstunAnimation(4)
            AirHitstunAnimation(4)
        else:
            Unknown1011(300000, 320000)
            GFX_Rotation(4000)
            GroundedHitstunAnimation(4)
            AirHitstunAnimation(4)
        Unknown1110(50000, 0)
        Unknown1025(10000, 20000)
        FireBall(1, 1, 1, 0, 0, 0, 0, 0)
        sendToLabelUpon(54, 9)

        def upon_32():
            EnableAfterimage(1)
            AfterimageCount(6)
            sendToLabel(0)

        def upon_33():
            EnableAfterimage(1)
            AfterimageCount(3)
            sendToLabel(1)

        def upon_34():
            EnableAfterimage(1)
            AfterimageCount(6)
            sendToLabel(2)

        def upon_36():
            clearUponHandler(54)
            clearUponHandler(12)
            Damage(1500)
            Unknown9001(4)
            Unknown11001(6, 6, 6)
            GroundedHitstunAnimation(18)
            AirHitstunAnimation(18)
            AirUntechableTime(300)
            GroundUntechableTime(10)
            AirPushbackX(0)
            Unknown11064(0)
            SlashFX(0)
            FireFX(1)
            Unknown11057(1000)
            IsInvisibility(1)
            endMomentum(1)
            Unknown1086(22)
            Unknown1006(0)
            sendToLabel(3)

        def upon_37():
            Damage(3300)
            GroundUntechableTime(30)
            AirPushbackY(80000)
            Unknown2037(1)

        def upon_12():
            SLOT_8 = (SLOT_8 + (-1))
            if (SLOT_8 <= 0):
                clearUponHandler(12)
                GroundedHitstunAnimation(2)
                AirHitstunAnimation(2)
                Unknown21012('BurstDDAdd', 34)

        def upon_3():
            if (SLOT_8 <= (-1)):
                clearUponHandler(3)
                Unknown23027()
    sprite('null', 1)
    label(0)
    sprite('vrbnef440_00', 2)
    sprite('vrbnef440_01', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrbnef440_10', 32767)
    loopRest()
    label(2)
    sprite('vrbnef440_20', 32767)
    loopRest()
    label(3)
    sprite('vrbnef440_30', 3)
    SFX_0('016_explode_2')
    SFX_0('015_blaze_2')
    sprite('vrbnef440_30', 3)
    RefreshMultihit()
    SFX_0('016_explode_2')
    SFX_0('015_blaze_2')
    Unknown23011(1)
    sprite('vrbnef440_30', 3)
    if SLOT_2:
        SFX_0('016_explode_2')
        SFX_0('015_blaze_2')
        Unknown23011(1)
    sprite('vrbnef440_30', 3)
    if SLOT_2:
        SFX_0('016_explode_2')
        SFX_0('015_blaze_2')
        Unknown23011(1)
    ExitState()
    label(9)
    clearUponHandler(10)
    sprite('keep', 12)
    Unknown3032()
    Unknown3004(-20)

@State
def BurstDD_Camera():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        Unknown20003(1)
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4007(3)
        Unknown4008(3)
        GFX_OffsetX(230000)
    sprite('null', 15)
    sprite('null', 32767)
    Unknown4007(0)

@State
def BurstDD_syuriken():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        EnableAfterimage(1)
        AfterimageCount(6)
    label(0)
    sprite('vrbnef440_00', 2)
    sprite('vrbnef440_01', 2)
    gotoLabel(0)

@State
def BurstDD_kunai():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        EnableAfterimage(1)
        AfterimageCount(3)
    sprite('vrbnef440_10', 32767)

@State
def BurstDD_kugi():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        EnableAfterimage(1)
        AfterimageCount(6)
    sprite('vrbnef440_20', 32767)

@State
def BurstDD_bomb():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        EnableAfterimage(1)
        AfterimageCount(6)
        GFX_SetPalette(4)
        Unknown23027()

        def upon_32():
            Unknown1025(8000, 9000)
            Unknown1026(27000, 28000)
            Unknown1041(1200, 1300)

        def upon_33():
            GFX_Rotation(315000)
            Unknown1025(5000, 6000)
            Unknown1026(24000, 25000)
            Unknown1041(1100, 1200)

        def upon_34():
            GFX_Rotation(280000)
            Unknown1025(5000, 6000)
            Unknown1026(30000, 31000)
            Unknown1041(1300, 1400)

        def upon_35():
            GFX_Rotation(30000)
            Unknown1025(4000, 5000)
            Unknown1026(33000, 35000)
            Unknown1041(1400, 1500)

        def upon_3():
            if (SLOT_23 <= 40000):
                clearUponHandler(3)
                endMomentum(1)
                Unknown1006(40000)
    sprite('vrbnef440_30', 1)
    sprite('vrbnef440_30', 32767)
    GFX_0('BurstDDSpark', 0)

@State
def BurstDDSpark():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        GFX_2('bnef_440spark00')
    sprite('null', 32767)

@State
def BurstDDKaton():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ef_440fire00_BN', '')
        Unknown1086(22)
        Unknown1056(100)
        Unknown1088(100)
        IsInvisibility(1)
        sendToLabelUpon(32, 0)
    sprite('vrbnef440_firepos', 2)
    GFX_1('bnef_434atk00_hasira00', -1)
    Unknown1059(90)
    Unknown1091(90)
    ScreenShake(10000, 10000)
    sprite('vrbnef440_firepos', 2)
    ScreenShake(10000, 10000)
    sprite('vrbnef440_firepos', 2)
    ScreenShake(10000, 10000)
    sprite('vrbnef440_firepos', 2)
    ScreenShake(10000, 10000)
    sprite('vrbnef440_firepos', 7)
    GFX_0('BurstDDKatonSubMato', -1)
    sprite('vrbnef440_firepos', 32767)
    Unknown1059(0)
    Unknown1091(0)
    label(0)
    sprite('vrbnef440_firepos', 10)
    Unknown3004(-26)
    Unknown1059(-45)
    Unknown1067(85)
    Unknown1091(-45)
    Unknown21012('BurstDDKatonSubMato', 32)

@State
def BurstDDKatonSubMato():

    def upon_IMMEDIATE():
        IsInvisibility(1)
        Unknown4010(2)
        sendToLabelUpon(32, 1)
        GFX_2('bnef_440_gbloom')
    label(0)
    sprite('vrbnef440_firepos', 2)
    GFX_1('bnef_440katon', 7)
    sprite('vrbnef440_firepos', 2)
    GFX_1('bnef_440katon', 0)
    sprite('vrbnef440_firepos', 2)
    GFX_1('bnef_440katon', 1)
    sprite('vrbnef440_firepos', 2)
    GFX_1('bnef_440katon', 2)
    sprite('vrbnef440_firepos', 2)
    GFX_1('bnef_440katon', 3)
    sprite('vrbnef440_firepos', 2)
    GFX_1('bnef_440katon', 4)
    sprite('vrbnef440_firepos', 2)
    GFX_1('bnef_440katon', 5)
    sprite('vrbnef440_firepos', 2)
    GFX_1('bnef_440katon', 6)
    gotoLabel(0)
    label(1)
    sprite('vrbnef440_firepos', 10)
    Unknown3004(-26)
    Unknown1099(300)

@State
def BurstDDBomb():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1086(22)
        Unknown1099(18)
        Unknown1056(1500)
        Unknown1064(1000)
    sprite('null', 4)
    GFX_0('BurstDDBombsub2', -1)
    ScreenShake(10000, 10000)
    sprite('null', 4)
    GFX_0('BurstDDBombsub', -1)
    ScreenShake(10000, 10000)

@State
def BurstDDBombEX():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1086(22)
        Unknown1056(2200)
        Unknown1064(1800)
    sprite('null', 4)
    GFX_0('BurstDDBombsub2', -1)
    ScreenShake(20000, 20000)
    sprite('null', 4)
    GFX_0('BurstDDBombsub', -1)
    ScreenShake(20000, 20000)

@State
def BurstDDBombsub2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ef_440bomb00_BN', '')
        Unknown4009(2)
        Unknown4013(2)
    sprite('null', 4)
    sprite('null', 20)
    Unknown3004(-13)

@State
def BurstDDBombsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ef_440bomb00_BN', '')
        Unknown4009(2)
        Unknown4013(2)
    sprite('null', 11)
    GFX_1('bnef_434atk00_impact01', -1)
    GFX_1('bnef_440_ray', -1)
    sprite('null', 10)
    GFX_1('bnef_440bomb', -1)

@State
def bnef_411_atk():

    def upon_IMMEDIATE():
        ProjectileDisapperOnHit(3)
        Unknown2010()
        AttackLevel_(5)
        Damage(1000)
        AttackP1(70)
        AirUntechableTime(80)
        Hitstop(2)
        Unknown11001(13, 13, 21)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(2000)
        AirPushbackY(35000)
        YImpluseBeforeWallbounce(1400)
        PushbackX(12000)
        FireFX(1)
        FatalCounter(1)
        StarterRating(2)
        Unknown12052(1)
        GFX_Scale(1500)
        Unknown11050(4, '')
    sprite('vrbnef411_atk', 3)
    Unknown23027()
    GFX_0('bnef_411_bomber', -1)
    GFX_0('bnef_411_cloth', -1)
    SFX_0('016_explode_2')
    ScreenShake(5000, 20000)
    sprite('vrbnef411_atk', 12)
    RefreshMultihit()

@State
def bnef_411_bomber():

    def upon_IMMEDIATE():
        ProjectileDisapperOnHit(3)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4054(6)
        Unknown23067('bnef_411bomber')
    sprite('null', 80)

@State
def bnef_411_cloth():

    def upon_IMMEDIATE():
        GFX_SetPalette(0)
        Unknown3032()
        Unknown2035(1)
        Unknown23015(7)
    sprite('vrbnef411_00', 4)
    sprite('vrbnef411_01', 4)
    sprite('vrbnef411_02', 2)
    sprite('vrbnef411_02', 2)
    Unknown4047(12, 12, 12)
    PFX('bnef_411_cloth_pos', -1)
    sprite('vrbnef411_03', 4)
    sprite('vrbnef411_04', 2)
    sprite('vrbnef411_04', 2)
    Unknown4047(12, 12, 12)
    PFX('bnef_411_cloth_pos', -1)

@State
def EventBNvsTBStandLC():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 1)
        GFX_SetPalette(3)
        Unknown2019(500)
    sprite('lc000_00', 5)
    label(0)
    sprite('lc000_01', 5)
    sprite('lc000_02', 5)
    sprite('lc000_03', 5)
    sprite('lc000_04', 5)
    sprite('lc000_05', 5)
    sprite('lc000_06', 5)
    sprite('lc000_07', 5)
    sprite('lc000_08', 5)
    sprite('lc000_00', 5)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('lc033_00', 1)
    sprite('lc033_00', 2)
    physicsXImpulse(-24000)
    physicsYImpulse(18000)
    Unknown8001(3, 0)
    sprite('lc033_01', 2)
    sprite('lc033_02', 3)
    setGravity(850)
    sprite('lc033_03', 3)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    label(1)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    sprite('lc033_02', 3)
    sprite('lc033_03', 3)
    loopRest()

@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    SFX_0('019_quake_0')
    loopRest()
    gotoLabel(0)

@State
def Event_Headache():

    def upon_IMMEDIATE():
        Unknown1086(3)
        GFX_OffsetY(360000)
    sprite('null', 1)
    SFX_0('014_electric_ll')
    PFX_Scale(500)
    PFX('ef_hits', -1)

@State
def Event_Kuginasi():
    sprite('null', 3)
    Unknown2019(500)
    sprite('bn063_11ex', 32767)

@State
def Act2Event_CreatePT():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        sendToLabelUpon(34, 3)
        GFX_OffsetX(-100000)
        Unknown30012(0)
    label(0)
    sprite('pt000_00', 7)
    sprite('pt000_01', 7)
    sprite('pt000_02', 7)
    sprite('pt000_03', 7)
    sprite('pt000_04', 7)
    sprite('pt000_05', 7)
    sprite('pt000_06', 7)
    sprite('pt000_07', 7)
    sprite('pt000_08', 7)
    sprite('pt000_09', 7)
    sprite('pt000_10', 7)
    sprite('pt000_11', 7)
    sprite('pt000_12', 7)
    sprite('pt000_13', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('pt200_00', 2)
    sprite('pt200_01', 3)
    SFX_0('003_swing_grap_0_0')
    sprite('pt200_02', 16)
    GFX_1('ef_exhit_sub', 0)
    SFX_0('100_hit_grap_0')
    ScreenShake(4000, 6000)
    sprite('pt200_02', 2)
    Unknown21007(2, 35)
    sprite('pt200_03', 3)
    sprite('pt200_04', 4)
    sprite('pt200_05', 4)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('pt003_00', 3)
    Unknown2005()
    sprite('pt003_01', 3)
    sprite('pt003_02', 3)
    loopRest()
    gotoLabel(0)
    label(3)
    sprite('pt032_02', 4)
    physicsXImpulse(-26200)
    Unknown2005()
    SFX_0('000_airdash_1')
    sprite('pt032_03', 4)
    Unknown8006(100, 1, 1)
    sprite('pt032_04', 4)
    sprite('pt032_05', 4)
    sprite('pt032_06', 4)
    loopRest()

@State
def Act2Event_PTCamera():
    sprite('null', 32767)
    CameraControlEnable(1)
    sendToLabelUpon(32, 1)
    GFX_OffsetX(-200000)
    loopRest()
    label(1)
    sprite('null', 20)

@State
def Act3Event_TeniObj():

    def upon_IMMEDIATE():
        GFX_OffsetY(100000)
    sprite('null', 80)
    GFX_1('story_teni', 100)
    SFX_0('000_airdash_2')
    SFX_0('022_magiccircle_b')
    sprite('null', 3)
    GFX_1('haef_event_lose_end', 103)
    loopRest()