@State
def EMB():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(300000)
        Unknown2054(1)
        IsInvisibility(1)
        Unknown4003('ef_emb_BL.DIG', '')
        Unknown23015(5)
        GFX_Scale(1200)
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
def EMB_BL_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(300000)
        Unknown2054(1)
        IsInvisibility(1)
        Unknown4003('ef_emb_BL.DIG', '')
        Unknown23015(5)
        GFX_Scale(1200)
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
def EMB_BL_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(300000)
        Unknown2054(1)
        Unknown4003('ef_emb_BL.DIG', '')
        Unknown23015(5)
        GFX_Scale(1200)
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
def BLEF_LockOnZone():

    def upon_IMMEDIATE():
        GFX_OffsetY(300000)
        Unknown4003('blef_circle.DIG', '')
        Unknown2054(1)
        Unknown3033()
        Unknown23023()
        Unknown2037(0)
        Unknown48(23, 2, 51, 3, 2, 23)
        if SLOT_51:
            SLOT_4 = 1000
        else:
            SLOT_4 = 1800

        def upon_3():
            if SLOT_2:
                if SLOT_51:
                    SLOT_4 = (SLOT_4 + 8)
                else:
                    SLOT_4 = (SLOT_4 + 11)
                Unknown23030('BulletLockOnZone', 2, 4, 0, 0, 0, 0, 0, 0)

        def upon_44():
            clearUponHandler(44)
            clearUponHandler(32)
            sendToLabel(2)

        def upon_32():
            clearUponHandler(44)
            clearUponHandler(32)
            sendToLabel(2)
        Unknown23151(3, 103)
        Unknown23144(3, 0, 103, 0, 0, 0, 0, 0, 50, 0, 20)
    if SLOT_51:
        sendToLabel(100)
    sprite('null', 5)
    GFX_Scale(0)
    Unknown3001(0)
    Unknown3004(60)
    Unknown1099(360)
    sprite('null', 1)
    SFX_3('blse_01')
    Unknown3004(0)
    GFX_Scale(1800)
    Unknown1099(0)
    gotoLabel(0)
    label(100)
    sprite('null', 5)
    GFX_Scale(0)
    Unknown3001(0)
    Unknown3004(60)
    Unknown1099(200)
    sprite('null', 1)
    SFX_3('blse_01')
    Unknown3004(0)
    GFX_Scale(1000)
    Unknown1099(0)
    gotoLabel(0)
    label(0)
    sprite('null', 10)
    Unknown2037(1)
    physicsYImpulse(-300)
    sprite('null', 30)
    physicsYImpulse(-200)
    sprite('null', 30)
    physicsYImpulse(-100)
    sprite('null', 10)
    YAccel(0)
    sprite('null', 10)
    physicsYImpulse(300)
    sprite('null', 30)
    physicsYImpulse(200)
    sprite('null', 30)
    physicsYImpulse(100)
    sprite('null', 10)
    YAccel(0)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('null', 10)
    Unknown2037(0)
    Unknown1099(0)
    Unknown3004(-26)

@State
def BLEF_LockOnMarker():

    def upon_IMMEDIATE():
        GFX_SetPalette(2)
        Unknown3033()
        GFX_Scale(500)
        Unknown1074(-1500)
        Unknown2019(-500)
        Unknown1086(22)
        GFX_OffsetY(200000)
        sendToLabelUpon(32, 10)
        sendToLabelUpon(33, 20)

        def upon_16():
            Unknown2071(22, 0, 0, 60, 1)
    label(0)
    sprite('blef_target', 32767)
    Unknown1099(0)
    label(10)
    sprite('blef_target', 5)
    clearUponHandler(32)
    Unknown1099(60)
    Unknown3013(31)
    sprite('blef_target', 10)
    SFX_3('blse_02')
    Unknown1099(-35)
    gotoLabel(0)
    label(20)
    sprite('blef_target', 16)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(16)
    Unknown1099(200)
    Unknown3004(-16)

@State
def blef405Atk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        AttackP2(72)
        SameMoveProration(10)
        FireFX(1)
        Unknown11068(0)
        AirUntechableTime(17)
        hitstun(17)
        Unknown11050(5, '')
        if (SLOT_5 == 1):
            AttackLevel_(4)
            Damage(1500)
            AttackP2(72)
            Hitstop(10)
            AirUntechableTime(35)
            WallstickLength(28)
            AirHitstunAfterWallbounce(45)
            AirPushbackX(40000)
            AirPushbackY(30000)
            AirHitstunAnimation(13)
            GroundedHitstunAnimation(13)
            Wallbounce(1)
            WallbounceReboundTime(5)
            Wallstick(1)

            def upon_12():
                ScreenShake(15000, 15000)
                SFX_0('100_hit_grap_3')
                SFX_3('blse_05')
        if (SLOT_5 == 2):
            AttackLevel_(5)
            Damage(3350)
            AttackP2(74)
            Hitstop(15)
            AirUntechableTime(40)
            WallstickLength(45)
            AirHitstunAfterWallbounce(45)
            AirPushbackX(50000)
            AirPushbackY(31250)
            AirHitstunAnimation(19)
            GroundedHitstunAnimation(19)
            Wallbounce(1)
            WallbounceReboundTime(4)
            Wallstick(1)
            if SLOT_110:
                WallbounceReboundTime(40)

            def upon_12():
                ScreenShake(30000, 0)
                SFX_0('100_hit_grap_3')
                SFX_3('blse_06')

        def upon_32():
            GFX_OffsetX(330000)
            GFX_OffsetY(250000)
    sprite('vrblef405_test', 3)

@State
def __202_Blast00():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 60)
    GFX_2('blef_5C_start')

@State
def __202_Blast01():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 60)
    GFX_2('blef_5C')
    GFX_1('blef_5C_add', 100)

@State
def shot_charge():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 64)
    GFX_2('blef_charge')

@State
def shot_fire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_SetPalette(1)
        Unknown3033()
        GFX_OffsetX(272000)
    sprite('vrblef401_00', 2)
    GFX_1('blef_shot_blast', 0)
    sprite('vrblef401_01', 2)
    sprite('vrblef401_02', 2)
    sprite('vrblef401_03', 2)
    sprite('vrblef401_04', 2)

@State
def shot_mazzle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_Rotation(135000)
    sprite('null', 60)
    GFX_2('blef_shot_mazzle')

@State
def shot():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        AttackLevel_(3)
        Damage(700)
        AttackP1(80)
        Unknown11092(1)
        SameMoveProration(10)
        Hitstop(2)
        Unknown11001(6, 6, 8)
        Unknown11056(2)
        FireFX(1)
        AirUntechableTime(25)
        hitstun(22)
        Unknown53(1)
        StarterRating(2)
        Unknown3033()
        GFX_SetPalette(1)
        Unknown2019(-500)
        GFX_OffsetX(64000)
        GFX_Scale(1500)
        physicsXImpulse(18000)
        Unknown2037(8)
        SLOT_51 = 1

        def upon_32():
            AirPushbackY(25000)
            Unknown11001(5, 4, 6)
            SLOT_51 = 2
            clearUponHandler(32)

        def upon_33():
            AirPushbackY(24000)
            Unknown11001(3, 2, 4)
            SLOT_51 = 3
            clearUponHandler(33)

        def upon_ON_HIT_OR_BLOCK():
            if (SLOT_52 >= 1):
                Damage(350)
            SLOT_52 = (SLOT_52 + 1)
            Unknown1019(75)
            SLOT_51 = (SLOT_51 + (-1))
            if (SLOT_51 <= 0):
                clearUponHandler(10)
                Unknown2037(0)
                physicsXImpulse(13000)
                sendToLabel(1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('null', 5)
    GFX_0('shot_add', -1)
    label(0)
    sprite('vrblef401_10', 2)
    RefreshMultihit()
    SFX_3('blse_08')
    sprite('vrblef401_11', 2)
    RefreshMultihit()
    sprite('vrblef401_12', 2)
    RefreshMultihit()
    sprite('vrblef401_13', 2)
    RefreshMultihit()
    sprite('vrblef401_14', 2)
    RefreshMultihit()
    sprite('vrblef401_15', 2)
    RefreshMultihit()
    Unknown2038(-1)
    Unknown1030(50)
    gotoLabel(0)
    label(1)
    sprite('vrblef401_20', 2)
    sprite('vrblef401_21', 2)
    sprite('vrblef401_22', 2)
    sprite('vrblef401_23', 2)

@State
def shot_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_OffsetX(96000)
    label(0)
    sprite('null', 3)
    GFX_1('blef_shot_add', -1)
    gotoLabel(0)

@State
def shot_geyser():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        GFX_SetPalette(1)
        Unknown3033()
        Unknown2019(-500)
        Unknown11056(2)
        AttackLevel_(4)
        Damage(900)
        AttackP1(80)
        Unknown11092(1)
        SameMoveProration(10)
        Hitstop(0)
        FireFX(1)
        Unknown11001(18, 18, 20)
        StarterRating(2)
        if SLOT_137:
            DamageMultiplier(80)
        Unknown2037(0)

        def upon_32():
            Unknown2037(1)
            sendToLabelUpon(10, 200)
            GFX_OffsetX(74000)
            GFX_Scale(1300)
            physicsXImpulse(24000)
            Damage(700)
            ProjectileHitWall(1)
            AirHitstunAnimation(9)
            GroundedHitstunAnimation(9)
            Unknown11001(8, 8, 10)
            AirUntechableTime(25)
            hitstun(22)
            Unknown53(1)
            if SLOT_137:
                DamageMultiplier(80)
            physicsXImpulse(12000)
            ProjectileHitWall(1)
            clearUponHandler(32)
            sendToLabel(99)

        def upon_33():
            Unknown2037(2)
            sendToLabelUpon(10, 200)
            GFX_OffsetX(74000)
            GFX_Scale(1300)
            physicsXImpulse(24000)
            Damage(800)
            AirHitstunAnimation(9)
            ProjectileHitWall(1)
            GroundedHitstunAnimation(9)
            Unknown11001(8, 8, 10)
            AirUntechableTime(30)
            hitstun(22)
            Unknown53(1)
            if SLOT_137:
                DamageMultiplier(80)
            ProjectileHitWall(1)
            physicsXImpulse(15000)
            clearUponHandler(33)
            sendToLabel(99)
    sprite('null', 1)
    label(999)
    sprite('vrblef401_50', 3)
    RefreshMultihit()
    GFX_Scale(1000)
    physicsXImpulse(0)
    Unknown1028(0)
    hitstun(25)
    AirUntechableTime(45)
    AirPushbackX(0)
    AirPushbackY(35000)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    PushbackX(15000)
    GFX_OffsetX(240000)
    SFX_3('blse_05')
    sprite('vrblef401_51', 3)
    sprite('vrblef401_52', 3)
    sprite('vrblef401_53', 3)
    sprite('vrblef401_54', 3)
    sprite('vrblef401_55', 3)
    ExitState()
    label(99)
    sprite('vrblef401_10', 1)
    GFX_0('shot_add', -1)
    label(0)
    sprite('vrblef401_10', 2)
    SFX_3('blse_08')
    sprite('vrblef401_11', 2)
    sprite('vrblef401_12', 2)
    sprite('vrblef401_13', 2)
    sprite('vrblef401_14', 2)
    if (SLOT_2 == 0):
        physicsXImpulse(2000)
        sendToLabel(1)
    else:
        Unknown2038(-1)
        Unknown1030(-400)
    gotoLabel(0)
    label(1)
    sprite('vrblef401_20', 2)
    clearUponHandler(10)
    sprite('keep', 2)
    GFX_OffsetX(-60000)
    sendToLabel(999)
    label(200)
    sprite('vrblef401_20', 2)
    clearUponHandler(10)
    physicsXImpulse(2000)
    Unknown11001(14, 14, 16)
    sprite('keep', 2)
    GFX_OffsetX(-120000)
    sendToLabel(999)

@State
def shot_geyser_col():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
    sprite('vrblef401_geyser_col', 15)

@State
def shot_geyser_2():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        GFX_SetPalette(1)
        Unknown3033()
        Unknown2019(-500)
        Unknown1056(-1000)
        Unknown1064(750)
        GFX_OffsetX(-128000)
    sprite('vrblef401_50', 3)
    sprite('vrblef401_51', 3)
    sprite('vrblef401_52', 3)
    sprite('vrblef401_53', 3)
    sprite('vrblef401_54', 3)
    sprite('vrblef401_55', 3)

@State
def shot_geyser_3():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        GFX_SetPalette(1)
        Unknown3033()
        Unknown2019(-500)
        GFX_Rotation(45000)
        GFX_Scale(875)
    sprite('vrblef401_50', 3)
    sprite('vrblef401_51', 3)
    sprite('vrblef401_52', 3)
    sprite('vrblef401_53', 3)
    sprite('vrblef401_54', 3)
    sprite('vrblef401_55', 3)

@State
def shot_geyser_4():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        GFX_SetPalette(1)
        Unknown3033()
        Unknown2019(-500)
        GFX_Rotation(-60000)
    sprite('vrblef401_50', 3)
    sprite('vrblef401_51', 3)
    sprite('vrblef401_52', 3)
    sprite('vrblef401_53', 3)
    sprite('vrblef401_54', 3)
    sprite('vrblef401_55', 3)

@State
def shot_geyser_3d():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown4003('bl_400blast_00.DIG', '')
        Unknown4015()
        GFX_Scale(500)
        Unknown2054(1)
        Unknown21010(1)
        GFX_Rotation(30000)
    sprite('null', 8)
    sprite('null', 8)
    Unknown3004(-32)

@State
def __400_mazzle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_Unload('shot_charge')
        GFX_Scale(750)
    sprite('null', 60)
    GFX_2('blef_DashThrow_fire')

@State
def __400_mazzle2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('bl_430bom_00.DIG', '')
        Unknown4015()
        Unknown1064(375)
        Unknown1056(937)
        GFX_Rotation(100000)
    sprite('null', 10)
    Unknown1099(30)

@State
def __403_mazzle():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 60)
    GFX_0('403_firewave00', 0)
    GFX_1('blef_GraspThrow_fire', 0)

@State
def __403_firewave00():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown4003('bl_403firewave_00.DIG', '')
        Unknown4015()
        GFX_Scale(750)
        Unknown2054(1)
        Unknown21010(1)
    sprite('null', 8)
    sprite('null', 8)
    Unknown3004(-32)

@State
def __404_mazzle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_Scale(800)
        GFX_Unload('shot_charge')
    sprite('null', 60)
    GFX_2('blef_DashThrow_fire')

@State
def __404_mazzle2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('bl_430bom_00.DIG', '')
        Unknown4015()
        Unknown1064(400)
        Unknown1056(1000)
        GFX_Rotation(100000)
    sprite('null', 10)
    Unknown1099(30)

@State
def __405_mazzle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_Unload('shot_charge')
    sprite('null', 60)
    GFX_2('blef_GuardCrush')

@State
def blef_410_fire():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4010(2)
        Unknown1006(0)
        GFX_OffsetX(-50000)
    sprite('null', 4)
    PFX_Scale(2000)
    PFX('blef_410fire', -1)
    sprite('null', 4)
    PFX_Scale(2000)
    PFX('blef_410fire', -1)

@State
def blef_410_finish():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    PFX_Rotation(-60000)
    PFX('blef_410finish', -1)

@State
def __430_handaura():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown2054(1)
        GFX_Scale(1500)
    sprite('null', 300)
    Unknown1099(-25)
    GFX_2('blef_430tame_pos')

@State
def __430_handaura2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown2054(1)
        GFX_Scale(1000)
    sprite('null', 300)
    GFX_2('blef_430tame_pos')

@State
def __430_mazzle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('bl_430bom_00.DIG', '')
        Unknown4015()
        GFX_Scale(800)
        GFX_Rotation(30000)
    sprite('null', 10)
    SFX_3('blse_05')
    PFX_Rotation(-45000)
    PFX('blef_430atk_hinoko', -1)
    Unknown1099(30)

@State
def __430_mazzle2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('bl_430bom_01.DIG', '')
        Unknown4015()
        GFX_Scale(600)
        GFX_Rotation(30000)
    sprite('null', 10)
    SFX_3('blse_05')
    PFX_Rotation(-45000)
    PFX('blef_430atk_circle', -1)
    Unknown1099(30)

@State
def __430_mazzlelast():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_Scale(900)
        GFX_Rotation(30000)
    sprite('null', 2)
    SFX_3('blse_06')
    sprite('null', 4)
    Unknown4003('bl_430bom_01.DIG', '')
    Unknown4015()
    PFX_Rotation(130000)
    PFX('blef_433bloom_add2', -1)
    Unknown1099(30)
    sprite('null', 7)

@State
def __430_bigmazzleShockDown():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('bl_430bom_01.DIG', '')
        Unknown4015()
        GFX_Scale(400)
        GFX_Rotation(30000)
    sprite('null', 10)
    PFX_Rotation(-45000)
    PFX('blef_430atk_circle', -1)
    Unknown1099(30)

@State
def __430_bigmazzleFireMatoDown():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
    sprite('null', 5)
    GFX_0('430_bigmazzleFire2Down', -1)

@State
def __430_bigmazzleFire2Down():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown3001(255)
        Unknown4003('bl_433fire_00', '')
        Unknown4015()
        GFX_Rotation(-60000)
    sprite('null', 11)
    sprite('null', 4)
    Unknown3004(-61)

@State
def __430_ShockCircleDown():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450firecircle_00.DIG', '')
        Unknown4015()
        GFX_Rotation(-60000)
        GFX_OffsetY(4294817296)
        GFX_OffsetX(-70000)
        GFX_Scale(1000)
        Unknown3001(150)
    sprite('null', 14)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __431_mazzle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_Rotation(30000)
    sprite('null', 60)
    GFX_2('blef_DD_fire')

@State
def __431_bigmazzleShockmatome():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4010(2)
    sprite('null', 2)
    GFX_1('blef_433bloom_add2', -1)
    GFX_0('431_bigmazzleShock', -1)
    sprite('null', 10)
    GFX_0('431_bigmazzleFireMato', -1)
    sprite('null', 3)
    GFX_0('431_ShockCircle', -1)

@State
def __431_bigmazzleShock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450atkshot_01.DIG', '')
        Unknown4015()
        GFX_Rotation(180000)
        GFX_Scale(1208)
    sprite('null', 7)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __431_bigmazzleFireMato():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
    sprite('null', 5)
    GFX_0('431_bigmazzleFire', -1)
    sprite('null', 5)
    GFX_0('431_bigmazzleFire', -1)

@State
def __431_bigmazzleFire():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450atkfire_01', '')
        Unknown4015()
        GFX_SetPalette(1)
        Unknown21004(243)
        GFX_Rotation(-100000)
        GFX_Scale(800)
    sprite('null', 3)
    GFX_0('431_bigmazzleFire2', -1)
    Unknown1059(-15)
    sprite('null', 8)
    sprite('null', 4)
    physicsYImpulse(1500)

@State
def __431_bigmazzleFire2():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_SetPalette(1)
        Unknown21004(243)
        Unknown2054(1)
        Unknown3001(255)
        Unknown4003('bl_433fire_00', '')
        Unknown4015()
        GFX_Rotation(-90000)
    sprite('null', 8)
    sprite('null', 4)
    Unknown3004(-61)

@State
def __431_ShockCircle():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450firecircle_00.DIG', '')
        Unknown4015()
        GFX_OffsetX(-200000)
        GFX_Scale(1200)
    sprite('null', 14)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __431_bigmazzleShockmatomeDown():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4010(2)
        GFX_OffsetY(150000)
    sprite('null', 2)
    PFX_Rotation(90000)
    PFX('blef_433bloom_add2', -1)
    GFX_0('431_bigmazzleShockDown', -1)
    PFX_Rotation(-90000)
    PFX_Scale(800)
    PFX('blef_433hibana_add2', -1)
    sprite('null', 5)
    GFX_0('431_bigmazzleFireMatoDown', -1)
    sprite('null', 3)
    GFX_0('431_ShockCircleDown', -1)

@State
def __431_bigmazzleShockDown():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450atkshot_01.DIG', '')
        Unknown4015()
        GFX_Rotation(90000)
        GFX_Scale(1057)
    sprite('null', 7)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __431_bigmazzleFireMatoDown():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
    sprite('null', 5)
    GFX_0('431_bigmazzleFire2Down', -1)
    sprite('null', 5)
    GFX_0('431_bigmazzleFire2Down', -1)

@State
def __431_bigmazzleFire2Down():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_SetPalette(1)
        Unknown21004(243)
        Unknown2054(1)
        Unknown3001(255)
        Unknown4003('bl_433fire_00', '')
        Unknown4015()
        GFX_Rotation(900000)
        Unknown1056(1500)
    sprite('null', 8)
    sprite('null', 4)
    Unknown3004(-61)

@State
def __431_ShockCircleDown():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450firecircle_00.DIG', '')
        Unknown4015()
        GFX_Rotation(94000)
        GFX_OffsetY(4294917296)
        GFX_Scale(1400)
        Unknown3001(150)
    sprite('null', 14)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __431_bigmazzleShockmatomeUp():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4010(2)
        GFX_OffsetY(150000)
    sprite('null', 2)
    PFX_Rotation(-90000)
    PFX('blef_433bloom_add2', -1)
    GFX_0('431_bigmazzleShockUp', -1)
    sprite('null', 5)
    PFX_Rotation(90000)
    PFX_Scale(800)
    PFX('blef_433hibana_add2', -1)
    GFX_0('431_bigmazzleFireMatoUp', -1)
    GFX_0('431_ShockCircleUp', -1)

@State
def __431_bigmazzleShockUp():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450atkshot_01.DIG', '')
        Unknown4015()
        GFX_Rotation(90000)
        GFX_Scale(1208)
    sprite('null', 7)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __431_bigmazzleFireMatoUp():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
    sprite('null', 5)
    GFX_0('431_bigmazzleFire2Up', -1)
    sprite('null', 5)
    GFX_0('431_bigmazzleFire2Up', -1)

@State
def __431_bigmazzleFire2Up():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_SetPalette(1)
        Unknown21004(243)
        Unknown2054(1)
        Unknown3001(255)
        Unknown4003('bl_433fire_00', '')
        Unknown4015()
        Unknown1056(1500)
        GFX_OffsetY(4294767296)
        Unknown1073(10000)
    sprite('null', 8)
    sprite('null', 4)
    Unknown3004(-61)

@State
def __431_ShockCircleUp():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450firecircle_00.DIG', '')
        Unknown4015()
        GFX_Rotation(-88000)
        GFX_OffsetY(4294917296)
        GFX_Scale(1600)
        Unknown3001(150)
    sprite('null', 14)
    sprite('null', 5)
    Unknown3004(-51)

@State
def blef_entry():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_SetPalette(1)
        Unknown3033()
    sprite('vrblef601_00', 3)
    sprite('vrblef601_01', 3)
    sprite('vrblef601_02', 3)

@State
def __408_BodyFire():

    def upon_IMMEDIATE():
        Unknown3033()
        GFX_SetPalette(1)
        Unknown23015(2)
        GFX_2('blef_408tamefire_tubu')
        Unknown4010(2)
    sprite('null', 30)
    sprite('null', 10)

@State
def __408_Fireroop():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4007(2)
        Unknown4010(2)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 10)
    GFX_0('408_Fire', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 16)

@State
def __408_Fire():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown2054(1)
        Unknown4003('bl_450tamefire_00.DIG', '')
        Unknown4015()
        GFX_Scale(700)
        Unknown3001(200)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __408_Kaiho():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4007(2)
        Unknown1064(2000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 5)
    GFX_0('408_Kaiho00', -1)
    GFX_1('blef_450tame_tubu', -1)
    sprite('null', 5)
    GFX_0('408_Kaiho01', -1)
    sprite('null', 5)
    GFX_0('408_Kaiho02', -1)

@State
def __408_Kaiho00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown3001(255)
        GFX_SetPalette(1)
        Unknown21004(243)
        Unknown4003('bl_450smoke_00', '')
        Unknown4015()
        Unknown1056(1300)
    sprite('null', 11)
    Unknown1059(-5)
    sprite('null', 4)
    physicsYImpulse(1500)

@State
def __408_Kaiho01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown3001(255)
        GFX_SetPalette(1)
        Unknown21004(243)
        Unknown4003('bl_450smoke_00', '')
        Unknown4015()
        GFX_OffsetX(70000)
        Unknown1064(500)
        GFX_Rotation(5000)
    sprite('null', 11)
    Unknown1059(-5)
    sprite('null', 4)
    physicsYImpulse(1500)

@State
def __408_Kaiho02():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        GFX_SetPalette(1)
        Unknown21004(243)
        Unknown3001(255)
        GFX_Scale(1000)
        Unknown2005()
        Unknown4003('bl_450smoke_00', '')
        Unknown4015()
        GFX_OffsetX(70000)
        Unknown1064(500)
        GFX_Rotation(5000)
    sprite('null', 11)
    Unknown1059(-5)
    sprite('null', 4)
    physicsYImpulse(1000)

@State
def __450_gandredfireroop():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4007(2)
        Unknown4010(2)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 10)
    GFX_0('450_gandredfire', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)

@State
def __450_gandredfire():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown2054(1)
        Unknown4003('bl_450tamefire_00.DIG', '')
        Unknown4015()
        GFX_Scale(800)
    sprite('null', 10)
    Unknown1067(10)
    Unknown1059(-10)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __450_Zanzo():

    def upon_IMMEDIATE():
        Unknown3033()
        GFX_SetPalette(1)
        Unknown3053(1)
        Unknown23015(1)
    sprite('vrbl450_00', 3)
    GFX_1('blef_450atk1_sub', 0)
    GFX_1('blef_450atk1_sub', 1)
    sprite('vrbl450_01', 4)
    GFX_1('blef_450atk1_sub', 0)
    GFX_1('blef_450atk1_sub', 1)
    sprite('vrbl450_02', 4)
    GFX_1('blef_450atk1_sub', 0)
    GFX_1('blef_450atk1_sub', 1)
    Unknown3004(-51)

@State
def __450_tamesmokeroop():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4007(2)
        Unknown1064(2000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 5)
    GFX_0('450_tamesmoke00', -1)
    PFX_Scale(1300)
    PFX('blef_450tame_tubu', -1)
    sprite('null', 5)
    GFX_0('450_tamesmoke01', -1)
    sprite('null', 5)
    GFX_0('450_tamesmoke02', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 20)

@State
def __450_tamesmoke00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown3001(200)
        Unknown4003('bl_450smoke_00', '')
        Unknown4015()
        Unknown4010(2)
        Unknown1056(1400)
    sprite('null', 11)
    Unknown1059(-5)
    sprite('null', 4)
    physicsYImpulse(1500)

@State
def __450_tamesmoke01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown3001(200)
        Unknown4003('bl_450smoke_00', '')
        Unknown4015()
        Unknown4010(2)
        GFX_OffsetX(70000)
        Unknown1064(600)
        Unknown1056(1400)
    sprite('null', 11)
    Unknown1059(-5)
    sprite('null', 4)
    physicsYImpulse(1500)

@State
def __450_tamesmoke02():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown3001(200)
        GFX_Scale(1000)
        Unknown4003('bl_450smoke_00', '')
        Unknown4015()
        Unknown4010(2)
        GFX_OffsetX(-70000)
        Unknown1064(700)
        Unknown1056(1400)
    sprite('null', 11)
    Unknown1059(-5)
    sprite('null', 4)
    physicsYImpulse(1500)

@State
def __450_bigmazzle00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450atkshot_00.DIG', '')
        Unknown4015()
        GFX_Rotation(45000)
        Unknown1064(1200)
    sprite('null', 4)
    GFX_0('450_bigmazzleFire', -1)
    GFX_0('450_fire', -1)
    GFX_0('450_bigmazzleShock', -1)
    Unknown1097(-300)
    sprite('null', 12)
    PFX_Rotation(45000)
    PFX('blef_450atk2_circle', -1)
    Unknown1097(300)
    sprite('null', 3)
    Unknown3004(-51)

@State
def __450_bigmazzle01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450atkshot_00.DIG', '')
        Unknown4015()
        GFX_Rotation(45000)
        GFX_Scale(1300)
    sprite('null', 4)
    GFX_0('450_bigmazzleFire', -1)
    GFX_0('450_fire', -1)
    GFX_0('450_bigmazzleShock', -1)
    Unknown1097(-300)
    sprite('null', 12)
    PFX_Rotation(45000)
    PFX('blef_450atk2_circle', -1)
    Unknown1097(300)
    sprite('null', 3)
    Unknown3004(-51)

@State
def __450_bigmazzle02():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450atkshot_00.DIG', '')
        Unknown4015()
        GFX_Rotation(45000)
        GFX_Scale(1400)
    sprite('null', 4)
    GFX_0('450_bigmazzleFire', -1)
    GFX_0('450_fire', -1)
    GFX_0('450_bigmazzleShock', -1)
    Unknown1097(-300)
    sprite('null', 12)
    PFX_Rotation(45000)
    PFX('blef_450atk2_circle', -1)
    Unknown1097(300)
    sprite('null', 3)
    Unknown3004(-51)

@State
def __450_bigmazzleShock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450atkshot_01.DIG', '')
        Unknown4015()
        GFX_Rotation(45000)
    sprite('null', 5)
    Unknown1099(50)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __450_bigmazzleShock2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450firecircle_00.DIG', '')
        Unknown4015()
        GFX_Rotation(95000)
        GFX_Scale(1500)
        GFX_OffsetX(-40000)
    sprite('null', 14)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __450_bigmazzleFire():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450atkfire_01', '')
        Unknown4015()
        GFX_Rotation(-45000)
    sprite('null', 11)
    Unknown1059(-15)
    sprite('null', 4)
    physicsYImpulse(1500)

@State
def __450_fire():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450atkfire_00.DIG', '')
        Unknown4015()
        GFX_Rotation(45000)
        Unknown3001(0)
    sprite('null', 15)
    Unknown3004(51)
    Unknown1067(-30)
    sprite('null', 15)
    Unknown3004(-17)

@State
def __450_ryuhai():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450ryuhai_00', '')
        Unknown4015()
        Unknown4007(2)
        sendToLabelUpon(32, 0)
        Unknown3001(0)
    sprite('null', 10)
    Unknown3004(26)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __450_lastAtk00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450lastatk_00.DIG', '')
        Unknown4015()
        GFX_Scale(1000)
    sprite('null', 7)
    GFX_1('blef_450lastground_pos', -1)
    Unknown1099(20)
    sprite('null', 6)
    Unknown3004(-51)
    GFX_0('450_lastAtkrenzoku', -1)

@State
def __450_lastAtk01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450lastatk_01.DIG', '')
        Unknown4015()
        GFX_Scale(1500)
    sprite('null', 11)
    sprite('null', 4)

@State
def __450_lastAtkrenzoku():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
    sprite('null', 5)
    GFX_0('450_bigmazzleShock2', -1)
    PFX_Rotation(50000)
    PFX_Scale(2400)
    PFX('blef_433hibana_add2', -1)

@State
def __450_lastTame():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        GFX_2('blef_450lasttame_circle')
        sendToLabelUpon(32, 0)
        GFX_Scale(2000)
    sprite('null', 32767)
    GFX_0('450_lastTame2', -1)
    Unknown1099(-10)
    label(0)
    sprite('null', 10)
    Unknown21012('450_lastTame2', 32)
    Unknown3004(-26)

@State
def __450_lastTame2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        GFX_2('blef_450lasttame_speed')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __450_Nokoribi():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450nokoribi.DIG', '')
        Unknown4015()
    sprite('null', 28)
    Unknown3004(-10)

@State
def __450nageBG():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4007(2)
        Unknown4010(2)
        sendToLabelUpon(32, 1)
    sprite('null', 32767)
    GFX_2('blef_450ahbg2_01')
    label(1)
    sprite('null', 10)
    Unknown3004(-26)

@State
def __450_rock():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450rock.DIG', '')
        Unknown21010(1)
    sprite('null', 15)
    GFX_1('blef_450minirock01', -1)
    sprite('null', 30)
    GFX_0('450_rock00', -1)
    sprite('null', 30)
    Unknown3001(0)

@State
def __450_rock00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown2005()
        Unknown4003('bl_450rock.DIG', '')
        Unknown21010(1)
        GFX_Scale(1500)
    sprite('null', 10)
    GFX_1('blef_450minirock01', -1)
    sprite('null', 49)
    GFX_0('450_rock01', -1)

@State
def __450_rock01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('bl_450rock.DIG', '')
        Unknown21010(1)
        GFX_Scale(600)
    sprite('null', 59)

@State
def HeatUpEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        GFX_2('blef_lvupsub')
        Unknown4007(2)
    sprite('null', 65)
    GFX_1('blef_lvup_hinoko', -1)
    SFX_3('blse_08')

@State
def __440_frameEffEX():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown21010(1)
        Unknown4010(2)
        GFX_SetPalette(1)
        GFX_OffsetX(-250000)
        GFX_Scale(1600)
    sprite('vrblef440_00', 3)
    Unknown1099(10)
    GFX_1('blef_440_rock', -1)
    sprite('vrblef440_01', 3)
    GFX_0('440_Brust', -1)
    sprite('vrblef440_02', 3)
    GFX_0('440_frameEffSub', 0)
    Unknown21010(0)
    Unknown4009(2)
    ScreenShake(8000, 8000)
    sprite('vrblef440_04', 3)
    GFX_0('440_frameEffSub2', -1)
    Unknown21012('440_frameEffSub', 32)
    sprite('vrblef440_05', 3)
    sprite('vrblef440_06', 3)
    sprite('vrblef440_07', 3)
    sprite('vrblef440_08', 2)
    sprite('vrblef440_09', 2)

@State
def __440_frameEff():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown21010(1)
        Unknown4010(2)
        GFX_SetPalette(1)
        GFX_OffsetX(-250000)
        GFX_Scale(1200)
    sprite('vrblef440_00', 3)
    Unknown1099(10)
    GFX_1('blef_440_rock', -1)
    sprite('vrblef440_01', 3)
    GFX_0('440_Brust', -1)
    sprite('vrblef440_02', 3)
    GFX_0('440_frameEffSub', 0)
    Unknown21010(0)
    Unknown4009(2)
    ScreenShake(8000, 8000)
    sprite('vrblef440_04', 3)
    Unknown21012('440_frameEffSub', 32)
    sprite('vrblef440_05', 3)
    sprite('vrblef440_06', 3)
    sprite('vrblef440_07', 3)
    sprite('vrblef440_08', 2)
    sprite('vrblef440_09', 2)

@State
def __440_Brust():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        GFX_Scale(1350)
        Unknown4003('bl_430bom_00.DIG', '')
        Unknown4015()
        GFX_Rotation(-35000)
        GFX_OffsetX(150000)
    sprite('null', 3)
    Unknown3001(0)
    sprite('null', 5)
    Unknown3001(255)
    Unknown1099(20)
    sprite('null', 5)
    Unknown3004(-51)

@State
def __440_frameEffSub():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown21010(1)
        Unknown1056(1600)
        Unknown1064(1600)
        Unknown1088(750)
        Unknown4010(2)
        GFX_2('blef_440bloom_00')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown1099(60)
    Unknown3004(-26)

@State
def __440_frameEffSub2():

    def upon_IMMEDIATE():
        Unknown21010(1)
        GFX_Rotation(50000)
        GFX_OffsetX(100000)
        GFX_2('blef_433hibana_add2')
    sprite('null', 20)
    Unknown4051(1)
    PFX_Scale(1300)
    PFX('blef_440_fireroad', -1)
    Unknown1067(-15)
    physicsXImpulse(-20000)
    physicsYImpulse(20000)
    sprite('null', 10)
    Unknown3004(-26)

@State
def EventCKRun():

    def upon_IMMEDIATE():
        Unknown30012(1)
        Unknown2055(600)
        physicsXImpulse(-12200)
    label(0)
    sprite('ctk450_25', 7)
    sprite('ctk450_26', 7)
    sprite('ctk450_27', 7)
    sprite('ctk450_28', 7)
    loopRest()
    gotoLabel(0)

@State
def EventTG():

    def upon_IMMEDIATE():
        Unknown30012(0)
        sendToLabelUpon(32, 1)
        Unknown1000(-50000)
        Unknown2019(1000)
    sprite('tg620_02', 32767)
    label(1)
    sprite('tg072_00', 14)
    GFX_1('ef_exhit_sub', 0)
    SFX_0('100_hit_grap_3')
    sprite('tg072_00', 7)
    physicsXImpulse(-50000)
    physicsYImpulse(20000)
    setGravity(2000)
    sprite('tg072_01', 7)
    sprite('tg072_02', 7)
    sprite('tg072_01', 7)
    sprite('tg072_02', 7)
    sprite('tg072_01', 7)
    sprite('tg072_02', 7)
    loopRest()