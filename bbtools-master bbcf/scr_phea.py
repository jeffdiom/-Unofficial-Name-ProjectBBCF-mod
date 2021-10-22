@Subroutine
def RedOnlyAirStatus():
    AirUntechableTime(25)
    AirPushbackX(10000)
    AirPushbackY(17000)

@Subroutine
def BlueOnlyAirStatus():
    AirPushbackX(2500)
    AirPushbackY(2500)

@Subroutine
def ShotDeleteZone():
    Unknown4011(3)
    Unknown4010(3)
    Unknown4007(3)
    Unknown4009(3)
    GuardPoint_(1)
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    Unknown22031(0, 0)
    Unknown22032(1)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_30):

            def upon_42():
                if SLOT_2:
                    Unknown21007(3, 32)

@State
def ShotDefCol():

    def upon_IMMEDIATE():
        callSubroutine('ShotDeleteZone')
        Unknown1056(1800)
        Unknown1064(2700)
        teleportRelativeX(150000)
        Unknown1007(150000)
    sprite('null', 2)
    sprite('ph_shotdefcol', 9)

@State
def EMB_PH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown2054(1)
        Unknown3038(1)
        Unknown23015(5)
        Unknown4003('ef_emb_ph.DIG', '')
        Unknown1007(315000)
        Unknown1096(1300)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-16776961, 10)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 10)
    Unknown3025(-1, 10)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 80)

@State
def EMB_PH_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown2054(1)
        Unknown3038(1)
        Unknown23015(5)
        Unknown4003('ef_emb_ph.DIG', '')
        Unknown1007(315000)
        Unknown1096(1300)
    sprite('null', 8)
    Unknown3026(-16777216)
    Unknown3025(-1, 10)
    sprite('null', 8)
    Unknown3025(-8342273, 10)
    sprite('null', 8)
    Unknown3025(-16744193, 10)
    sprite('null', 8)
    Unknown3025(-16744193, 10)
    sprite('null', 80)

@State
def EMB_PH_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown2054(1)
        Unknown23015(5)
        Unknown4003('ef_emb_ph.DIG', '')
        Unknown1007(315000)
        Unknown1096(1300)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-65536, 10)
    sprite('null', 10)
    Unknown3025(-55256, 10)
    sprite('null', 10)
    Unknown3025(-19276, 10)
    sprite('null', 10)
    Unknown3025(-65536, 10)
    sprite('null', 80)

@State
def ph333_arm():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown23015(8)
    sprite('ph333_cutin00', 3)
    GFX_0('ph333_arm_eff_L', 0)
    GFX_0('ph333_arm_eff_R', 1)
    sprite('ph333_cutin01', 20)
    sprite('ph333_cutin02', 3)
    GFX_0('ph333_arm_eff2_L', 0)
    GFX_0('ph333_arm_eff2_R', 1)
    sprite('ph333_cutin03', 32767)
    Unknown4054(9)
    Unknown4045('706865665f33333361726d5f666972653300000000000000000000000000000002000000')
    Unknown4054(9)
    Unknown4045('706865665f33333361726d5f666972653300000000000000000000000000000003000000')

@State
def ph333_arm_eff_L():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4054(6)
        Unknown23067('phef_333arm_circle')
    label(0)
    sprite('null', 3)
    Unknown4054(9)
    Unknown4045('706865665f33333361726d5f666972650000000000000000000000000000000064000000')
    gotoLabel(0)

@State
def ph333_arm_eff_R():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4054(6)
        Unknown23067('phef_333arm_circle')
    label(0)
    sprite('null', 3)
    Unknown4054(9)
    Unknown4045('706865665f33333361726d5f666972650000000000000000000000000000000064000000')
    gotoLabel(0)

@State
def ph333_arm_eff2_L():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown23015(7)
        GFX_2('phef_333arm')
    sprite('null', 60)
    Unknown4054(9)
    Unknown4045('706865665f33333361726d5f666972653200000000000000000000000000000064000000')

@State
def ph333_arm_eff2_R():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown23015(7)
        GFX_2('phef_333arm')
    sprite('null', 60)
    Unknown4054(9)
    Unknown4045('706865665f33333361726d5f666972653200000000000000000000000000000064000000')

@State
def phef_340_fire():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()
        teleportRelativeX(-32000)
        Unknown1007(8000)
    sprite('vr_ph340_07', 3)
    GFX_1('phef_340fire_ground', 0)
    sprite('vr_ph340_08', 4)
    Unknown4049(1250)
    Unknown4045('706865665f33343066697265000000000000000000000000000000000000000000000000')
    Unknown4049(1000)
    Unknown4045('706865665f33343066697265000000000000000000000000000000000000000001000000')
    sprite('vr_ph340_10', 2)
    Unknown4049(750)
    Unknown4045('706865665f33343066697265000000000000000000000000000000000000000000000000')
    Unknown4049(500)
    Unknown4045('706865665f33343066697265000000000000000000000000000000000000000001000000')
    sprite('vr_ph340_11', 2)
    Unknown4049(250)
    Unknown4045('706865665f33343066697265000000000000000000000000000000000000000000000000')
    GFX_1('phef_340fire_add', 1)
    sprite('vr_ph340_12', 2)
    sprite('vr_ph340_13', 4)
    sprite('vr_ph340_14', 4)
    sprite('vr_ph340_15', 4)

@State
def phef_600_bg():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(3)
        Unknown3032()
        Unknown1056(20000)
        Unknown1064(20000)
        Unknown23032(50)
        Unknown23033(50)
        Unknown23015(15)
        Unknown2019(10000)
    sprite('vr_screen_black', 30)
    Unknown3001(0)
    Unknown3004(3)
    sprite('vr_screen_black', 60)
    Unknown3001(95)
    Unknown3004(0)
    sprite('vr_screen_black', 30)
    Unknown3004(-3)

@State
def phef_600_Fire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        teleportRelativeX(100000)
    sprite('null', 1)
    GFX_1('phef_600bigen', 100)

@State
def phef_600_Fire2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()
    sprite('phef600_10', 4)
    sprite('phef600_11', 4)
    sprite('phef600_12', 4)

@State
def phef_600_FireWall():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4003('pheff600_firewall', '')
        Unknown4015()
        teleportRelativeX(100000)
        Unknown3033()
        GFX_2('phef_600ground')
    sprite('null', 6)
    Unknown3001(0)
    Unknown3004(32)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_0')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_1')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_0')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_1')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_0')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_1')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_0')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 16)
    Unknown3004(-16)
    GFX_0('phef_600_Fire_End', -1)

@State
def phef_600_Fire_End():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 1)
    GFX_1('phef_600fire_end', -1)

@State
def phef_600_HatFire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()
        Unknown23015(6)
    sprite('phef600_01', 6)
    sprite('phef600_02', 6)
    sprite('phef600_03', 6)
    sprite('phef600_04', 6)
    sprite('phef600_05', 6)
    sprite('phef600_06', 6)

@State
def phef_600_Hat():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(0)
        Unknown3032()
    sprite('phef600_hat', 2)
    Unknown3001(127)
    sprite('phef600_hat', 2)
    Unknown3001(191)
    sprite('phef600_hat', 2)
    Unknown3001(255)

@State
def phef_602_Fire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        teleportRelativeX(-20000)
    sprite('null', 1)
    GFX_1('phef_600bigen', 100)

@State
def phef_602_Fire2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()
        teleportRelativeX(-80000)
    sprite('phef600_10', 4)
    sprite('phef600_11', 4)
    sprite('phef600_12', 4)

@State
def phef_602_FireWall():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4003('pheff600_firewall', '')
        Unknown4015()
        teleportRelativeX(-20000)
        Unknown3033()
        GFX_2('phef_600ground')
        Unknown1056(1500)
    sprite('null', 6)
    SFX_0('019_quake_0')
    Unknown3001(0)
    Unknown3004(32)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    SFX_0('019_quake_1')
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    SFX_0('019_quake_0')
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    SFX_0('019_quake_1')
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    SFX_0('019_quake_0')
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    SFX_0('019_quake_1')
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    SFX_0('019_quake_0')
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 16)
    Unknown3004(-16)
    GFX_0('phef_602_Fire_End', -1)

@State
def phef_602_Fire_End():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        teleportRelativeX(-20000)
    sprite('null', 1)
    GFX_1('phef_600fire_end', -1)

@State
def ph001Eff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('pheff001_fire00', '')
        Unknown1096(450)
        Unknown3001(180)
        Unknown1007(275000)
        teleportRelativeX(-65000)
        Unknown2008()
        GFX_2('phef001_hinoko')
    sprite('null', 5)
    Unknown3001(0)
    Unknown3004(30)
    label(0)
    sprite('null', 25)
    physicsYImpulse(300)
    Unknown3004(0)
    Unknown1099(-2)
    sprite('null', 5)
    Unknown1099(-1)
    physicsYImpulse(150)
    sprite('null', 25)
    physicsYImpulse(-300)
    Unknown1099(2)
    sprite('null', 5)
    Unknown1099(1)
    physicsYImpulse(-150)
    gotoLabel(0)

@State
def ph032FireEff():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(2)
        Unknown3033()
        teleportRelativeX(50000)
    sprite('vr_ph32_00', 3)
    GFX_0('ph032FireEffSub', -1)
    GFX_1('phef_dash_aura', 0)
    GFX_1('phef_dash_aura', 1)
    GFX_1('phef_dash_aura', 2)
    GFX_1('phef_dash_aura', 3)
    GFX_1('phef_dash_aura', 4)
    GFX_1('phef_dash_aura', 5)
    GFX_1('phef_dash_aura', 6)
    sprite('vr_ph32_01', 3)
    sprite('vr_ph32_02', 3)
    sprite('vr_ph32_03', 3)
    sprite('vr_ph32_04', 3)
    sprite('vr_ph32_05', 3)
    Unknown3004(-25)
    sprite('vr_ph32_06', 3)
    sprite('vr_ph32_07', 3)

@State
def ph032FireEffSub():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(0)
    sprite('vr_ph32_10', 3)
    Unknown3025(0, 16)
    sprite('vr_ph32_11', 3)
    sprite('vr_ph32_12', 3)
    sprite('vr_ph32_13', 3)
    Unknown3004(-25)
    sprite('vr_ph32_14', 3)
    sprite('vr_ph32_15', 3)

@State
def ph032FireEff2():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(2)
        Unknown3033()
        teleportRelativeX(50000)
    sprite('vr_ph32_00', 3)
    sprite('vr_ph32_01', 3)
    sprite('vr_ph32_02', 3)
    sprite('vr_ph32_03', 3)
    sprite('vr_ph32_04', 3)
    sprite('vr_ph32_05', 3)
    Unknown3004(-25)
    sprite('vr_ph32_06', 3)
    sprite('vr_ph32_07', 3)

@State
def ph035FireEff():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(2)
        Unknown3033()
    sprite('vr_ph35_00', 3)
    GFX_0('ph035FireEffSub', -1)
    GFX_1('phef_dash_aura', 0)
    GFX_1('phef_dash_aura', 1)
    GFX_1('phef_dash_aura', 2)
    GFX_1('phef_dash_aura', 3)
    GFX_1('phef_dash_aura', 4)
    GFX_1('phef_dash_aura', 5)
    GFX_1('phef_dash_aura', 6)
    sprite('vr_ph35_01', 3)
    sprite('vr_ph35_02', 3)
    sprite('vr_ph35_04', 3)
    sprite('vr_ph35_05', 2)
    sprite('vr_ph35_06', 2)
    sprite('vr_ph35_07', 2)

@State
def ph035FireEffSub():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(0)
    sprite('vr_ph035_10', 3)
    Unknown3025(0, 16)
    sprite('vr_ph035_11', 3)
    sprite('vr_ph035_12', 3)
    Unknown3004(-25)
    sprite('vr_ph035_13', 3)
    sprite('vr_ph035_14', 3)

@State
def ph035FireEff2():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(2)
        Unknown3033()
    sprite('vr_ph35_00', 3)
    sprite('vr_ph35_02', 3)
    sprite('vr_ph35_05', 3)
    Unknown3004(-25)
    sprite('vr_ph35_06', 3)
    sprite('vr_ph35_07', 3)

@State
def phStocEff_Master1():

    def upon_IMMEDIATE():
        Unknown2054(1)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(0)

        def upon_34():
            clearUponHandler(34)
            sendToLabel(1)

        def upon_35():
            clearUponHandler(35)
            sendToLabel(2)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(100)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(200)
    sprite('null', 10)
    label(0)
    sprite('null', 32767)
    GFX_0('phStocEff_blue', -1)
    Unknown38(4, 1)
    Unknown21007(4, 33)
    label(1)
    sprite('null', 32767)
    GFX_0('phStocEff_green', -1)
    Unknown38(4, 1)
    Unknown21007(4, 33)
    label(2)
    sprite('null', 32767)
    GFX_0('phStocEff_red', -1)
    Unknown38(4, 1)
    Unknown21007(4, 33)
    label(100)
    sprite('null', 10)
    Unknown21007(4, 32)
    ExitState()
    label(200)
    sprite('null', 10)
    Unknown21007(4, 41)
    ExitState()

@State
def phStocEff_Master2():

    def upon_IMMEDIATE():
        Unknown2054(1)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(0)

        def upon_34():
            clearUponHandler(34)
            sendToLabel(1)

        def upon_35():
            clearUponHandler(35)
            sendToLabel(2)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(100)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(200)
    sprite('null', 10)
    label(0)
    sprite('null', 3)
    sprite('null', 32767)
    GFX_0('phStocEff_blue', -1)
    Unknown38(5, 1)
    Unknown21007(5, 34)
    label(1)
    sprite('null', 3)
    sprite('null', 32767)
    GFX_0('phStocEff_green', -1)
    Unknown38(5, 1)
    Unknown21007(5, 34)
    label(2)
    sprite('null', 3)
    sprite('null', 32767)
    GFX_0('phStocEff_red', -1)
    Unknown38(5, 1)
    Unknown21007(5, 34)
    label(100)
    sprite('null', 10)
    Unknown21007(5, 32)
    ExitState()
    label(200)
    sprite('null', 10)
    Unknown21007(5, 41)
    ExitState()

@State
def phStocEff_Master3():

    def upon_IMMEDIATE():
        Unknown2054(1)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(0)

        def upon_34():
            clearUponHandler(34)
            sendToLabel(1)

        def upon_35():
            clearUponHandler(35)
            sendToLabel(2)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(100)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(200)
    sprite('null', 10)
    label(0)
    sprite('null', 6)
    sprite('null', 32767)
    GFX_0('phStocEff_blue', -1)
    Unknown38(6, 1)
    Unknown21007(6, 35)
    label(1)
    sprite('null', 6)
    sprite('null', 32767)
    GFX_0('phStocEff_green', -1)
    Unknown38(6, 1)
    Unknown21007(6, 35)
    label(2)
    sprite('null', 6)
    sprite('null', 32767)
    GFX_0('phStocEff_red', -1)
    Unknown38(6, 1)
    Unknown21007(6, 35)
    label(100)
    sprite('null', 10)
    Unknown21007(6, 32)
    ExitState()
    label(200)
    sprite('null', 10)
    Unknown21007(6, 41)
    ExitState()

@State
def phStocEff_red():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown1096(650)
        Unknown3032()
        Unknown4025(3)
        Unknown4008(3)
        Unknown2054(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)

        def upon_41():
            Unknown14()

        def upon_33():
            SLOT_51 = 1

        def upon_34():
            SLOT_52 = 1

        def upon_35():
            SLOT_53 = 1

        def upon_16():
            if SLOT_51:
                Unknown2071('0300000000000000a08601005a00000001000000')
            if SLOT_52:
                Unknown2071('03000000589effff50c300005a00000001000000')
            if SLOT_53:
                Unknown2071('03000000b03cffff000000005a00000001000000')
    sprite('null', 1)
    sprite('null', 5)
    Unknown4003('pheff_stoc00', '')
    sprite('null', 32767)
    Unknown4003('pheff_stoc01', '')
    label(1)
    sprite('null', 6)
    sprite('null', 4)
    Unknown4025(0)
    Unknown4003('pheff_stoc02', '')
    Unknown3004(-51)

@State
def phStocEff_blue():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown1096(650)
        Unknown3032()
        Unknown4025(3)
        Unknown4008(3)
        Unknown2054(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)

        def upon_41():
            Unknown14()

        def upon_33():
            SLOT_51 = 1

        def upon_34():
            SLOT_52 = 1

        def upon_35():
            SLOT_53 = 1

        def upon_16():
            if SLOT_51:
                Unknown2071('0300000000000000a08601005a00000001000000')
            if SLOT_52:
                Unknown2071('03000000589effff50c300005a00000001000000')
            if SLOT_53:
                Unknown2071('03000000b03cffff000000005a00000001000000')
    sprite('null', 1)
    sprite('null', 5)
    Unknown4003('pheff_Bstoc00', '')
    sprite('null', 32767)
    Unknown4003('pheff_Bstoc01', '')
    label(1)
    sprite('null', 6)
    sprite('null', 4)
    Unknown4025(0)
    Unknown4003('pheff_Bstoc02', '')
    Unknown3004(-51)

@State
def phStocEff_green():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown1096(650)
        Unknown3032()
        Unknown4025(3)
        Unknown4008(3)
        Unknown2054(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)

        def upon_41():
            Unknown14()

        def upon_33():
            SLOT_51 = 1

        def upon_34():
            SLOT_52 = 1

        def upon_35():
            SLOT_53 = 1

        def upon_16():
            if SLOT_51:
                Unknown2071('0300000000000000a08601005a00000001000000')
            if SLOT_52:
                Unknown2071('03000000589effff50c300005a00000001000000')
            if SLOT_53:
                Unknown2071('03000000b03cffff000000005a00000001000000')
    sprite('null', 1)
    sprite('null', 5)
    Unknown4003('pheff_Gstoc00', '')
    sprite('null', 32767)
    Unknown4003('pheff_Gstoc01', '')
    label(1)
    sprite('null', 6)
    sprite('null', 4)
    Unknown4025(0)
    Unknown4003('pheff_Gstoc02', '')
    Unknown3004(-51)

@State
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4003('rgef_mc.DIG', 'rgef_mc_motion_000.mmot')
        Unknown4015()
        Unknown21004(224)
        Unknown2054(1)
    sprite('null', 74)

@State
def phCmnFireEff():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown4003('phCmneff_fire00', '')
        Unknown3032()
    sprite('null', 7)
    sprite('null', 5)
    Unknown3004(-51)

@State
def phCmnWaterEff():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
    sprite('null', 10)
    Unknown1099(1)
    GFX_1('phefcmn_fallwater', -1)
    Unknown3004(-8)
    sprite('null', 6)
    Unknown1099(15)

@State
def phCmnWaterEff2():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown1096(550)
        Unknown4003('phCmneff_water01', '')
    sprite('null', 10)
    GFX_1('phefcmn_fallwater', -1)
    sprite('null', 6)
    Unknown1099(15)

@State
def ph200_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('ph200eff_00.DIG', '')
        Unknown1007(300000)
        teleportRelativeX(100000)
        Unknown1056(1400)
        Unknown1064(950)
        Unknown3032()
        Unknown1073(20000)
        Unknown4007(2)
    sprite('null', 3)
    sprite('null', 3)
    Unknown4007(0)
    sprite('null', 16)
    GFX_0('ph200_effSub', -1)

@State
def ph200_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(20000)
    sprite('vr_ph200effpos_00', 2)
    GFX_1('phefcmn_fallwater', 0)
    sprite('vr_ph200effpos_00', 2)
    GFX_1('phefcmn_fallwater', 1)
    sprite('vr_ph200effpos_00', 2)
    GFX_1('phefcmn_fallwater', 2)

@State
def ph201_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('ph201eff_00.DIG', '')
        Unknown1007(270000)
        teleportRelativeX(100000)
        Unknown3032()
        Unknown4007(2)
    sprite('null', 3)
    Unknown1096(700)
    sprite('null', 9)
    Unknown4007(0)
    GFX_0('ph201_effSub', -1)
    Unknown1096(850)
    sprite('null', 4)
    sprite('null', 10)
    Unknown3004(-26)

@State
def ph201_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(75000)
        Unknown1007(-50000)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 0)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 1)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 2)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 3)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 4)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 5)

@State
def ph202_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('ph202eff_00.DIG', '')
        Unknown1007(210000)
        teleportRelativeX(205000)
        Unknown1056(700)
        Unknown1064(600)
        Unknown4007(2)
    sprite('null', 3)
    GFX_1('phef202_patchin', -1)
    SFX_0('015_blaze_0')
    sprite('null', 3)
    Unknown4007(0)
    sprite('null', 5)
    GFX_1('phef202_hinoko', -1)
    GFX_0('ph202_effSub', -1)

@State
def ph202_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(20000)
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 0)
    Unknown36(1)
    Unknown2005()
    Unknown1096(700)
    Unknown1007(-25000)
    Unknown35()
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 1)
    Unknown36(1)
    Unknown1056(900)
    Unknown1064(-700)
    Unknown1007(32500)
    Unknown35()
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 2)
    Unknown36(1)
    Unknown2005()
    Unknown1096(700)
    Unknown1007(-22000)
    Unknown35()

@State
def ph210_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('ph210eff_00.DIG', '')
        Unknown1007(324000)
        teleportRelativeX(-40000)
        Unknown1096(900)
        Unknown1072(-15000)
        Unknown3032()
        Unknown4007(2)
    sprite('null', 3)
    GFX_0('ph210_effSub', -1)
    sprite('null', 11)
    Unknown4007(0)
    sprite('null', 8)

@State
def ph210_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
    sprite('vr_ph210effpos_00', 1)
    GFX_1('phefcmn_fallwater', 0)
    sprite('vr_ph210effpos_00', 1)
    GFX_1('phefcmn_fallwater', 1)
    sprite('vr_ph210effpos_00', 1)
    GFX_1('phefcmn_fallwater', 2)
    sprite('vr_ph210effpos_00', 1)
    GFX_1('phefcmn_fallwater', 3)
    sprite('vr_ph210effpos_00', 1)
    GFX_1('phefcmn_fallwater', 4)

@State
def ph211_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1007(308000)
        teleportRelativeX(50000)
        Unknown3032()
        Unknown1072(-30000)
        Unknown1064(-1000)
        Unknown1056(1000)
        Unknown4007(2)
    sprite('vr_ph254_00', 1)
    GFX_1('phef201_kira', 0)
    GFX_1('phef201_kira', 1)
    GFX_1('phef201_kira', 2)
    GFX_1('phef201_kira', 3)
    GFX_1('phef201_kira', 4)
    GFX_1('phef201_kira', 5)
    GFX_1('phef201_kira', 6)
    sprite('vr_ph254_00', 3)
    Unknown1057(300)
    Unknown1065(-300)
    sprite('vr_ph254_01', 2)
    sprite('vr_ph254_01', 2)
    Unknown4007(0)
    sprite('vr_ph254_02', 4)
    Unknown3004(-22)
    sprite('vr_ph254_03', 3)
    sprite('vr_ph254_04', 3)

@State
def ph212_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('ph202eff_00.DIG', '')
        Unknown1007(330000)
        teleportRelativeX(175000)
        Unknown1056(900)
        Unknown1064(750)
        Unknown1072(-14500)
        Unknown4007(2)
    sprite('null', 3)
    GFX_1('phef202_patchin', -1)
    SFX_0('015_blaze_0')
    sprite('null', 3)
    Unknown4007(0)
    sprite('null', 5)
    GFX_1('phef202_hinoko', -1)
    GFX_0('ph212_effSub', -1)

@State
def ph212_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
    sprite('vr_ph212effpos_00', 2)
    GFX_0('phCmnFireEff', 0)
    Unknown36(1)
    Unknown2005()
    Unknown1096(800)
    Unknown1007(-60000)
    Unknown35()
    sprite('vr_ph212effpos_00', 2)
    GFX_0('phCmnFireEff', 1)
    Unknown36(1)
    Unknown1096(800)
    Unknown1064(-700)
    teleportRelativeX(40000)
    Unknown1072(7500)
    Unknown35()
    sprite('vr_ph212effpos_00', 2)
    GFX_0('phCmnFireEff', 2)
    Unknown36(1)
    Unknown2005()
    Unknown1096(900)
    teleportRelativeX(-100000)
    Unknown1007(-100000)
    Unknown35()

@State
def ph214_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown1007(130000)
        teleportRelativeX(135000)
        Unknown1096(1100)
        Unknown1077(-25000, 25000)
        Unknown4007(2)
    sprite('vr_ph214_00', 3)
    Unknown21010(1)
    sprite('vr_ph214_01', 3)
    Unknown4007(0)
    Unknown21010(0)
    sprite('vr_ph214_02', 4)
    sprite('vr_ph214_03', 3)
    Unknown3004(-15)
    sprite('vr_ph214_04', 2)
    sprite('vr_ph214_05', 2)
    GFX_1('phefcmn_fallwater', -1)

@State
def ph215_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        teleportRelativeX(300000)
        Unknown1007(-25000)
        Unknown1096(1150)
        Unknown3032()
        Unknown4007(2)
    sprite('vr_ph215_00', 2)
    sprite('vr_ph215_01', 2)
    sprite('vr_ph215_02', 2)
    sprite('vr_ph215_03', 3)
    sprite('vr_ph215_04', 3)
    Unknown4007(0)
    sprite('vr_ph215_05', 3)
    sprite('vr_ph215_06', 3)
    GFX_1('phef201_kira', 0)
    GFX_1('phef201_kira', 1)
    GFX_1('phef201_kira', 2)
    sprite('vr_ph215_07', 3)

@State
def ph216_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1007(130000)
        teleportRelativeX(135000)
        Unknown1056(1400)
        Unknown1064(1200)
        Unknown3033()
        Unknown4061(2)
        Unknown23015(1)
        Unknown4007(2)
    sprite('vr_ph216_00', 4)
    GFX_0('ph216_effBG', -1)
    SFX_0('015_blaze_0')
    sprite('vr_ph216_01', 4)
    GFX_1('phef216_smoke', -1)
    Unknown4007(0)
    sprite('vr_ph216_02', 3)
    sprite('vr_ph216_03', 3)
    sprite('vr_ph216_04', 2)
    sprite('vr_ph216_05', 2)

@State
def ph216_effBG():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1096(2000)
    sprite('vr_ph216bloom_00', 15)
    sprite('vr_ph216bloom_00', 10)
    Unknown3004(-26)

@State
def ph230_eff():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4003('ph230eff_00.DIG', '')
        teleportRelativeX(20000)
        Unknown1007(50000)
        Unknown3032()
        Unknown1064(700)
        Unknown1056(600)
        Unknown1072(15000)
        Unknown2054(1)
        Unknown4007(2)
    sprite('vr_ph202effpos_00', 4)
    GFX_1('phef230_sibuki', -1)
    sprite('vr_ph202effpos_00', 2)
    Unknown4007(0)
    Unknown1097(50)
    sprite('vr_ph202effpos_00', 2)
    GFX_1('phef230_sibuki', -1)
    Unknown1097(50)
    sprite('vr_ph202effpos_00', 16)

@State
def ph231_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('ph201eff_00.DIG', '')
        teleportRelativeX(120000)
        Unknown1007(150000)
        Unknown1072(10000)
        Unknown3032()
        Unknown4007(2)
    sprite('null', 3)
    Unknown1096(400)
    sprite('null', 3)
    GFX_0('ph231_effSub', -1)
    Unknown1096(550)
    sprite('null', 6)
    Unknown4007(0)
    sprite('null', 4)
    sprite('null', 10)
    Unknown3004(-26)

@State
def ph231_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(75000)
        Unknown1007(-50000)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 0)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 1)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 2)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 3)

@Subroutine
def MagicInit():
    Unknown2010()
    Unknown4011(3)

@State
def ph232_eff():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        teleportRelativeX(-100000)
        Unknown1007(-50000)
        Unknown4007(2)
    sprite('vr_ph235_00', 4)
    SFX_0('015_blaze_0')
    GFX_1('phef_232_burn', 0)
    sprite('vr_ph235_01', 4)
    Unknown4007(0)
    GFX_1('phef235fire', -1)
    sprite('vr_ph235_02', 4)
    sprite('vr_ph235_03', 4)
    sprite('vr_ph235_04', 4)

@State
def ph235_eff():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        teleportRelativeX(275000)
        Unknown1007(-10000)
        Unknown1096(1900)
        Unknown2005()
        Unknown4007(2)
    sprite('vr_ph235_10', 4)
    SFX_0('015_blaze_0')
    GFX_1('phef232_sub', 0)
    GFX_1('phef232_sub', 1)
    GFX_1('phef232_sub', 2)
    GFX_1('phef232_sub', 3)
    GFX_1('phef232_sub', 4)
    GFX_1('phef232_sub', 5)
    GFX_1('phef232_sub', 6)
    sprite('vr_ph235_11', 4)
    Unknown4007(0)
    sprite('vr_ph235_12', 4)
    sprite('vr_ph235_13', 4)
    sprite('vr_ph235_14', 4)
    sprite('vr_ph235_15', 4)
    sprite('vr_ph235_16', 4)

@State
def ph250_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('ph250eff_00.DIG', '')
        Unknown1007(217000)
        teleportRelativeX(75000)
        Unknown1096(850)
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 3)
    sprite('null', 19)
    GFX_0('ph250_effSub', -1)
    Unknown4007(0)
    Unknown4010(0)

@State
def ph250_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(20000)
        Unknown1007(100000)
    sprite('vr_ph200effpos_00', 2)
    GFX_0('phCmnWaterEff', 0)
    Unknown36(1)
    Unknown1096(450)
    Unknown1007(-25000)
    Unknown1073(-5000)
    Unknown35()
    sprite('vr_ph200effpos_00', 2)
    GFX_0('phCmnWaterEff', 1)
    Unknown36(1)
    Unknown1056(550)
    Unknown1064(-750)
    Unknown1007(40000)
    Unknown35()

@State
def ph251_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1007(289800)
        teleportRelativeX(20000)
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
    sprite('vr_ph254_00', 2)
    GFX_1('phef201_kira', 0)
    GFX_1('phef201_kira', 1)
    GFX_1('phef201_kira', 2)
    GFX_1('phef201_kira', 3)
    GFX_1('phef201_kira', 4)
    GFX_1('phef201_kira', 5)
    GFX_1('phef201_kira', 6)
    Unknown1099(3)
    sprite('vr_ph254_00', 1)
    sprite('vr_ph254_00', 1)
    Unknown1097(300)
    sprite('vr_ph254_01', 3)
    sprite('vr_ph254_02', 3)
    Unknown3004(-22)
    Unknown4010(0)
    Unknown4007(0)
    sprite('vr_ph254_03', 3)
    sprite('vr_ph254_04', 3)

@State
def ph251_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(75000)
        Unknown1007(-50000)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 0)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 1)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 2)
    sprite('vr_ph201effpos_00', 2)
    GFX_1('phef201_kira', 3)

@State
def ph252_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('ph202eff_00.DIG', '')
        Unknown1007(270000)
        teleportRelativeX(175000)
        Unknown1056(600)
        Unknown1064(700)
        Unknown4007(2)
    sprite('null', 3)
    Unknown4010(2)
    GFX_1('phef202_patchin', -1)
    SFX_0('015_blaze_0')
    sprite('null', 3)
    Unknown4007(0)
    Unknown4010(0)
    sprite('null', 5)
    GFX_1('phef202_hinoko', -1)
    GFX_0('ph252_effSub', -1)

@State
def ph252_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(20000)
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 0)
    Unknown36(1)
    Unknown2005()
    Unknown1096(600)
    Unknown1007(-25000)
    Unknown35()
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 1)
    Unknown36(1)
    Unknown1056(800)
    Unknown1064(-600)
    Unknown1007(32500)
    Unknown35()
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 2)
    Unknown36(1)
    Unknown2005()
    Unknown1096(600)
    Unknown1007(-22000)
    teleportRelativeX(-22000)
    Unknown35()

@State
def ph253_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('ph253eff_00.DIG', '')
        Unknown1007(270000)
        teleportRelativeX(-90000)
        Unknown3032()
        teleportRelativeX(100000)
        Unknown1007(50000)
        Unknown1073(-20000)
        Unknown4007(2)
    sprite('null', 3)
    GFX_0('ph253_effSub', -1)
    sprite('null', 12)
    Unknown4007(0)

@State
def ph253_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown1007(-100000)
    sprite('vr_ph200effpos_00', 2)
    GFX_1('phefcmn_fallwater', 0)
    GFX_1('phefcmn_fallwater', 1)
    GFX_1('phefcmn_fallwater', 2)

@State
def ph254_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1007(250000)
        teleportRelativeX(100000)
        Unknown3032()
        Unknown1072(60000)
        Unknown1096(950)
        Unknown4007(2)
    sprite('vr_ph254_00', 3)
    GFX_1('phef201_kira', 0)
    GFX_1('phef201_kira', 1)
    GFX_1('phef201_kira', 2)
    GFX_1('phef201_kira', 3)
    GFX_1('phef201_kira', 4)
    GFX_1('phef201_kira', 5)
    GFX_1('phef201_kira', 6)
    Unknown1099(3)
    sprite('vr_ph254_01', 3)
    sprite('vr_ph254_02', 3)
    Unknown4007(0)
    Unknown3004(-22)
    sprite('vr_ph254_03', 3)
    sprite('vr_ph254_04', 3)

@State
def ph255_eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('ph202eff_00.DIG', '')
        Unknown1007(210000)
        teleportRelativeX(125000)
        Unknown1056(700)
        Unknown1064(800)
        Unknown1072(40000)
        Unknown4007(2)
    sprite('null', 3)
    GFX_1('phef202_patchin', -1)
    SFX_0('015_blaze_0')
    sprite('null', 3)
    Unknown4007(0)
    sprite('null', 5)
    GFX_1('phef202_hinoko', -1)
    GFX_0('ph255_effSub', -1)

@State
def ph255_effSub():

    def upon_IMMEDIATE():
        Unknown3038(1)
        teleportRelativeX(20000)
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 0)
    Unknown36(1)
    Unknown2005()
    Unknown1096(700)
    Unknown1007(-100000)
    Unknown1072(-40000)
    Unknown35()
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 1)
    Unknown36(1)
    Unknown1056(700)
    Unknown1064(-700)
    Unknown1072(20000)
    teleportRelativeX(-50000)
    Unknown1007(-140000)
    Unknown35()
    sprite('vr_ph202effpos_00', 3)
    GFX_0('phCmnFireEff', 2)
    Unknown36(1)
    Unknown2005()
    Unknown1096(800)
    Unknown1007(-300000)
    teleportRelativeX(100000)
    Unknown1072(-40000)
    Unknown35()

@State
def DriveAtk_NNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1064(4000)
        teleportRelativeX(250000)
        Unknown1007(200000)
        AttackLevel_(3)
        Damage(750)
        AttackP1(90)
        BonusProrationPct(110)
        Unknown9016(1)
        Unknown11057(700)
        AirUntechableTime(35)
        AirPushbackX(15000)
        AirPushbackY(6000)
        Unknown9324(2)
        Unknown9132(45)
        Unknown9144(35)
        Unknown3038(1)

        def upon_11():
            Unknown23078(0)
            Unknown48(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 0):
                Unknown23078(1)
            Unknown21007(3, 32)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_NNN', -1)
    Unknown1056(7500)
    teleportRelativeX(-120000)
    sprite('vr_ph_magictest', 2)
    Unknown1056(15000)
    teleportRelativeX(120000)

@State
def Eff_NNN():

    def upon_IMMEDIATE():
        Unknown4061(2)
        teleportRelativeX(-300000)
        Unknown1007(70000)
        Unknown1096(1000)
    sprite('vr_ph5d_00', 2)
    physicsXImpulse(32000)
    GFX_0('Eff_NNNsub', -1)
    SFX_3('phse_04')
    sprite('vr_ph5d_00', 1)
    physicsXImpulse(1000)
    GFX_1('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_01', 2)
    GFX_1('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_02', 2)
    GFX_1('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_03', 2)
    physicsXImpulse(-1000)
    GFX_1('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_04', 2)
    GFX_1('phef_nnn_nokosi', 0)
    sprite('vr_ph5d_05', 2)
    GFX_1('phef_nnn_nokosi', 0)

@State
def Eff_NNNsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(1)
    sprite('null', 60)
    GFX_2('phef_nnn')
    GFX_0('Eff_NNNsub2', -1)

@State
def Eff_NNNsub2():

    def upon_IMMEDIATE():
        Unknown4003('phef_nnn00', '')
        Unknown3032()
        Unknown23015(1)
        Unknown3001(200)
    sprite('null', 8)
    sprite('null', 2)
    Unknown3004(-26)
    Unknown1056(600)
    Unknown1064(900)
    sprite('null', 2)
    Unknown1056(450)
    Unknown1064(700)
    sprite('null', 5)

@State
def DriveAtk_RNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(6000)
        Unknown1064(11000)
        if (SLOT_19 < 400000):
            Unknown1008()
            Unknown1086(22)
            Unknown1009()
        else:
            teleportRelativeX(400000)
        Unknown1007(75000)
        AttackLevel_(3)
        Damage(900)
        AttackP2(70)
        AirPushbackX(2000)
        AirPushbackY(43000)
        AirUntechableTime(40)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        FatalCounter(1)
        ProjectileHitsWall(1)
        Unknown3038(1)

        def upon_11():
            Unknown23078(0)
            Unknown48(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 256):
                Unknown23078(1)

        def upon_32():
            Damage(1080)
            AttackP2(79)

        def upon_33():
            callSubroutine('RedOnlyAirStatus')
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_RNN', -1)

@State
def Eff_RNN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_rnn00', '')
        Unknown1096(1200)
        Unknown1007(50000)
        ProjectileHitsWall(1)
    sprite('null', 8)
    GFX_0('Eff_RNNsub', -1)
    SFX_0('016_explode_0')
    sprite('null', 3)
    Unknown1065(50)
    sprite('null', 3)
    Unknown1065(50)
    sprite('null', 8)
    Unknown1065(50)
    Unknown3033()
    GFX_0('Eff_RNNsub2', -1)

@State
def Eff_RNNsub2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4003('pheff_rnn01', '')
        Unknown1096(1200)
    sprite('null', 16)
    Unknown3004(-10)

@State
def Eff_RNNsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown1096(800)
    sprite('null', 60)
    GFX_2('phef_rnn_mc')

@State
def DriveAtk_GNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(20000)
        Unknown1064(2500)
        teleportRelativeX(650000)
        Unknown1007(210000)
        AttackLevel_(3)
        Damage(700)
        AttackP2(69)
        Unknown11092(1)
        AirPushbackX(30000)
        AirPushbackY(5000)
        Unknown9202(40)
        GroundedHitstunAnimation(9)
        AirUntechableTime(25)
        Unknown11001(0, 0, 0)
        Unknown11057(500)
        Unknown9016(1)
        PushbackX(39800)
        Unknown23182(3)
        Unknown3038(1)

        def upon_32():
            Damage(840)
            AttackP2(79)

        def upon_33():
            AirPushbackX(50000)
            AirPushbackY(15000)
            AirHitstunAfterWallbounce(28)
            Unknown9178(1)
            WallbounceReboundTime(25)
            Unknown9203()
        Unknown4010(3)

        def upon_11():
            Unknown23078(0)
            Unknown48(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 16):
                Unknown23078(1)
    sprite('vr_ph_magictest', 1)
    GFX_0('Eff_GNN', -1)
    GFX_0('Eff_GNN', -1)
    Unknown21007(1, 32)
    GFX_0('Eff_GNN', -1)
    Unknown21007(1, 33)
    SFX_0('011_spin_0')
    SFX_0('011_spin_0')
    SFX_0('011_spin_1')
    SFX_3('phse_01')
    Unknown1056(15000)
    teleportRelativeX(-400000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    Unknown1056(25000)
    teleportRelativeX(160000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    Unknown1056(40000)
    teleportRelativeX(240000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    ExitState()

@State
def DriveAtk_GNN_PU():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(40000)
        Unknown1064(2500)
        teleportRelativeX(650000)
        Unknown1007(210000)
        AttackLevel_(3)
        Damage(350)
        AirPushbackX(30000)
        AirPushbackY(5000)
        Unknown9202(40)
        AirUntechableTime(25)
        AttackP2(96)
        GroundedHitstunAnimation(9)
        Unknown11001(0, 0, 0)
        YImpluseBeforeWallbounce(1800)
        PushbackX(39800)
        Hitstop(3)
        Unknown11057(500)
        Unknown9016(1)
        Unknown23182(3)
        Unknown3038(1)

        def upon_33():
            AirPushbackX(50000)
            AirPushbackY(15000)
            AirHitstunAfterWallbounce(28)
            Unknown9178(1)
            WallbounceReboundTime(25)
            Unknown9203()
        Unknown4010(3)

        def upon_11():
            Unknown23078(0)
            Unknown48(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 16):
                Unknown23078(1)
    sprite('vr_ph_magictest', 1)
    GFX_0('Eff_GNN', -1)
    GFX_0('Eff_GNN', -1)
    Unknown21007(1, 32)
    Unknown21007(1, 34)
    GFX_0('Eff_GNN', -1)
    Unknown21007(1, 33)
    Unknown21007(1, 34)
    SFX_0('011_spin_0')
    SFX_0('011_spin_0')
    SFX_0('011_spin_1')
    SFX_3('phse_01')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    ExitState()

@State
def Eff_GNN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_gnn00', '')
        teleportRelativeX(-500000)
        Unknown1007(40000)
        Unknown1096(700)
        Unknown1065(-200)

        def upon_32():
            Unknown3001(0)
            Unknown2037(3)
            teleportRelativeX(350000)

        def upon_33():
            Unknown3001(0)
            Unknown2037(6)
            teleportRelativeX(700000)

        def upon_34():
            Unknown3001(255)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                Unknown2038(-1)
                if (not SLOT_2):
                    Unknown3001(255)
    sprite('null', 1)
    sprite('null', 1)
    GFX_1('phef_gnn_moya02', -1)
    if (not SLOT_2):
        GFX_1('phef_gnn_mc', -1)
    GFX_0('Eff_GNNsub', -1)
    sprite('null', 2)
    GFX_0('Eff_GNNsub', -1)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown35()
    sprite('null', 12)
    ExitState()

@State
def Eff_GNNsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_gnn01', '')
    sprite('null', 8)
    Unknown1099(15)
    sprite('null', 10)
    Unknown3004(-26)

@State
def DriveAtk_BNN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(14500)
        Unknown1064(4000)
        teleportRelativeX(330000)
        Unknown1007(180000)
        AttackLevel_(3)
        Damage(800)
        AttackP2(69)
        AirPushbackX(100)
        AirPushbackY(28000)
        Hitstop(6)
        Unknown11001(5, 5, 7)
        FreezeCount(1)
        FreezeDuration(36)
        ChipDamagePct(40)
        Unknown3038(1)

        def upon_11():
            Unknown23078(0)
            Unknown48(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 1):
                Unknown23078(1)

        def upon_32():
            Damage(960)
            AttackP2(79)

        def upon_33():
            callSubroutine('BlueOnlyAirStatus')
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_BNN', -1)

@State
def Eff_BNN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_bnn00', '')
        Unknown1096(1000)
        teleportRelativeX(-100000)
        Unknown1007(35000)
    sprite('null', 5)
    GFX_0('Eff_BNNsub', -1)
    sprite('null', 4)
    Unknown1097(100)
    sprite('null', 3)
    Unknown1097(-50)
    Unknown3001(200)
    sprite('null', 3)
    Unknown1097(-50)
    Unknown3001(100)
    GFX_1('phef_bnn_moya', -1)

@State
def Eff_BNNsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_bnn01', '')
        Unknown1096(750)
        GFX_1('phef_bnn_mc', -1)
    sprite('null', 5)
    SFX_0('017_freeze_1')
    Unknown1097(200)
    sprite('null', 5)
    Unknown1097(200)
    sprite('null', 2)
    Unknown1097(-200)
    sprite('null', 2)
    SFX_0('018_ice_break_1')
    Unknown1097(-200)

@State
def DriveAtk_RRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(6000)
        Unknown1064(13000)
        if (SLOT_19 < 400000):
            Unknown1008()
            Unknown1086(22)
            Unknown1009()
        else:
            teleportRelativeX(400000)
        Unknown1007(75000)
        AttackLevel_(4)
        Damage(1200)
        AttackP2(75)
        AirPushbackX(1000)
        AirPushbackY(43000)
        AirUntechableTime(45)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        FatalCounter(1)
        ProjectileHitsWall(1)
        Unknown3038(1)

        def upon_11():
            Unknown23078(0)
            Unknown48(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 512):
                Unknown23078(1)

        def upon_32():
            Damage(1440)
            AttackP2(82)

        def upon_33():
            callSubroutine('RedOnlyAirStatus')
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_RRN', -1)

@State
def Eff_RRN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_rnn00', '')
        Unknown1096(1350)
        Unknown1007(50000)
        ProjectileHitsWall(1)
    sprite('null', 8)
    GFX_0('Eff_RNNsub', -1)
    GFX_0('Eff_RRNsub2Mato', -1)
    SFX_0('016_explode_1')
    sprite('null', 3)
    Unknown1065(50)
    sprite('null', 3)
    Unknown1065(50)
    sprite('null', 8)
    Unknown1065(50)
    Unknown3033()
    GFX_0('Eff_RRNsub', -1)

@State
def Eff_RRNsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4003('pheff_rnn01', '')
        Unknown1096(1350)
    sprite('null', 16)
    Unknown3004(-10)

@State
def Eff_RRNsub2Mato():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
    sprite('null', 4)
    GFX_1('phef_rrn_bg', -1)
    GFX_0('Eff_RRNsub2', -1)
    Unknown36(1)
    Unknown1072(25500)
    Unknown35()
    sprite('null', 4)
    GFX_0('Eff_RRNsub2', -1)
    Unknown36(1)
    Unknown1007(100000)
    Unknown1097(-125)
    Unknown2005()
    Unknown1072(-25500)
    Unknown35()
    sprite('null', 4)
    GFX_0('Eff_RRNsub2', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown1097(-125)
    Unknown1072(25500)
    Unknown35()

@State
def Eff_RRNsub2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_rrn00', '')
        Unknown1096(1450)
        Unknown3001(255)
    sprite('null', 15)
    Unknown1099(20)
    sprite('null', 4)
    Unknown3004(-51)

@State
def DriveAtk_GGN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(40000)
        Unknown1064(2500)
        teleportRelativeX(650000)
        Unknown1007(210000)
        AttackLevel_(4)
        Damage(500)
        AttackP2(72)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(5000)
        Unknown9202(40)
        AirUntechableTime(25)
        GroundUntechableTime(5)
        Hitstop(4)
        Unknown11001(0, 0, 0)
        Unknown11057(500)
        Unknown9016(1)
        PushbackX(60800)
        Unknown23182(3)
        Unknown3038(1)

        def upon_32():
            Unknown2037(1)
            AttackP2(82)

        def upon_33():
            AirPushbackX(55000)
            AirPushbackY(12500)
            AirHitstunAfterWallbounce(28)
            Unknown9178(1)
            WallbounceReboundTime(22)
            Unknown9203()
        Unknown4010(3)

        def upon_11():
            Unknown23078(0)
            Unknown48(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 32):
                Unknown23078(1)
    sprite('vr_ph_magictest', 1)
    Damage(500)
    if SLOT_2:
        Damage(600)
    RefreshMultihit()
    GFX_0('Eff_GGN', -1)
    GFX_0('Eff_GGN', -1)
    Unknown21007(1, 32)
    GFX_0('Eff_GGN', -1)
    Unknown21007(1, 33)
    SFX_0('011_spin_2')
    SFX_0('011_spin_2')
    SFX_0('006_swing_blade_2')
    SFX_0('022_magiccircle_b')
    Unknown1056(15000)
    teleportRelativeX(-400000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    Damage(800)
    if SLOT_2:
        Damage(960)
    RefreshMultihit()
    Unknown1056(25000)
    teleportRelativeX(160000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    Unknown1056(40000)
    teleportRelativeX(240000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    ExitState()

@State
def DriveAtk_GGN_PU():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(40000)
        Unknown1064(2500)
        teleportRelativeX(650000)
        Unknown1007(210000)
        AttackLevel_(4)
        Damage(250)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(5000)
        Unknown9202(45)
        AirUntechableTime(25)
        GroundUntechableTime(5)
        AttackP2(97)
        YImpluseBeforeWallbounce(1800)
        PushbackX(37500)
        Hitstop(2)
        Unknown11001(0, 0, 0)
        Unknown11057(500)
        Unknown9016(1)
        PushbackX(60800)
        Unknown23182(3)
        Unknown3038(1)

        def upon_33():
            AirPushbackX(50000)
            AirPushbackY(12500)
            AirHitstunAfterWallbounce(28)
            Unknown9178(1)
            WallbounceReboundTime(22)
            Unknown9203()
        Unknown4010(3)

        def upon_11():
            Unknown23078(0)
            Unknown48(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 32):
                Unknown23078(1)
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    GFX_0('Eff_GGN', -1)
    GFX_0('Eff_GGN', -1)
    Unknown21007(1, 32)
    Unknown21007(1, 34)
    GFX_0('Eff_GGN', -1)
    Unknown21007(1, 33)
    Unknown21007(1, 34)
    SFX_0('011_spin_2')
    SFX_0('011_spin_2')
    SFX_0('006_swing_blade_2')
    SFX_0('022_magiccircle_b')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    ExitState()

@State
def Eff_GGN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_ggn00', '')
        teleportRelativeX(-500000)
        Unknown1007(40000)
        Unknown1096(700)
        Unknown1065(-150)
        Unknown1072(2000)

        def upon_32():
            Unknown3001(0)
            Unknown2037(3)
            teleportRelativeX(350000)

        def upon_33():
            Unknown3001(0)
            Unknown2037(6)
            teleportRelativeX(700000)

        def upon_34():
            Unknown3001(255)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                Unknown2038(-1)
                if (not SLOT_2):
                    Unknown3001(255)
    sprite('null', 1)
    sprite('null', 1)
    GFX_1('phef_ggn_moya02', -1)
    if (not SLOT_2):
        GFX_0('Eff_GNNmc', -1)
    GFX_0('Eff_GGNsub', -1)
    sprite('null', 2)
    GFX_0('Eff_GGNsub', -1)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown35()
    sprite('null', 12)
    ExitState()

@State
def Eff_GGNsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_gnn01', '')
    sprite('null', 8)
    Unknown1099(30)
    sprite('null', 10)
    Unknown3004(-26)

@State
def Eff_GNNmc():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('phef_gnn_mc')
    sprite('null', 20)

@State
def DriveAtk_BBN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(16000)
        Unknown1064(4000)
        teleportRelativeX(305000)
        Unknown1007(180000)
        AttackLevel_(4)
        Damage(1000)
        AttackP2(72)
        AirPushbackX(100)
        AirPushbackY(28000)
        Hitstop(7)
        Unknown11001(5, 5, 10)
        FreezeCount(1)
        FreezeDuration(36)
        ChipDamagePct(40)
        Unknown3038(1)

        def upon_11():
            Unknown23078(0)
            Unknown48(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 2):
                Unknown23078(1)

        def upon_32():
            Damage(1200)
            AttackP2(82)

        def upon_33():
            callSubroutine('BlueOnlyAirStatus')
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_BBN', -1)

@State
def Eff_BBN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_bbn00', '')
        Unknown1096(1000)
        Unknown1057(100)
        teleportRelativeX(-125000)
        Unknown1007(25000)
    sprite('null', 5)
    GFX_0('Eff_BNNsub', -1)
    Unknown36(1)
    Unknown1097(150)
    Unknown35()
    SFX_0('017_freeze_1')
    sprite('null', 4)
    Unknown1097(100)
    sprite('null', 3)
    Unknown1097(-50)
    Unknown3001(200)
    sprite('null', 3)
    Unknown1097(-50)
    Unknown3001(100)
    Unknown3033()
    GFX_1('phef_bbb', -1)
    SFX_0('018_ice_break_1')

@State
def DriveAtk_BGN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown4008(3)
        Unknown4025(3)
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        AirUntechableTime(30)
        AirPushbackY(12000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11032('f049020010b6fdffe0930400206cfbff')
        StarterRating(2)
        Unknown1007(300000)
        teleportRelativeX(100000)
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown4054(7)
        Unknown23067('phef_bgn_00')
        Unknown23015(8)
        Unknown4061(0)
        Unknown1096(1000)
        Unknown3032()
        FireBallMultiHit(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 2)

        def upon_CLEAR_OR_EXIT():
            if (not Unknown48(23, 2, 0, 3, 2, 23)):
                if Unknown68('0100000000000000000000000000000000000000'):
                    Unknown2071('03000000c0d40100000000001400000001000000')
                else:
                    Unknown2071('03000000c0d40100803801001400000001000000')
            else:
                Unknown48(23, 2, 0, 3, 2, 13)
                if (not (0 >= SLOT_0)):
                    Unknown2071('03000000c0d4010080c7feff1400000001000000')
                else:
                    Unknown2071('03000000c0d40100000000001400000001000000')
        loopRelated(17, 180)

        def upon_17():
            sendToLabel(1)

        def upon_32():
            sendToLabel(1)
    sprite('vr_ph', 4)
    StartMultihit()
    setGravity(-200)
    SFX_3('phse_04')
    Unknown3004(51)
    GFX_0('Eff_BGNeye', -1)
    Unknown38(4, 1)
    label(0)
    sprite('vr_ph', 30)
    Unknown1039(-100)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_ph', 10)
    Unknown1084(1)
    clearUponHandler(3)
    clearUponHandler(17)
    clearUponHandler(54)
    clearUponHandler(32)
    Unknown2001()
    Unknown3004(-26)
    Unknown4061(2)
    Unknown4047(1, 1, 1)
    Unknown4045('706865665f62676e5f656e640000000000000000000000000000000000000000ffffffff')
    ExitState()
    label(2)
    sprite('vr_ph', 10)
    Unknown1084(1)
    clearUponHandler(3)
    clearUponHandler(17)
    clearUponHandler(54)
    clearUponHandler(32)
    Unknown2001()
    Unknown3004(-26)
    Unknown4061(2)
    Unknown4047(1, 1, 1)
    GFX_1('phef216_smoke', -1)

@State
def DriveDef_BGN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown3038(1)
        Unknown4008(2)

        def upon_35():
            clearUponHandler(32)
            clearUponHandler(35)
            clearUponHandler(14)
            sendToLabel(2)

        def upon_14():
            clearUponHandler(32)
            clearUponHandler(35)
            clearUponHandler(14)
            sendToLabel(2)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(35)
            clearUponHandler(14)
            sendToLabel(1)

        def upon_33():
            setInvincible(0)
            Unknown21007(4, 34)

        def upon_34():
            setInvincible(1)
            Unknown21007(4, 35)

        def upon_STATE_END():
            SLOT_8 = 0
        Unknown23022(1)
        Unknown2003(1)
        Unknown23142(1)
        Unknown1056(7000)
        Unknown1064(14000)

        def upon_CLEAR_OR_EXIT():
            if (not Unknown48(23, 2, 0, 3, 2, 23)):
                Unknown2071('0300000000000000702ffcff6400000001000000')
            else:
                Unknown48(23, 2, 0, 3, 2, 13)
                if (not (0 >= SLOT_0)):
                    Unknown2071('0300000000000000e040fdff6400000001000000')
                else:
                    Unknown2071('0300000000000000702ffcff6400000001000000')
    sprite('null', 13)
    Unknown3001(128)
    Unknown22009(1)
    GFX_0('Eff_BGN', -1)
    Unknown38(4, 1)
    sprite('vr_ph_magictestEx01', 600)
    SLOT_8 = 180
    label(1)
    sprite('vr_ph_magictestEx01', 8)
    Unknown21007(4, 32)
    sprite('null', 10)
    SLOT_8 = 0
    ExitState()
    label(2)
    sprite('null', 10)
    Unknown21007(4, 33)
    SLOT_8 = 0
    ExitState()

@State
def Eff_BGN():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown4054(7)
        Unknown23067('phef_bgn_00')
        Unknown23015(8)
        Unknown1007(300000)
        teleportRelativeX(100000)
        Unknown4025(3)
        Unknown4010(2)
        Unknown4008(2)
        Unknown4061(0)
        Unknown1096(1000)
        Unknown3032()
        Unknown3001(0)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)

        def upon_34():
            Unknown3001(255)
            Unknown3004(0)
            Unknown4025(3)
            Unknown21007(4, 32)

        def upon_35():
            Unknown3001(0)
            Unknown3004(0)
            Unknown4025(0)
            Unknown21007(4, 33)

        def upon_CLEAR_OR_EXIT():
            Unknown2071('03000000a0860100803801003200000001000000')
    sprite('null', 5)
    sprite('null', 5)
    SFX_3('phse_04')
    sprite('vr_ph', 4)
    Unknown3004(51)
    GFX_0('Eff_BGNeye', -1)
    Unknown38(4, 1)
    label(0)
    sprite('vr_ph', 20)
    physicsYImpulse(-1500)
    sprite('vr_ph', 10)
    physicsYImpulse(-750)
    sprite('vr_ph', 5)
    physicsYImpulse(-375)
    sprite('vr_ph', 20)
    physicsYImpulse(1500)
    sprite('vr_ph', 10)
    physicsYImpulse(750)
    sprite('vr_ph', 5)
    physicsYImpulse(375)
    gotoLabel(0)
    label(1)
    sprite('vr_ph', 10)
    Unknown3004(-26)
    Unknown4061(2)
    Unknown4047(1, 1, 1)
    Unknown4045('706865665f62676e5f656e640000000000000000000000000000000000000000ffffffff')
    ExitState()
    label(2)
    sprite('vr_ph', 10)
    Unknown3004(-26)
    Unknown4061(2)
    Unknown4047(1, 1, 1)
    Unknown4045('706865665f62676e5f656e640000000000000000000000000000000000000000ffffffff')
    GFX_1('phef_bgn_guard', -1)
    ExitState()

@State
def Eff_BGNeye():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(2)
        Unknown4019(3)
        Unknown4047(1, 1, 1)
        Unknown4054(9)
        Unknown23067('phef_bgn_00b')
        Unknown4025(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4008(2)
    label(0)
    sprite('null', 32767)
    Unknown3001(255)
    loopRest()
    label(1)
    sprite('null', 32767)
    Unknown3001(0)
    loopRest()

@State
def DriveAtk_BRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(6000)
        Unknown1064(6000)
        teleportRelativeX(200000)
        Unknown1007(150000)
        AttackLevel_(4)
        Damage(1000)
        AttackP2(82)
        BonusProrationPct(110)
        Hitstop(0)
        ProjectileDurabilityLvl(1)
        Unknown11001(10, 10, 15)
        AirPushbackX(2500)
        AirPushbackY(20000)
        AirUntechableTime(100)
        AttackP1(80)
        AirHitstunAnimation(14)
        GroundedHitstunAnimation(14)
        Unknown53(1)
        Unknown3038(1)
        StarterRating(2)
        FireBallMultiHit(1, 1, 1, 1, 1, 0, 1, 1)
        sendToLabelUpon(54, 1)

        def upon_32():
            clearUponHandler(10)
            clearUponHandler(32)
            Unknown2037(0)
            sendToLabel(1)
    sprite('vr_ph_magictest', 14)
    Unknown2037(18)
    GFX_0('Eff_BRN', -1)
    SFX_3('phse_04')
    GFX_1('phef_rbn_mc', -1)
    label(0)
    sprite('vr_ph_magictest', 13)
    RefreshMultihit()
    GFX_0('Eff_BRN', -1)
    teleportRelativeX(120000)
    if (SLOT_2 <= 12):
        teleportRelativeX(-20000)
    if (SLOT_2 <= 9):
        teleportRelativeX(-20000)
    if (SLOT_2 <= 6):
        teleportRelativeX(-20000)
    sprite('vr_ph_magictest', 1)
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(0)
    label(1)
    sprite('null', 10)
    clearUponHandler(54)
    clearUponHandler(32)

@State
def Eff_BRN():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown3032()
        Unknown4003('pheff_brn00', '')
        GFX_2('phef_brn_00')
        Unknown1007(75000)
    sprite('null', 2)
    Unknown3001(255)
    GFX_1('phef_brn_00a2', -1)
    GFX_0('Eff_BRNsub', -1)
    SFX_0('014_electric_sl')
    sprite('null', 2)
    Unknown1077(-90000, 90000)
    Unknown3001(255)
    GFX_0('Eff_BRNsub', -1)
    sprite('null', 2)
    GFX_0('Eff_BRNsub', -1)
    sprite('null', 2)
    Unknown1077(-90000, 90000)
    sprite('null', 2)
    sprite('null', 2)
    Unknown3033()
    Unknown1096(1075)
    Unknown1077(-90000, 90000)
    sprite('null', 2)
    sprite('null', 3)
    Unknown1096(1100)

@State
def Eff_BRNsub():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4003('pheff_brn01', '')
        Unknown1096(750)
        Unknown1102(-50, 250)
        Unknown1077(-360000, 360000)
    sprite('null', 2)
    sprite('null', 1)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(128)
    sprite('null', 1)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(128)
    sprite('null', 1)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(128)

@State
def DriveAtk_GRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(6500)
        Unknown1064(13000)
        Unknown1007(75000)
        AttackLevel_(4)
        Damage(700)
        AirPushbackX(20000)
        AirPushbackY(5000)
        Unknown9202(19)
        GroundedHitstunAnimation(9)
        AttackP1(80)
        Unknown11084(1)
        StarterRating(2)
        Unknown3038(1)

        def upon_11():
            clearUponHandler(11)
            Unknown21007(2, 34)
    sprite('vr_ph_magictest', 5)

@State
def DriveReAtk_GRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown4007(2)
        Unknown1056(4000)
        Unknown1064(13000)
        teleportRelativeX(0)
        Unknown1007(75000)
        AttackLevel_(4)
        Damage(500)
        AttackP2(100)
        AirPushbackX(40000)
        AirPushbackY(25000)
        AirHitstunAfterWallbounce(40)
        WallbounceReboundTime(0)
        Unknown9178(1)
        Hitstop(6)
        AirUntechableTime(60)
        GroundedHitstunAnimation(10)
        AttackP1(80)
        GroundUntechableTime(1)
        StarterRating(2)
        Unknown3038(1)

        def upon_32():
            clearUponHandler(32)
            Unknown2001()
    sprite('null', 1)
    sprite('vr_ph_magictest', 15)

@State
def DriveDef_GRN():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown3038(1)
        Unknown4011(0)
        teleportRelativeX(100000)
        setInvincible(1)
        Unknown22024(3000)
        GuardPoint_(1)
        Unknown22019('0000000000000000000000000100000000000000')
        Unknown22026(0)
        Unknown23013(1)
        ProjectileHitsWall(1)
        EnableCollision(1)
        Unknown2015(105)
        Unknown23087(-100000)

        def upon_40():
            Unknown23023()
            SFX_0('100_hit_grap_2')
            GFX_1('ef_hitmd', 0)
            physicsXImpulse(100000)
            GFX_0('DriveReAtk_GRN', -1)
            Unknown4009(3)

            def upon_CLEAR_OR_EXIT():
                Unknown1019(90)

        def upon_41():
            Unknown23023()
            SFX_0('100_hit_grap_2')
            GFX_1('ef_hitmd', 0)
            physicsXImpulse(-50000)
            GFX_0('DriveReAtk_GRN', -1)

        def upon_44():
            clearUponHandler(44)
            sendToLabel(1)

        def upon_34():
            teleportRelativeX(50000)
            EnableCollision(0)
            SLOT_51 = 10

            def upon_CLEAR_OR_EXIT():
                SLOT_51 = (SLOT_51 + (-1))
                if (SLOT_51 <= 0):
                    EnableCollision(1)

        def upon_32():
            EnableCollision(0)
            sendToLabel(1)
        Unknown23021(1)

        def upon_14():
            EnableCollision(0)
            sendToLabel(1)
        Unknown2037(0)

        def upon_42():
            Unknown21007(3, 40)
            Unknown48(23, 2, 0, 22, 2, 38)
            if op(15, 2, 0, 2, 38):
                if (SLOT_2 == 0):
                    sendToLabel(2)
                if (SLOT_2 == 1):
                    sendToLabel(3)
                if (SLOT_2 == 2):
                    sendToLabel(4)
                Unknown2038(1)
                if (SLOT_2 >= 3):
                    Unknown2037(0)
        Unknown2003(1)
    sprite('null', 1)
    GFX_0('DriveAtk_GRN', -1)
    GFX_0('Eff_GRN', -1)
    Unknown38(4, 1)
    SFX_3('phse_04')
    sprite('phdrivecol_grn', 10)
    Unknown3001(128)
    physicsXImpulse(20000)
    sprite('phdrivecol_grn', 10)
    Unknown1019(60)
    sprite('phdrivecol_grn', 10)
    Unknown1019(60)
    sprite('phdrivecol_grn', 10)
    Unknown1019(60)
    sprite('phdrivecol_grn', 10)
    Unknown1019(60)
    sprite('phdrivecol_grn', 10)
    Unknown1019(60)
    label(0)
    sprite('phdrivecol_grn', 300)
    Unknown1019(60)
    label(1)
    sprite('null', 10)
    clearUponHandler(42)
    clearUponHandler(14)
    clearUponHandler(44)
    clearUponHandler(32)
    clearUponHandler(40)
    clearUponHandler(41)
    Unknown21012('DriveReAtk_GRN', 32)
    Unknown21007(4, 32)
    ExitState()
    label(2)
    sprite('phdrivecol_grn', 30)
    GFX_0('DriveDef_GRN_ATK', 0)
    GFX_0('Eff_GRNatk', -1)
    sendToLabel(0)
    ExitState()
    label(3)
    sprite('phdrivecol_grn', 30)
    GFX_0('DriveDef_GRN_ATK', 1)
    GFX_0('Eff_GRNatk', -1)
    sendToLabel(0)
    ExitState()
    label(4)
    sprite('phdrivecol_grn', 30)
    GFX_0('DriveDef_GRN_ATK', 2)
    GFX_0('Eff_GRNatk', -1)
    sendToLabel(0)
    ExitState()

@State
def DriveDef_GRN_ATK():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(4000)
        Unknown1064(2000)
        AttackLevel_(3)
        Damage(650)
        ProjectileDurabilityLvl(2)
        Unknown9016(1)
        Hitstop(3)
        Unknown11084(1)
        Unknown11057(300)
        Unknown11001(8, 8, 10)
        AttackP1(50)
        AttackP2(94)
        Unknown11089(-1)
        GroundedHitstunAnimation(2)
        StarterRating(2)
        Unknown3032()
        Unknown4003('pheff_grn02', '')
        Unknown4061(2)
        Unknown21004(1)
        Unknown3038(1)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(51)
    Unknown21012('Eff_GRNmc', 32)
    GFX_0('Eff_GRNmc', -1)
    sprite('vr_ph_magictest', 30)
    physicsXImpulse(120000)
    GFX_0('Eff_GRNnokosi', -1)

@State
def Eff_GRN():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_grn00', '')
        Unknown4007(2)
        Unknown4010(2)
        Unknown1096(500)
        Unknown3001(0)
        Unknown1007(200000)
        Unknown4061(2)
        Unknown21004(1)
        sendToLabelUpon(32, 1)
    sprite('null', 5)
    Unknown4045('706865665f726e6e5f7374617274000000000000000000000000000000000000ffffffff')
    GFX_0('Eff_GRNsub', -1)
    Unknown1056(0)
    Unknown1059(100)
    Unknown3004(51)
    gotoLabel(0)
    label(0)
    sprite('null', 20)
    Unknown1059(0)
    physicsYImpulse(400)
    Unknown3004(-2)
    Unknown4047(1, 1, 1)
    Unknown4045('706865665f726e6e5f6a697a6f6b750000000000000000000000000000000000ffffffff')
    sprite('null', 10)
    physicsYImpulse(200)
    sprite('null', 20)
    Unknown4047(1, 1, 1)
    Unknown4045('706865665f726e6e5f6a697a6f6b750000000000000000000000000000000000ffffffff')
    Unknown3004(2)
    physicsYImpulse(-400)
    sprite('null', 10)
    physicsYImpulse(-200)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Unknown4047(1, 1, 1)
    Unknown4045('706865665f726e6e5f656e640000000000000000000000000000000000000000ffffffff')
    Unknown3004(-51)
    Unknown1059(-60)
    Unknown1067(60)
    loopRest()

@State
def Eff_GRNsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_grn01', '')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4025(2)
        Unknown4013(2)
    sprite('null', 32767)

@State
def Eff_GRNatk():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        Unknown21004(1)
        Unknown4003('pheff_grn01', '')
        Unknown1096(650)
        Unknown1007(200000)
    sprite('null', 5)
    Unknown1067(7)
    Unknown1059(15)
    sprite('null', 5)
    Unknown3004(-51)

@State
def Eff_GRNmc():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown23067('phef_grn_atk00')

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)
    sprite('null', 55)
    label(1)
    sprite('null', 5)

@State
def Eff_GRNnokosi():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4061(2)
    label(0)
    sprite('null', 2)
    Unknown4047(1, 1, 1)
    Unknown4045('706865665f67726e5f6e6f6b6f73690000000000000000000000000000000000ffffffff')
    gotoLabel(0)

@State
def DriveAtk_RRR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(6000)
        Unknown1064(15000)
        if (SLOT_19 < 400000):
            Unknown1008()
            Unknown1086(22)
            Unknown1009()
        else:
            teleportRelativeX(400000)
        Unknown1007(75000)
        AttackLevel_(5)
        Damage(1500)
        AttackP2(75)
        AirPushbackX(0)
        AirPushbackY(45000)
        AirUntechableTime(90)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        FatalCounter(1)
        ProjectileHitsWall(1)
        Unknown3038(1)

        def upon_11():
            Unknown23078(0)
            Unknown48(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 768):
                Unknown23078(1)

        def upon_32():
            Damage(1800)
            AttackP2(84)

        def upon_33():
            callSubroutine('RedOnlyAirStatus')
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_RRR', -1)

@State
def Eff_RRR():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_rrr01', '')
        Unknown1064(1750)
        Unknown1056(1500)
        Unknown1007(50000)
        ProjectileHitsWall(1)
    sprite('null', 8)
    GFX_0('Eff_RNNsub', -1)
    GFX_0('Eff_RRRsub2Mato', -1)
    SFX_0('016_explode_2')
    ScreenShake(5000, 5000)
    sprite('null', 3)
    Unknown1065(25)
    sprite('null', 3)
    Unknown1065(25)
    sprite('null', 8)
    Unknown1065(25)
    Unknown3033()
    GFX_0('Eff_RRRsub', -1)

@State
def Eff_RRRsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4003('pheff_rnn01', '')
        Unknown1096(1350)
    sprite('null', 16)
    Unknown3004(-10)

@State
def Eff_RRRsub2Mato():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
    sprite('null', 6)
    GFX_1('phef_rrr_bg', -1)
    GFX_0('Eff_RRRsub2', -1)
    Unknown36(1)
    Unknown1072(25500)
    Unknown35()
    sprite('null', 6)
    GFX_0('Eff_RRRsub2', -1)
    Unknown36(1)
    Unknown1007(100000)
    Unknown1097(-125)
    Unknown2005()
    Unknown1072(-25500)
    Unknown35()
    sprite('null', 6)
    GFX_0('Eff_RRRsub2', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown1097(100)
    Unknown1072(25500)
    Unknown35()
    sprite('null', 12)

@State
def Eff_RRRsub2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4003('pheff_rrr00', '')
        Unknown1096(1450)
        Unknown3001(255)
    sprite('null', 14)
    Unknown1099(20)
    sprite('null', 4)
    Unknown3004(-51)

@State
def Wind_Herald():

    def upon_IMMEDIATE():
        Unknown1007(260000)
        Unknown1056(700)
        GFX_2('phef_g_yotyou')
    sprite('null', 7)
    sprite('null', 4)
    Unknown3004(-51)

@State
def DriveAtk_GGG():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(40000)
        Unknown1064(2500)
        teleportRelativeX(650000)
        Unknown1007(210000)
        AttackLevel_(5)
        Damage(500)
        AttackP2(75)
        StarterRating(3)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(5000)
        Unknown9202(60)
        AirUntechableTime(30)
        Hitstop(2)
        Unknown9362(1)
        Unknown9364(25)
        GroundedHitstunAnimation(10)
        Unknown11001(0, 0, 0)
        Unknown11057(500)
        Unknown9016(1)
        PushbackX(79800)
        Unknown23182(3)
        Unknown3038(1)

        def upon_12():
            PushbackX(78000)

        def upon_32():
            Unknown2037(1)
            AttackP2(84)

        def upon_33():
            AirPushbackX(60000)
            AirPushbackY(8000)
            AirHitstunAfterWallbounce(48)
            Unknown9178(1)
            WallbounceReboundTime(23)
            Unknown9203()
        Unknown4010(3)

        def upon_11():
            Unknown23078(0)
            Unknown48(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 48):
                Unknown23078(1)
    sprite('vr_ph_magictest', 1)
    Damage(350)
    if SLOT_2:
        Damage(420)
    RefreshMultihit()
    GFX_0('Eff_GGG', -1)
    GFX_0('Eff_GGG', -1)
    Unknown21007(1, 32)
    GFX_0('Eff_GGG', -1)
    Unknown21007(1, 33)
    SFX_3('phse_03')
    ScreenShake(5000, 5000)
    Unknown1056(15000)
    teleportRelativeX(-400000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    Damage(600)
    if SLOT_2:
        Damage(720)
    RefreshMultihit()
    Unknown1056(25000)
    teleportRelativeX(160000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    Damage(1000)
    if SLOT_2:
        Damage(1200)
    RefreshMultihit()
    Unknown1056(40000)
    teleportRelativeX(240000)
    sprite('vr_ph_magictest', 1)
    sprite('vr_ph_magictest', 1)
    ExitState()

@State
def DriveAtk_GGG_PU():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(40000)
        Unknown1064(2500)
        teleportRelativeX(650000)
        Unknown1007(210000)
        AttackLevel_(5)
        Damage(210)
        StarterRating(3)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(5000)
        Unknown9202(60)
        AirUntechableTime(30)
        Hitstop(1)
        AttackP2(98)
        YImpluseBeforeWallbounce(1800)
        Unknown9362(1)
        Unknown9364(25)
        GroundedHitstunAnimation(10)
        PushbackX(59900)
        Unknown11001(0, 0, 0)
        Unknown11057(500)
        Unknown9016(1)
        PushbackX(79800)
        Unknown23182(3)
        Unknown3038(1)

        def upon_12():
            PushbackX(58000)
            PushbackX(78000)

        def upon_33():
            AirPushbackX(45000)
            AirPushbackY(8000)
            AirHitstunAfterWallbounce(48)
            Unknown9178(1)
            WallbounceReboundTime(23)
            Unknown9203()
        Unknown4010(3)

        def upon_11():
            Unknown23078(0)
            Unknown48(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 48):
                Unknown23078(1)
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    GFX_0('Eff_GGG', -1)
    GFX_0('Eff_GGG', -1)
    Unknown21007(1, 32)
    Unknown21007(1, 34)
    GFX_0('Eff_GGG', -1)
    Unknown21007(1, 33)
    Unknown21007(1, 34)
    SFX_3('phse_03')
    ScreenShake(5000, 5000)
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    ExitState()

@State
def Eff_GGG():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_ggg00', '')
        teleportRelativeX(-500000)
        Unknown1007(40000)
        Unknown1096(750)
        Unknown1065(-300)
        Unknown1072(2000)

        def upon_32():
            Unknown3001(0)
            Unknown2037(3)
            teleportRelativeX(350000)

        def upon_33():
            Unknown3001(0)
            Unknown2037(6)
            teleportRelativeX(700000)

        def upon_34():
            Unknown3001(255)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                Unknown2038(-1)
                if (not SLOT_2):
                    Unknown3001(255)
    sprite('null', 1)
    sprite('null', 1)
    if (not SLOT_2):
        GFX_0('Eff_GNNmc', -1)
    GFX_1('phef_ggg_moya03', -1)
    GFX_0('Eff_GGGsub', -1)
    Unknown1065(50)
    sprite('null', 2)
    GFX_0('Eff_GGGsub', -1)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown35()
    Unknown1065(-50)
    sprite('null', 2)
    Unknown1065(50)
    sprite('null', 2)
    Unknown1065(-50)
    sprite('null', 2)
    Unknown1065(50)
    sprite('null', 1)
    sprite('null', 5)
    ExitState()

@State
def Eff_GGGsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_gnn01', '')
    sprite('null', 8)
    Unknown1099(45)
    sprite('null', 10)
    Unknown3004(-26)

@State
def DriveAtk_BBB():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(17500)
        Unknown1064(5000)
        teleportRelativeX(280000)
        Unknown1007(170000)
        AttackLevel_(5)
        Damage(1250)
        AttackP2(75)
        AirPushbackX(100)
        AirPushbackY(28000)
        Hitstop(8)
        Unknown11001(5, 5, 13)
        FreezeCount(1)
        FreezeDuration(45)
        ChipDamagePct(40)
        Unknown3038(1)

        def upon_11():
            Unknown23078(0)
            Unknown48(23, 2, 0, 3, 2, 53)
            if (SLOT_0 == 3):
                Unknown23078(1)

        def upon_32():
            Damage(1500)
            AttackP2(84)

        def upon_33():
            callSubroutine('BlueOnlyAirStatus')
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_BBB', -1)

@State
def Eff_BBB():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_bbb00', '')
        Unknown1096(675)
        teleportRelativeX(-100000)
        Unknown1007(70000)
    sprite('null', 4)
    GFX_0('Eff_BNNsub', -1)
    Unknown36(1)
    Unknown1097(225)
    Unknown35()
    SFX_0('017_freeze_0')
    SFX_0('017_freeze_0')
    sprite('null', 4)
    Unknown1097(100)
    sprite('null', 3)
    Unknown1097(-50)
    Unknown3001(200)
    GFX_1('phef_bbb', -1)
    SFX_0('018_ice_break_0')
    SFX_0('018_ice_break_0')
    sprite('null', 4)
    Unknown1097(-50)
    Unknown1099(7)
    Unknown3004(-51)

@State
def DriveAtk_RRB():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(6000)
        Unknown1064(10000)
        Unknown1007(375000)
        ProjectileHitsWall(1)
        Unknown48(23, 2, 51, 3, 2, 23)
        if SLOT_51:
            if (SLOT_19 > 300000):
                if (SLOT_19 < 650000):
                    Unknown1008()
                    Unknown1086(22)
                    Unknown1009()
                else:
                    teleportRelativeX(650000)
            else:
                teleportRelativeX(300000)
        elif (SLOT_19 > 100000):
            if (SLOT_19 < 650000):
                Unknown1008()
                Unknown1086(22)
                Unknown1009()
            else:
                teleportRelativeX(650000)
        else:
            teleportRelativeX(100000)
        AttackLevel_(5)
        Damage(1050)
        AirPushbackX(1500)
        AirPushbackY(50000)
        Hitstop(3)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AttackP1(100)
        AttackP2(79)
        AirPushbackX(3500)
        AirPushbackY(-60000)
        PushbackX(19950)
        StarterRating(2)
        HitOverhead(2)
        Unknown9190(1)
        Unknown9118(30)
        AirUntechableTime(60)
        Unknown3038(1)
        Unknown23013(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(2)
            sendToLabel(2)
    sprite('vr_ph_magictest', 17)
    GFX_0('phEff_RRB', -1)
    Unknown38(4, 1)
    SFX_3('phse_04')
    SFX_0('019_quake_1')
    StartMultihit()
    physicsYImpulse(5000)
    setGravity(500)
    sprite('vr_ph_magictest', 32767)
    physicsYImpulse(-150000)
    label(1)
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    AirHitstunAnimation(9)
    AirPushbackX(5000)
    AirPushbackY(20000)
    AirUntechableTime(30)
    blockstun(11)
    Unknown11001(0, 7, 15)
    Unknown9191()
    PushbackX(19800)
    HitOverhead(0)
    Unknown21007(4, 32)
    GFX_0('Eff_RRNsub2', -1)
    Unknown36(1)
    Unknown1007(180000)
    Unknown1073(25000)
    Unknown1097(500)
    Unknown35()
    StartMultihit()
    SFX_0('016_explode_2')
    sprite('vr_ph_magictest', 5)
    GFX_0('Eff_RRNsub2', -1)
    Unknown36(1)
    Unknown1007(60000)
    Unknown1073(15000)
    Unknown1099(30)
    Unknown35()
    ExitState()
    label(2)
    sprite('null', 10)
    Unknown3004(-23)
    ExitState()

@State
def phEff_RRB():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(100000)
        Unknown1096(1150)
        sendToLabelUpon(32, 1)
    sprite('vr_phrrb_01', 2)
    GFX_0('phEff_RRBSub', -1)
    sprite('vr_phrrb_02', 2)
    sprite('vr_phrrb_03', 2)
    sprite('vr_phrrb_04', 2)
    GFX_2('phef_rrb_jizoku')
    sprite('vr_phrrb_05', 2)
    sprite('vr_phrrb_00', 4)
    label(0)
    sprite('vr_phrrb_00', 2)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(3)
    Unknown3076(1200)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_phrrb_00', 3)
    Unknown1099(30)
    sprite('null', 10)
    GFX_1('phef_rrb_end', -1)
    Unknown3004(-26)
    ScreenShake(10000, 10000)
    loopRest()

@State
def phEff_RRBSub():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4013(2)
    sprite('null', 30)
    GFX_2('phef_rrb_start')

@State
def DriveAtk_RRG():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown3038(1)
        Unknown1056(2500)
        Unknown1064(2500)
        teleportRelativeX(100000)
        Unknown1007(300000)
        OnlyInHitstun(1)
        DisableAttackRestOfMove()
        Unknown23013(1)
        FireBallMultiHit(1, 0, 0, 0, 0, 0, 1, 0)

        def upon_54():
            clearUponHandler(32)
            clearUponHandler(54)
            sendToLabel(2)

        def upon_4():
            clearUponHandler(4)
            AttackLevel_(3)
            Damage(100)
            AttackP1(90)
            AirPushbackY(-20000)
            AirUntechableTime(60)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(2)
            OnlyInHitstun(0)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    physicsXImpulse(7500)
    physicsYImpulse(10000)
    Unknown1043()
    GFX_0('phEff_RRGseed', -1)
    SFX_3('phse_04')
    label(0)
    sprite('vr_ph_magictest', 32767)
    label(1)
    sprite('vr_ph_magictest', 10)
    AttackLevel_(5)
    Damage(900)
    HitLow(2)
    AirPushbackX(20000)
    AirPushbackY(-20000)
    AttackP2(84)
    Hitstop(0)
    PushbackX(19950)
    Unknown11001(6, 6, 8)
    Unknown9202(17)

    def upon_11():
        Unknown2038(1)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_2 >= 1):
            HitLow(0)
    Unknown26('phEff_RRGseed')
    GFX_1('phef_rrb_umore', -1)
    Unknown1059(500)
    Unknown1067(150)
    StartMultihit()
    Unknown1084(1)
    Unknown2006()
    SFX_0('012_stab_deep')
    sprite('vr_ph_magictest', 15)
    GFX_0('phEff_RRGmoguri', -1)
    Unknown1056(7500)
    Unknown1064(4000)
    Unknown1059(0)
    Unknown1067(0)
    StartMultihit()
    physicsXImpulse(1000)
    SFX_0('019_quake_1')
    sprite('vr_ph_magictest', 10)
    RefreshMultihit()
    GroundedHitstunAnimation(2)
    HitstunP2(40)
    Unknown9142(30)
    Unknown2006()
    physicsXImpulse(45000)
    GFX_0('phEff_RRG', -1)
    SFX_0('005_swing_grap_2_2')
    SFX_3('phse_05')
    sprite('vr_ph_magictest', 13)
    StartMultihit()
    Unknown1019(5)
    sprite('vr_ph_magictest', 10)
    RefreshMultihit()
    Unknown2006()
    PushbackX(50000)
    GroundedHitstunAnimation(9)
    AirPushbackX(20000)
    Unknown9202(12)
    GroundUntechableTime(20)
    physicsXImpulse(45000)
    GFX_0('phEff_RRG', -1)
    SFX_0('005_swing_grap_2_2')
    SFX_3('phse_05')
    sprite('vr_ph_magictest', 20)
    StartMultihit()
    Unknown1019(5)
    ExitState()
    label(2)
    sprite('null', 10)
    Unknown3004(-23)
    ExitState()

@State
def phEff_RRG():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        Unknown1096(1000)
        Unknown2005()
        GFX_2('phef_rrb_kusa')
    sprite('null', 7)
    Unknown4003('pheff_rrg_start', '')
    ScreenShake(4000, 4000)
    GFX_1('phef_rrb_kusa', -1)
    GFX_0('phEff_RRG_moya', -1)
    sprite('null', 10)
    Unknown4003('pheff_rrg_jizoku', '')
    sprite('null', 5)
    Unknown4007(0)
    sprite('null', 40)
    Unknown3001(0)
    GFX_0('phEff_RRGend', -1)
    Unknown21012('phEff_RRG_moya', 32)

@State
def phEff_RRG_moya():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        Unknown1096(1000)
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown23067('phef_rrg_moya')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown4047(1, 1, 1)
    Unknown4045('706865665f7272675f7462000000000000000000000000000000000000000000ffffffff')

@State
def phEff_RRGseed():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown1096(1200)
        Unknown1074(1250)
        Unknown23015(8)
        Unknown4054(7)
        Unknown23067('phef_rrb_seed')
        Unknown3029(1)
    sprite('vr_phrrg_00', 10)
    Unknown1074(1250)
    sprite('vr_phrrg_00', 10)
    Unknown1074(625)
    sprite('vr_phrrg_00', 32767)
    Unknown1074(416)

@State
def phEff_RRGend():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(1200)
    sprite('null', 15)
    GFX_1('phef_rrb_kusa', -1)
    Unknown4003('pheff_rrg_end', '')

@State
def phEff_RRGmoguri():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
    label(0)
    sprite('null', 4)
    GFX_1('phef_rrb_umore2', -1)
    gotoLabel(0)

@State
def DriveAtk_GGR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown4011(3)
        Unknown1096(200)
        teleportRelativeX(150000)
        Unknown1007(225000)
        ProjectileHitsWall(1)
        Unknown2003(1)
        Unknown3038(1)
        Unknown3032()
        Unknown4003('pheff_ggr00', '')
        Unknown4015()
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown23067('phef_ggr_jizoku')
        Unknown2037(0)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                YAccel(95)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(0)
    sprite('null', 10)
    GFX_1('phef_ggr_mc', -1)
    Unknown3001(0)
    Unknown3004(28)
    Unknown1099(30)
    SFX_3('phse_04')
    physicsXImpulse(5000)
    physicsYImpulse(5000)
    sprite('null', 10)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1099(0)
    sprite('null', 5)
    Unknown2037(1)
    Unknown1019(1200)
    YAccel(1800)
    sprite('null', 2)
    Unknown2037(0)
    Unknown1019(40)
    YAccel(40)
    sprite('null', 2)
    Unknown1019(40)
    YAccel(40)
    sprite('null', 2)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1099(100)
    sprite('null', 70)
    clearUponHandler(3)

    def upon_CLEAR_OR_EXIT():
        Unknown48(23, 2, 52, 22, 2, 22)
        Unknown47('01000000020000001600000002000000340000000200000034000000')
        if SLOT_38:
            Unknown47('030000000200000034000000000000003c000000020000000c000000')
        else:
            Unknown47('03000000020000003400000000000000c4ffffff020000000c000000')
    GFX_0('phEff_GGRYotyouMC', -1)
    Unknown1099(0)
    sprite('null', 5)
    clearUponHandler(3)
    Unknown1019(80)
    GFX_0('phEff_GGRatk', -1)
    sprite('null', 5)
    Unknown1019(80)
    sprite('null', 5)
    Unknown1019(80)
    sprite('null', 5)
    Unknown1019(80)
    sprite('null', 5)
    Unknown1019(80)
    sprite('null', 5)
    physicsXImpulse(0)
    sprite('null', 3)
    Unknown21012('phEff_GGRYotyouMC', 32)
    GFX_0('DriveAtk_GGR_C', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_R', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_L', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_RR', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_LL', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_C', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_R', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_L', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_RR', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_LL', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_C', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_R', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_L', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_RR', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_LL', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_C', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_R', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_L', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_RR', -1)
    sprite('null', 3)
    GFX_0('DriveAtk_GGR_LL', -1)
    sprite('null', 60)
    Unknown21012('phEff_GGRatk', 32)
    Unknown21012('phEff_GGRYotyouMC', 33)
    Unknown3004(-25)
    ExitState()
    label(0)
    sprite('null', 15)
    Unknown21012('phEff_GGRatk', 32)
    Unknown3004(-15)
    ExitState()

@State
def DriveAtk_GGR_PreAtk():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(4000)
        Unknown1064(4000)
        AttackLevel_(2)
        Damage(300)
        AirPushbackX(15000)
        AirPushbackY(40000)
        AirUntechableTime(53)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        OnlyInHitstun(1)
        Unknown3038(1)

        def upon_CLEAR_OR_EXIT():
            Unknown2071('0200000010270000f0d8ffff6400000001000000')
    sprite('vr_ph_magictest', 10)

@State
def phEff_GGRatk():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(200)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('pheff_ggr01', '')
        Unknown4015()

        def upon_32():
            clearUponHandler(32)
            sendToLabel(0)
    sprite('null', 10)
    ScreenShake(10000, 10000)
    Unknown3001(0)
    Unknown3004(20)
    physicsYImpulse(-16000)
    Unknown1099(20)
    SFX_0('016_explode_0')
    SFX_0('019_quake_1')
    sprite('null', 100)
    Unknown3004(0)
    Unknown1099(0)
    physicsYImpulse(0)
    Unknown1099(0)
    Unknown4061(2)
    Unknown4047(1, 1, 1)
    Unknown23067('phef_ggr_ray')
    label(0)
    sprite('null', 10)
    Unknown3004(-23)
    loopRest()

@State
def phEff_GGRtama():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        Unknown23015(8)
        Unknown4054(7)
        Unknown4047(1, 1, 1)
        Unknown23067('phef_ggr_tamacolor')
        Unknown1056(1000)
    sprite('vr_phbbr_00', 2)
    Unknown1007(150000)
    label(0)
    sprite('vr_phbbr_00', 2)
    GFX_0('Eff_GGRfire', -1)
    sprite('vr_phbbr_01', 2)
    sprite('vr_phbbr_02', 2)
    GFX_0('Eff_GGRfire2', -1)
    sprite('vr_phbbr_03', 2)
    gotoLabel(0)

@State
def Eff_GGRfire():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4006(2)
        Unknown4003('pheff_ggrAtk00', '')
        Unknown1064(500)
        Unknown1056(600)
        Unknown1102(-100, 100)
    sprite('null', 3)
    sprite('null', 5)
    Unknown3004(-51)

@State
def Eff_GGRfire2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4006(2)
        Unknown4003('pheff_ggrAtk00', '')
        Unknown1064(500)
        Unknown1056(-600)
        Unknown1062(0, 200)
    sprite('null', 3)
    sprite('null', 5)
    Unknown1102(-100, 100)

@State
def phEff_GGRgshock():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1096(400)
        Unknown3033()
        Unknown4061(2)
        Unknown23015(1)
        Unknown1077(-360000, 360000)
        Unknown1011(50000, 100000)
        Unknown1010(-25000, 25000)
        Unknown1102(0, 300)
    sprite('vr_ph216_00', 2)
    Unknown1099(30)
    sprite('vr_ph216_01', 2)
    sprite('vr_ph216_02', 2)
    sprite('vr_ph216_03', 2)
    sprite('vr_ph216_04', 2)
    sprite('vr_ph216_05', 5)

@Subroutine
def DriveAtk_GGR_Init():
    AttackLevel_(3)
    Damage(400)
    AirHitstunAnimation(10)
    AttackP1(80)
    AttackP2(94)
    AirUntechableTime(25)
    AirPushbackX(0)
    AirPushbackY(12000)
    Hitstop(0)
    Unknown11001(2, 2, 4)
    PushbackX(0)
    Unknown11057(300)
    Unknown11084(1)
    StarterRating(2)
    Unknown23182(2)

@State
def DriveAtk_GGR_C():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        Unknown1056(1500)
        Unknown1064(1500)
        Unknown1007(-100000)
        Unknown3038(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    SFX_0('015_blaze_0')
    GFX_0('phEff_GGRtama', -1)
    Unknown36(1)
    Unknown1072(90000)
    Unknown35()
    physicsYImpulse(-60000)
    label(1)
    sprite('null', 1)
    SFX_0('016_explode_1')
    GFX_0('phEff_GGRgshock', -1)
    GFX_1('phef_ggr_gshock', -1)
    Unknown1084(1)
    ScreenShake(1000, 1000)
    loopRest()
    ExitState()
    label(2)
    sprite('null', 4)
    Unknown3001(255)
    Unknown3004(-51)
    ExitState()

@State
def DriveAtk_GGR_L():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        teleportRelativeX(-25000)
        Unknown1007(-100000)
        Unknown1056(1500)
        Unknown1064(1500)
        Unknown3038(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    physicsXImpulse(-11000)
    physicsYImpulse(-60000)
    GFX_0('phEff_GGRtama', -1)
    Unknown36(1)
    Unknown1072(90000)
    Unknown35()
    label(1)
    sprite('null', 1)
    GFX_0('phEff_GGRgshock', -1)
    GFX_1('phef_ggr_gshock', -1)
    Unknown1084(1)
    ScreenShake(1000, 1000)
    loopRest()
    label(2)
    sprite('null', 4)
    Unknown3001(255)
    Unknown3004(-51)
    ExitState()

@State
def DriveAtk_GGR_LL():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        teleportRelativeX(-50000)
        Unknown1007(-100000)
        Unknown1056(1500)
        Unknown1064(1500)
        Unknown3038(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    physicsXImpulse(-22000)
    physicsYImpulse(-60000)
    GFX_0('phEff_GGRtama', -1)
    Unknown36(1)
    Unknown1072(100000)
    Unknown35()
    label(1)
    sprite('null', 1)
    GFX_0('phEff_GGRgshock', -1)
    GFX_1('phef_ggr_gshock', -1)
    Unknown1084(1)
    ScreenShake(1000, 1000)
    loopRest()
    label(2)
    sprite('null', 4)
    Unknown3001(255)
    Unknown3004(-51)
    ExitState()

@State
def DriveAtk_GGR_R():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        teleportRelativeX(25000)
        Unknown1007(-100000)
        Unknown1056(1500)
        Unknown1064(1500)
        Unknown3038(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    physicsXImpulse(11000)
    physicsYImpulse(-60000)
    GFX_0('phEff_GGRtama', -1)
    Unknown36(1)
    Unknown1072(85000)
    Unknown35()
    label(1)
    sprite('null', 1)
    GFX_0('phEff_GGRgshock', -1)
    GFX_1('phef_ggr_gshock', -1)
    Unknown1084(1)
    ScreenShake(1000, 1000)
    loopRest()
    ExitState()
    label(2)
    sprite('null', 4)
    Unknown3001(255)
    Unknown3004(-51)
    ExitState()

@State
def DriveAtk_GGR_RR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        callSubroutine('DriveAtk_GGR_Init')
        teleportRelativeX(50000)
        Unknown1007(-100000)
        Unknown1056(1500)
        Unknown1064(1500)
        Unknown3038(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(3)
            sendToLabel(2)
    sprite('vr_ph_magictest', 32767)
    physicsXImpulse(22000)
    physicsYImpulse(-60000)
    GFX_0('phEff_GGRtama', -1)
    Unknown36(1)
    Unknown1072(75000)
    Unknown35()
    label(1)
    sprite('null', 1)
    GFX_0('phEff_GGRgshock', -1)
    GFX_1('phef_ggr_gshock', -1)
    Unknown1084(1)
    ScreenShake(1000, 1000)
    loopRest()
    ExitState()
    label(2)
    sprite('null', 4)
    Unknown3001(255)
    Unknown3004(-51)
    ExitState()

@State
def phEff_GGRYotyouMC():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown23015(5)
        Unknown4003('pheff_ggr00_yotyou', '')
        Unknown1086(2)
        teleportRelativeY(0)
        Unknown1056(900)
        Unknown1064(600)
        Unknown3001(160)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        Unknown48(23, 2, 51, 2, 2, 23)
        Unknown47('03000000020000003300000000000000200300000200000068000000')
        if (SLOT_104 > 2000):
            SLOT_104 = 2000

        def upon_CLEAR_OR_EXIT():
            Unknown1086(2)
            teleportRelativeY(0)
    sprite('null', 32767)
    GFX_0('phEff_GGRYotyouMCcolor', -1)
    GFX_0('phEff_GGRYotyouMCcore', -1)
    label(0)
    sprite('null', 32767)
    Unknown21012('phEff_GGRYotyouMCcolor', 32)
    label(1)
    sprite('null', 5)
    Unknown21012('phEff_GGRYotyouMCcore', 32)
    sprite('null', 5)
    Unknown3004(-51)

@State
def phEff_GGRYotyouMCcore():

    def upon_IMMEDIATE():
        Unknown4010(2)
        GFX_2('phef_rgg_yotei_mc')
        Unknown1056(900)
        Unknown1064(600)
        sendToLabelUpon(32, 0)

        def upon_CLEAR_OR_EXIT():
            Unknown1086(2)
            teleportRelativeY(0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    Unknown1099(80)
    sprite('null', 5)
    Unknown3004(-51)

@State
def phEff_GGRYotyouMCcolor():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown4010(2)
        Unknown4047(1, 1, 1)
        Unknown23067('phef_rgg_yotei_color')
        Unknown1096(700)
        sendToLabelUpon(32, 0)

        def upon_CLEAR_OR_EXIT():
            Unknown1086(2)
            teleportRelativeY(0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def DriveDef_GGB():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown3038(1)
        Unknown4007(2)

        def upon_14():
            clearUponHandler(32)
            clearUponHandler(14)
            Unknown21007(2, 32)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(14)
            Unknown23022(1)
            sendToLabel(1)
    sprite('phdrivecol_ggb', 300)
    label(1)
    sprite('null', 10)

@State
def DriveAtk_GGB():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(4000)
        Unknown1064(4000)
        teleportRelativeX(150000)
        Unknown1007(125000)
        ProjectileHitsWall(1)
        Unknown23013(1)
        Unknown3038(1)
        AttackLevel_(3)
        Hitstop(0)
        Damage(300)
        ProjectileDurabilityLvl(3)
        AirHitstunAnimation(18)
        AirUntechableTime(19)
        AirPushbackX(15000)
        AirPushbackY(10000)
        YImpluseBeforeWallbounce(1000)
        OnlyInHitstun(1)
        Unknown2001()
        Unknown2037(0)

        def upon_CLEAR_OR_EXIT():
            Unknown1019(95)
            YAccel(95)
            if SLOT_2:
                if SLOT_51:
                    Unknown1028(0)
                    Unknown2037(0)
                    sendToLabel(1)
                if (not SLOT_51):
                    if CheckInput(0x93):
                        Unknown1021(1500)
                    if CheckInput(0x45):
                        Unknown1021(-1500)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(33)
            clearUponHandler(34)
            clearUponHandler(3)
            clearUponHandler(54)
            sendToLabel(0)

        def upon_33():
            clearUponHandler(33)
            clearUponHandler(34)
            clearUponHandler(54)
            SLOT_51 = 1

        def upon_34():
            clearUponHandler(33)
            clearUponHandler(34)
            clearUponHandler(54)
            SLOT_51 = 1
        FireBallMultiHit(1, 0, 0, 0, 0, 0, 1, 0)

        def upon_54():
            clearUponHandler(32)
            clearUponHandler(33)
            clearUponHandler(34)
            clearUponHandler(3)
            clearUponHandler(54)
            sendToLabel(0)
    sprite('vr_ph_magictest', 3)
    physicsXImpulse(60000)
    Unknown1028(1000)
    SFX_3('phse_04')
    GFX_0('DriveDef_GGB', -1)
    GFX_0('Eff_GGB', -1)
    Unknown38(4, 1)
    Unknown2037(1)
    sprite('vr_ph_magictest', 3)
    Unknown1019(50)
    sprite('vr_ph_magictest', 3)
    Unknown1019(50)
    sprite('vr_ph_magictest', 60)
    Unknown2001()
    label(1)
    sprite('vr_ph_magictest', 15)
    Unknown1019(50)
    sprite('vr_ph_magictest', 5)
    Unknown1084(1)
    Unknown21007(4, 34)
    Unknown21012('DriveDef_GGB', 32)
    sprite('vr_ph_magictest', 10)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(3)
    Unknown21007(4, 32)
    sprite('vr_ph_magictest', 60)
    GFX_0('DriveAtk_GGB_ATKMaster', -1)
    SFX_0('013_thunder_0')
    sprite('vr_ph_magictest', 10)
    ExitState()
    label(2)
    sprite('vr_ph_magictest', 40)
    Unknown1084(1)
    sprite('vr_ph_magictest', 20)
    Unknown21007(4, 34)
    Unknown21012('DriveDef_GGB', 32)
    sprite('vr_ph_magictest', 10)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(3)
    Unknown21007(4, 32)
    sprite('vr_ph_magictest', 60)
    GFX_0('DriveAtk_GGB_ATKMaster', -1)
    SFX_0('013_thunder_0')
    sprite('vr_ph_magictest', 10)
    ExitState()
    label(0)
    sprite('null', 11)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown21012('DriveDef_GGB', 32)
    Unknown21007(4, 33)
    Unknown3004(-25)
    ExitState()

@State
def DriveAtk_GGB_ATKMaster():

    def upon_IMMEDIATE():
        Unknown2037(6)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)
    sprite('null', 3)
    GFX_0('Eff_GGBatk', -1)
    Unknown38(4, 1)
    GFX_0('DriveAtk_GGB_ATKU', -1)
    Unknown38(5, 1)
    GFX_0('DriveAtk_GGB_ATKH', -1)
    Unknown38(6, 1)
    Unknown21007(5, 33)
    Unknown21007(6, 33)
    label(0)
    sprite('null', 2)
    Unknown21007(5, 33)
    Unknown21007(6, 33)
    sprite('null', 1)
    if (SLOT_2 == 0):
        sendToLabel(1)
    else:
        Unknown2038(-1)
        sendToLabel(0)
    label(1)
    sprite('null', 10)
    Unknown21007(4, 32)
    Unknown21007(5, 32)
    Unknown21007(6, 32)

@Subroutine
def DriveAtk_GGB_Init():
    AttackLevel_(3)
    Damage(250)
    ChipDamagePct(15)
    Unknown11056(1)
    Hitstop(0)
    Unknown11001(0, 10, 10)
    Unknown11057(200)
    Unknown9016(1)
    AttackP2(92)
    Unknown23182(2)
    Unknown11084(1)
    PushbackX(39900)
    StarterRating(2)
    AirPushbackX(60000)
    AirPushbackY(35000)
    AirUntechableTime(30)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    Unknown9178(1)
    WallbounceReboundTime(10)
    AirHitstunAfterWallbounce(60)

@State
def DriveAtk_GGB_ATKU():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(120000)
        Unknown1064(1000)
        Unknown1007(25000)
        callSubroutine('DriveAtk_GGB_Init')
        Unknown3038(1)

        def upon_12():
            Damage(300)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        DisableAttackRestOfMove()
    sprite('null', 10)
    label(1)
    sprite('vr_ph_magictest', 4)
    RefreshMultihit()
    sprite('null', 60)
    label(0)
    sprite('null', 5)

@State
def DriveAtk_GGB_ATKH():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(1000)
        Unknown1064(100000)
        Unknown1007(-600000)
        callSubroutine('DriveAtk_GGB_Init')
        Unknown3038(1)

        def upon_12():
            Damage(400)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 10)
    label(1)
    sprite('vr_ph_magictest', 4)
    RefreshMultihit()
    sprite('null', 60)
    label(0)
    sprite('null', 5)

@State
def Eff_GGB():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('pheff_ggb01', '')
        Unknown4015()
        Unknown1096(1100)
        Unknown1007(50000)
        GFX_2('phef_ggb_add')
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        sendToLabelUpon(34, 100)
        Unknown3001(0)
        Unknown3004(63)
    label(0)
    sprite('null', 2)
    Unknown1096(1100)
    GFX_0('Eff_GGBMoya', -1)
    sprite('null', 2)
    Unknown1096(1000)
    sprite('null', 2)
    Unknown1096(1100)
    sprite('null', 2)
    Unknown1096(1000)
    SFX_0('014_electric_s')
    gotoLabel(0)
    label(100)
    clearUponHandler(34)
    sprite('null', 5)
    Unknown3001(255)
    Unknown3004(-23)
    Unknown1096(1000)
    Unknown1099(-90)
    Unknown21012('Eff_GGBMoya', 32)
    sprite('null', 5)
    GFX_0('Eff_GGBPre', -1)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(0)
    Unknown1096(0)
    Unknown1099(0)
    label(1)
    clearUponHandler(32)
    clearUponHandler(33)
    sprite('null', 7)
    ScreenShake(20000, 20000)
    Unknown3001(255)
    Unknown1096(1000)
    Unknown1099(200)
    GFX_1('phef_ggb_start', -1)
    Unknown21012('Eff_GGBMoya', 32)
    loopRest()
    label(2)
    clearUponHandler(32)
    clearUponHandler(33)
    sprite('null', 10)
    Unknown3001(255)
    Unknown3004(-23)
    Unknown21012('Eff_GGBMoya', 32)
    loopRest()

@State
def Eff_GGBPre():

    def upon_IMMEDIATE():
        Unknown1096(250)
        GFX_2('phef_ggb_end')
    sprite('null', 60)

@State
def Eff_DriveMagicCircle():

    def upon_IMMEDIATE():
        GFX_2('phef_magicAir_mc')

        def upon_CLEAR_OR_EXIT():
            Unknown2071('03000000b03cffffc0f2fcff6400000001000000')
    sprite('null', 20)

@State
def Eff_GGBMoya():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        sendToLabelUpon(32, 1)
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown23067('phef_rrb_moya')
        Unknown1096(700)
    sprite('null', 32767)
    label(1)
    sprite('null', 10)
    Unknown1099(-25)
    Unknown3004(-31)

@State
def Eff_GGBatk():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('pheff_ggb00', '')
        Unknown4015()
        Unknown1007(50000)
        sendToLabelUpon(32, 1)
        GFX_2('phef_ggb_jizoku')
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    Unknown1096(1300)
    ScreenShake(1000, 1000)
    sprite('null', 2)
    Unknown1096(1250)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Unknown1099(-25)
    GFX_1('phef_ggb_end', -1)
    loopRest()

@State
def DriveAtk_BBR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown3032()
        Unknown4011(2)
        Unknown1096(550)
        Unknown3001(0)
        GFX_2('phef_rrb_add')
        teleportRelativeX(150000)
        Unknown1007(200000)
        Unknown3038(1)
        Unknown2003(1)
        FireBallMultiHit(1, 0, 0, 0, 0, 0, 1, 1)

        def upon_54():
            clearUponHandler(32)
            clearUponHandler(54)
            sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            clearUponHandler(54)
            sendToLabel(1)
    sprite('null', 10)
    physicsXImpulse(2000)
    GFX_0('Eff_BBRSub', -1)
    GFX_0('ParticleMaster_BBR', -1)
    Unknown4003('pheff_bbr00', '')
    Unknown3001(0)
    Unknown3004(51)
    SFX_3('phse_04')
    sprite('null', 20)
    sprite('null', 4)
    Unknown1019(2500)
    Unknown3001(255)
    Unknown3004(-63)
    SFX_0('000_airdash_0')
    sprite('null', 20)
    Unknown3001(0)
    Unknown3004(0)
    sprite('null', 5)
    Unknown1086(22)
    Unknown1007(200000)
    Unknown1019(0)
    YAccel(0)
    sprite('null', 4)
    Unknown3001(0)
    Unknown3004(51)
    physicsXImpulse(-60000)
    physicsYImpulse(50000)
    sprite('null', 6)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1019(10)
    YAccel(10)
    sprite('null', 6)
    Unknown1019(10)
    YAccel(10)
    sprite('null', 2)
    Unknown1019(0)
    YAccel(0)
    Unknown4003('pheff_bbr01', '')
    sprite('null', 3)
    GFX_0('DriveAtk_BBR_ATK', -1)
    Unknown21007(1, 32)
    physicsXImpulse(-8000)
    physicsYImpulse(8000)
    sprite('null', 3)
    Unknown1019(25)
    YAccel(25)
    sprite('null', 3)
    Unknown1019(25)
    YAccel(25)
    sprite('null', 6)
    Unknown1019(0)
    YAccel(0)
    sprite('null', 6)
    physicsXImpulse(5000)
    physicsYImpulse(-1500)
    Unknown4003('pheff_bbr00', '')
    sprite('null', 4)
    Unknown1019(2500)
    YAccel(2500)
    Unknown3001(255)
    Unknown3004(-63)
    SFX_0('000_airdash_0')
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(0)
    Unknown1019(0)
    YAccel(0)
    sprite('null', 5)
    Unknown1086(22)
    Unknown1007(200000)
    sprite('null', 4)
    Unknown3001(0)
    Unknown3004(51)
    physicsXImpulse(80000)
    sprite('null', 6)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1019(5)
    YAccel(5)
    Unknown2006()
    sprite('null', 6)
    Unknown1019(5)
    YAccel(5)
    sprite('null', 2)
    Unknown1019(0)
    YAccel(0)
    Unknown1072(15000)
    Unknown4003('pheff_bbr01', '')
    sprite('null', 3)
    GFX_0('DriveAtk_BBR_ATK', -1)
    Unknown21007(1, 33)
    physicsXImpulse(-8000)
    sprite('null', 3)
    Unknown1019(25)
    sprite('null', 3)
    Unknown1019(25)
    sprite('null', 6)
    Unknown1019(0)
    sprite('null', 6)
    physicsXImpulse(6000)
    Unknown4003('pheff_bbr00', '')
    sprite('null', 4)
    Unknown1072(0)
    Unknown1019(2500)
    YAccel(2500)
    Unknown3001(255)
    Unknown3004(-63)
    SFX_0('000_airdash_0')
    sprite('null', 10)
    Unknown3004(-63)
    Unknown3001(0)
    Unknown3004(0)
    Unknown1019(0)
    YAccel(0)
    sprite('null', 5)
    Unknown1086(22)
    teleportRelativeX(-30000)
    Unknown1007(200000)
    sprite('null', 4)
    Unknown3001(0)
    Unknown3004(51)
    physicsYImpulse(75000)
    sprite('null', 6)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1019(5)
    YAccel(5)
    sprite('null', 6)
    Unknown1019(5)
    YAccel(5)
    sprite('null', 2)
    Unknown1019(0)
    YAccel(0)
    Unknown2006()
    sprite('null', 3)
    Unknown4003('pheff_bbr01', '')
    Unknown1072(35000)
    GFX_0('DriveAtk_BBR_ATK', -1)
    Unknown21007(1, 34)
    physicsYImpulse(8000)
    sprite('null', 5)
    YAccel(25)
    sprite('null', 5)
    YAccel(25)
    sprite('null', 10)
    YAccel(0)
    sprite('null', 5)
    Unknown4003('pheff_bbr00', '')
    physicsXImpulse(-20000)
    physicsYImpulse(2000)
    sprite('null', 5)
    Unknown1019(50)
    YAccel(50)
    sprite('null', 5)
    physicsYImpulse(-5000)
    sprite('null', 5)
    Unknown1019(50)
    YAccel(200)
    sprite('null', 5)
    physicsXImpulse(10000)
    YAccel(200)
    sprite('null', 8)
    Unknown1072(0)
    Unknown1019(1500)
    YAccel(150)
    Unknown3001(255)
    Unknown3004(-15)
    SFX_0('000_airdash_0')
    sprite('null', 30)
    Unknown3001(0)
    Unknown3004(0)
    ExitState()
    label(1)
    sprite('null', 10)
    Unknown4003('pheff_bbr00', '')
    Unknown1019(0)
    YAccel(0)
    Unknown3004(-28)

@State
def DriveAtk_BBR_PreAtk():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(4000)
        Unknown1064(4000)
        AttackLevel_(2)
        Damage(300)
        AirPushbackX(20000)
        AirPushbackY(10000)
        AirUntechableTime(26)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        OnlyInHitstun(1)
        Unknown3038(1)

        def upon_CLEAR_OR_EXIT():
            Unknown2071('02000000e0b1ffffc063ffff6400000001000000')
    sprite('vr_ph_magictest', 10)

@State
def ParticleMaster_BBR():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(2)
    label(0)
    sprite('null', 4)
    GFX_1('phef_rrb_tb', -1)
    gotoLabel(0)

@State
def DriveAtk_BBR_ATK():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(1500)
        Unknown1064(1500)
        AttackLevel_(2)
        AttackP1(80)
        AirPushbackX(250)
        AirPushbackY(25000)
        AirUntechableTime(20)
        Unknown11001(0, 10, 11)
        Unknown9015(1)
        Unknown11057(500)
        Unknown23182(2)
        StarterRating(2)
        Unknown3038(1)
        Unknown53(1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown2001()

        def upon_32():
            Unknown1072(45000)
            physicsXImpulse(60000)
            physicsYImpulse(-60000)

        def upon_33():
            physicsXImpulse(60000)

        def upon_34():
            AirPushbackX(0)
            AirPushbackY(-40000)
            Unknown11056(3)
            Unknown9190(1)
            Unknown9118(25)
            Unknown1072(90000)
            physicsYImpulse(-60000)
    sprite('vr_ph_magictest', 120)
    GFX_0('Eff_BBRmc', -1)
    GFX_0('Eff_BBRAtk', -1)
    SFX_3('phse_07')
    label(1)
    sprite('null', 10)
    Unknown3004(-23)

@State
def Eff_BBRSub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4025(2)
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown23067('phef_rrb_moya')
    sprite('null', 32767)

@State
def Eff_BBRAtk():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4025(2)
        Unknown4006(2)
        Unknown4061(3)
        Unknown23015(8)
        Unknown4054(7)
        Unknown23067('phef_rrbatk_add')
        Unknown3029(1)
        Unknown3069(2)
        Unknown1096(1000)
    label(0)
    sprite('vr_phbbr_00', 2)
    GFX_1('phef_rrbatk_bgnokosi', -1)
    GFX_1('phef_rrbatk_tb', -1)
    GFX_1('phef_rrbatk_tb2', -1)
    GFX_0('Eff_BBRBlack', -1)
    sprite('vr_phbbr_01', 2)
    GFX_1('phef_rrbatk_bgnokosi', -1)
    sprite('vr_phbbr_02', 2)
    GFX_1('phef_rrbatk_bgnokosi', -1)
    GFX_1('phef_rrbatk_tb', -1)
    GFX_1('phef_rrbatk_tb2', -1)
    GFX_0('Eff_BBRBlack', -1)
    sprite('vr_phbbr_03', 2)
    GFX_1('phef_rrbatk_bgnokosi', -1)
    gotoLabel(0)

@State
def Eff_BBRBlack():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4006(2)
        Unknown4003('pheff_bbrAtk', '')
    sprite('null', 5)
    sprite('null', 10)
    Unknown3004(-26)

@State
def Eff_BBRmc():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4006(2)
        GFX_2('phef_bbr_entermc')
    sprite('null', 30)

@State
def DriveAtk_BBG():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(10000)
        Unknown1064(150000)
        Unknown1008()
        Unknown1086(22)
        Unknown1009()
        AttackLevel_(3)
        Damage(0)
        AttackP1(50)
        AttackP2(100)
        AirHitstunAnimation(11)
        AirPushbackY(-50000)
        Hitstop(0)
        AirUntechableTime(60)
        GroundUntechableTime(25)
        Unknown11046(1)
        Unknown11104(1)
        Unknown11066(1)
        HitOverhead(4)
        HitLow(4)
        HitAirUnblockable(4)
        Unknown11032('400d0300c0f2fcff80841e00807be1ff')
        Unknown11042(1)
        StarterRating(0)
        Unknown12055(1)
        DisableAttackRestOfMove()
        Unknown3038(1)
        ProjectileHitsWall(1)
        Unknown2037(1)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_135 > 0):
                Unknown2037(0)
                DisableAttackRestOfMove()
            if SLOT_2:
                Unknown48(23, 2, 51, 22, 2, 23)
                if (SLOT_51 == 0):
                    DisableAttackRestOfMove()
                elif (SLOT_51 > 80000):
                    if (SLOT_135 == 0):
                        RefreshMultihit()
            else:
                Unknown48(23, 2, 51, 22, 2, 23)
                if (SLOT_51 == 0):
                    if (SLOT_135 == 0):
                        Unknown2037(1)
            if SLOT_52:
                if (SLOT_19 < 350000):
                    SLOT_53 = (SLOT_53 + 1)
                    if (SLOT_53 > 150):
                        SLOT_52 = 0
                        SLOT_53 = 0
                        sendToLabel(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)

        def upon_33():
            clearUponHandler(33)
            Unknown1086(3)
            teleportRelativeX(300000)
    sprite('null', 1)
    sprite('null', 105)
    GFX_0('Eff_BBGmc', -1)
    Unknown38(4, 1)
    SFX_3('phse_06')
    sprite('null', 8)
    SLOT_52 = 1
    GFX_0('SoundMaster_BBG', -1)
    Unknown23124(1)
    ScreenShake(10000, 10000)
    GFX_0('Eff_BBGct', -1)
    Unknown38(5, 1)
    GFX_0('Eff_BBG', -1)
    Unknown38(6, 1)
    GFX_0('Eff_BBG', -1)
    Unknown38(7, 1)
    Unknown36(6)
    teleportRelativeX(250000)
    Unknown35()
    Unknown36(7)
    teleportRelativeX(-250000)
    Unknown2005()
    Unknown35()
    sprite('vr_ph_magictest', 300)
    label(1)
    sprite('vr_ph_magictest', 30)
    clearUponHandler(3)
    Unknown2001()
    Unknown21007(4, 32)
    Unknown21007(5, 32)
    Unknown21007(6, 32)
    Unknown21007(7, 32)
    Unknown23124(0)

@State
def SoundMaster_BBG():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
    label(0)
    sprite('null', 50)
    SFX_0('022_magiccircle_c')
    gotoLabel(0)

@State
def Eff_BBG():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_bbg00', '')
        Unknown4010(2)
        Unknown1056(180)
        Unknown1064(700)
        Unknown4061(2)
        Unknown21004(1)
        teleportRelativeY(0)
        sendToLabelUpon(32, 1)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(13)
    label(0)
    sprite('null', 20)
    Unknown3004(-4)
    physicsXImpulse(0)
    Unknown1059(-1)
    sprite('null', 20)
    Unknown3004(4)
    Unknown1059(1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown3004(-26)
    loopRest()

@State
def Eff_BBGct():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_bbg01', '')
        Unknown4010(2)
        Unknown1056(650)
        Unknown1064(750)
        teleportRelativeY(0)
        sendToLabelUpon(32, 1)
    sprite('null', 5)
    GFX_0('Eff_BBGcore', -1)
    Unknown38(4, 1)
    Unknown3001(0)
    Unknown3004(45)
    label(0)
    sprite('null', 25)
    Unknown3004(-5)
    GFX_1('phef_bbg_jizoku', -1)
    sprite('null', 25)
    Unknown3004(5)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown21007(4, 32)
    loopRest()

@State
def Eff_BBGcore():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4054(2)
        Unknown23067('phef_bbr_core')
        Unknown4010(2)
        teleportRelativeY(0)
        Unknown1096(550)
        sendToLabelUpon(32, 1)
    sprite('null', 10)
    physicsYImpulse(15000)
    sprite('null', 4)
    physicsYImpulse(7500)
    GFX_0('Eff_BBGcoresub', -1)
    Unknown36(1)
    Unknown23015(2)
    Unknown35()
    physicsYImpulse(3750)
    GFX_0('Eff_BBGcoresub', -1)
    Unknown36(1)
    Unknown23015(2)
    Unknown35()
    label(0)
    sprite('null', 4)
    physicsYImpulse(-1500)
    GFX_0('Eff_BBGcoresub', -1)
    Unknown36(1)
    Unknown23015(2)
    Unknown35()
    sprite('null', 4)
    physicsYImpulse(1500)
    GFX_0('Eff_BBGcoresub', -1)
    Unknown36(1)
    Unknown23015(2)
    Unknown35()
    gotoLabel(0)
    label(1)
    sprite('null', 20)
    Unknown3004(-17)
    physicsYImpulse(-15000)
    loopRest()

@State
def Eff_BBGcoresub():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4003('pheff_brn01', '')
        Unknown1096(750)
        Unknown1102(-50, 250)
        Unknown1077(-360000, 360000)
    sprite('null', 2)
    sprite('null', 1)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(64)
    sprite('null', 1)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(64)
    sprite('null', 1)
    Unknown3001(0)
    sprite('null', 2)
    Unknown3001(64)

@State
def Eff_BBGmc():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown23067('phef_bbr_core_mc')
        Unknown4010(2)
        teleportRelativeY(0)
        sendToLabelUpon(32, 1)
    sprite('null', 32767)
    label(1)
    sprite('null', 5)
    Unknown1099(60)
    sprite('null', 10)
    Unknown3004(-26)
    loopRest()

@State
def DriveAtk_BGR():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1096(20000)
        AttackLevel_(5)
        Damage(1500)
        AttackP1(80)
        AttackP2(74)
        MinimumDamagePct(20)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(100000)
        AirUntechableTime(180)
        Hitstop(2)
        Unknown11001(0, 0, 1)
        Unknown11069('DriveAtk_BGR')
        Unknown11023(1)
        ChipDamagePct(35)
        Unknown11056(3)
        Unknown11044(1)
        StarterRating(2)
        Unknown2008()
        Unknown11087(100, 1)
        Unknown2037(481)
        Unknown3038(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)
    sprite('null', 10)
    SFX_3('phse_04')
    GFX_0('Eff_BGRcount', -1)
    Unknown38(4, 1)
    sprite('null', 600)
    sprite('null', 64)
    Unknown1086(22)
    Unknown21007(4, 32)
    Unknown2036(60, -1, 2)
    GFX_0('Eff_BGRCamera', -1)
    GFX_0('Eff_BGRstart', -1)
    GFX_0('Eff_BGRbg', -1)
    Unknown38(5, 1)
    sprite('vr_ph_magictest', 1)
    Unknown21007(4, 33)
    GFX_0('Eff_BGRmato', -1)
    ScreenShake(0, 20000)
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    Unknown11087(0, 0)
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    Unknown11069('')
    sprite('vr_ph_magictest', 25)
    Unknown2001()
    sprite('vr_ph_magictest', 10)
    Unknown21007(5, 32)
    ExitState()
    label(1)
    sprite('null', 10)
    Unknown21007(4, 33)
    Unknown21007(5, 32)

@State
def Eff_BGRcount():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown1096(50)
        Unknown23015(6)
        Unknown1086(22)
        Unknown1007(240000)

        def upon_CLEAR_OR_EXIT():
            Unknown2071('160000000000000050c300003200000001000000')
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('vr_phbgr_00', 10)
    SFX_0('022_magiccircle_b')
    GFX_0('Eff_BGRhari', -1)
    Unknown1099(75)
    sprite('vr_phbgr_00', 78)
    Unknown1096(800)
    Unknown1099(0)
    sprite('vr_phbgr_00', 138)
    GFX_0('Eff_BGRcountSub1', 2)
    Unknown38(4, 1)
    sprite('vr_phbgr_00', 162)
    GFX_0('Eff_BGRcountSub2', 3)
    Unknown38(5, 1)
    sprite('vr_phbgr_00', 138)
    GFX_0('Eff_BGRcountSub3', 1)
    Unknown38(6, 1)
    sprite('vr_phbgr_00', 1)
    GFX_0('Eff_BGRcountSub4', 0)
    Unknown38(7, 1)
    sprite('vr_phbgr_00', 32767)
    label(0)
    sprite('vr_phbgr_00', 32767)
    clearUponHandler(3)
    Unknown1096(1300)
    Unknown1086(22)
    Unknown1007(200000)
    Unknown21007(4, 32)
    Unknown21007(5, 32)
    Unknown21007(6, 32)
    Unknown21007(7, 32)
    label(1)
    sprite('null', 1)

@State
def Eff_BGRhari():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1096(1200)
        Unknown23015(8)
        Unknown4011(3)
        Unknown4010(2)
        Unknown4007(2)
    sprite('vr_phbgr_01', 10)
    Unknown3001(0)
    Unknown3004(28)
    sprite('vr_phbgr_01', 32767)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1074(600)

@Subroutine
def CountDownFrameInit():
    Unknown4007(2)
    Unknown4010(2)
    Unknown4011(3)
    Unknown3032()
    Unknown4054(7)
    SFX_0('015_blaze_0')

@State
def Eff_BGRcountSub1():

    def upon_IMMEDIATE():
        callSubroutine('CountDownFrameInit')
        Unknown23067('phef_bgr_count1')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    Unknown1099(20)
    physicsXImpulse(3000)
    physicsYImpulse(3000)
    sprite('null', 32767)
    Unknown1099(0)
    physicsXImpulse(0)
    physicsYImpulse(0)

@State
def Eff_BGRcountSub2():

    def upon_IMMEDIATE():
        callSubroutine('CountDownFrameInit')
        Unknown23067('phef_bgr_count2')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    Unknown1099(20)
    physicsXImpulse(3000)
    physicsYImpulse(-3000)
    sprite('null', 32767)
    Unknown1099(0)
    physicsXImpulse(0)
    physicsYImpulse(0)

@State
def Eff_BGRcountSub3():

    def upon_IMMEDIATE():
        callSubroutine('CountDownFrameInit')
        GFX_2('phef_bgr_count3')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    Unknown1099(20)
    physicsXImpulse(-3000)
    physicsYImpulse(-3000)
    sprite('null', 32767)
    Unknown1099(0)
    physicsXImpulse(0)
    physicsYImpulse(0)

@State
def Eff_BGRcountSub4():

    def upon_IMMEDIATE():
        callSubroutine('CountDownFrameInit')
        Unknown23067('phef_bgr_count4')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    Unknown1099(20)
    physicsXImpulse(-3000)
    physicsYImpulse(3000)
    sprite('null', 32767)
    Unknown1099(0)
    physicsXImpulse(0)
    physicsYImpulse(0)

@State
def Eff_BGRCamera():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown21010(1)
        Unknown2054(1)
        Unknown4010(2)
    sprite('null', 30)
    Unknown20009(1250)
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    Unknown20004(1)
    sprite('null', 30)
    Unknown20000(0)
    sprite('null', 32767)
    Unknown1007(300000)
    Unknown20009(1000)

@State
def Eff_BGRstart():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_bgr_start', '')
        Unknown21010(1)
        Unknown2054(1)
        Unknown1011(-10000, 10000)
        Unknown2054(1)
    sprite('null', 60)
    GFX_1('phef_ggr_start', -1)
    sprite('null', 5)
    physicsYImpulse(-1000)
    Unknown1067(50)

@State
def Eff_BGRmato():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown21010(1)
        Unknown2054(1)
        teleportRelativeY(0)
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    SFX_0('013_thunder_0')
    SFX_0('016_explode_2')
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown35()
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown35()
    SFX_0('013_thunder_0')
    SFX_0('016_explode_2')
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(-600000)
    Unknown35()
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown35()
    SFX_0('013_thunder_0')
    SFX_0('016_explode_2')
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown35()
    SFX_0('013_thunder_0')
    SFX_0('016_explode_2')
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown35()
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(-600000)
    Unknown35()
    SFX_0('013_thunder_0')
    SFX_0('016_explode_2')
    sprite('null', 3)
    GFX_0('Eff_BGRatk', -1)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown35()

@State
def Eff_BGRatk():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_bgr_water00', '')
        Unknown21010(1)
        Unknown2054(1)
        Unknown1056(300)
        Unknown1064(800)
        Unknown1011(-10000, 10000)
    sprite('null', 10)
    ScreenShake(2500, 2500)
    sprite('null', 10)
    Unknown1059(-13)
    GFX_1('phef_bgr_atk_end', -1)
    GFX_0('Eff_BGRatkEnd', -1)

@State
def Eff_BGRatkEnd():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_bgr_water01', '')
        Unknown21010(1)
        Unknown2054(1)
        Unknown1056(300)
        Unknown1064(800)
        Unknown1011(-5000, 5000)
    sprite('null', 30)
    sprite('null', 10)
    Unknown3004(-26)

@State
def Eff_BGRbg():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_bgr_bg', '')
        Unknown21010(1)
        Unknown2054(1)
        Unknown4010(2)
        teleportRelativeY(0)
        Unknown1007(600000)
        Unknown1096(600)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def ph320SmokeEff():

    def upon_IMMEDIATE():
        GFX_2('phef321_smoke')
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown1099(5)
        Unknown1062(150, 300)
        Unknown1070(0, 300)
        Unknown3001(175)
    sprite('vr_phcmn_10', 6)
    sprite('vr_phcmn_11', 6)
    sprite('vr_phcmn_12', 6)
    sprite('vr_phcmn_13', 5)
    Unknown3004(-7)
    sprite('vr_phcmn_14', 4)
    sprite('vr_phcmn_15', 4)

@State
def ph320SmokeEff2():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown1062(150, 300)
        Unknown1070(0, 300)
        Unknown3001(175)
    sprite('null', 12)
    sprite('vr_phcmn_10', 6)
    GFX_2('phef321_smoke')
    Unknown1099(5)
    sprite('vr_phcmn_11', 6)
    sprite('vr_phcmn_12', 6)
    sprite('vr_phcmn_13', 5)
    Unknown3004(-7)
    sprite('vr_phcmn_14', 4)
    sprite('vr_phcmn_15', 4)

@State
def ph320BombEff():

    def upon_IMMEDIATE():
        Unknown3032()
    sprite('null', 4)
    Unknown4003('pheff431_bomb00', '')
    GFX_1('phef_400_bom', -1)
    Unknown1096(750)
    ScreenShake(10000, 10000)
    sprite('null', 3)
    Unknown3001(0)
    Unknown1096(1800)
    Unknown4003('pheffcmn_bomb00', '')
    GFX_0('ph320BombEff2', -1)
    sprite('null', 7)
    Unknown3001(255)
    GFX_1('phef_400_bom', -1)
    GFX_1('phef321_shock', -1)
    GFX_0('ph320BombEff_Circle', -1)
    sprite('null', 10)
    Unknown3004(-26)

@State
def ph320BombEff2():

    def upon_IMMEDIATE():
        Unknown4061(3)
    sprite('vr_ph400_07', 2)
    Unknown1096(1300)
    sprite('vr_ph400_08', 2)
    sprite('vr_ph400_09', 2)
    Unknown1099(20)
    sprite('vr_ph400_06', 2)

@State
def ph320BombEff_Circle():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4003('pheff450_AddCircle', '')
        Unknown1096(650)
    sprite('null', 5)
    Unknown1099(300)
    sprite('null', 5)
    Unknown3004(-51)

@State
def pheff_400():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown4007(2)
        Unknown4010(2)
        sendToLabelUpon(32, 1)
    sprite('vr_ph400_00', 2)
    Unknown3001(0)
    Unknown3004(51)
    GFX_1('phef400_nokosi', 0)
    GFX_0('pheff_400Fire', 0)
    GFX_1('phef400_nokosi', 1)
    GFX_0('pheff_400Fire', 1)
    GFX_1('phef400_nokosi', 2)
    GFX_0('pheff_400Fire', 2)
    GFX_1('phef400_nokosi', 3)
    label(0)
    sprite('vr_ph400_00', 2)
    GFX_1('phef400_nokosi', 0)
    GFX_1('phef400_nokosi', 1)
    GFX_1('phef400_nokosi', 2)
    GFX_1('phef400_nokosi', 3)
    sprite('vr_ph400_01', 2)
    GFX_1('phef400_nokosi', 0)
    GFX_1('phef400_nokosi', 1)
    GFX_1('phef400_nokosi', 2)
    GFX_1('phef400_nokosi', 3)
    gotoLabel(0)
    label(1)
    sprite('vr_ph400_00', 2)
    Unknown21012('pheff_400Fire', 32)
    sprite('vr_ph400_01', 2)
    sprite('vr_ph400_02', 4)
    sprite('vr_ph400_03', 4)
    sprite('vr_ph400_04', 2)
    Unknown1096(1000)
    Unknown3029(0)
    sprite('vr_ph400_04', 2)
    Unknown1096(1500)
    teleportRelativeX(-40000)
    Unknown1007(-50000)
    Unknown4007(0)
    sprite('vr_ph400_05', 7)
    Unknown1096(1150)
    Unknown1007(50000)
    Unknown1007(200000)
    teleportRelativeX(40000)
    ScreenShake(10000, 10000)
    Unknown1099(15)
    GFX_0('pheff_400sub', 0)
    GFX_1('phef_400_bom', 1)
    GFX_1('phef_400_blm', 1)
    GFX_1('phef_400_bom_ground', 1)
    sprite('vr_ph400_07', 3)
    sprite('vr_ph400_08', 3)
    sprite('vr_ph400_09', 3)
    GFX_0('pheff_400sub3', 0)
    sprite('vr_ph400_06', 5)
    GFX_0('phEff400_corebom', 0)
    Unknown3004(-51)

@State
def pheff_400Fire():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ph400eff_jizoku00', '')
        Unknown4010(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown1062(-50, 200)
        sendToLabelUpon(32, 0)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(13)
    sprite('null', 32767)
    Unknown3004(0)
    label(0)
    sprite('null', 5)
    Unknown3004(51)
    Unknown1067(-30)
    sprite('null', 5)
    Unknown3004(-51)

@State
def pheff_400sub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ph240eff_00', '')
        Unknown1064(450)
        Unknown1056(600)
        Unknown2054(1)
    sprite('null', 19)
    sprite('null', 5)
    Unknown3004(-51)

@State
def phEff400_corebom():

    def upon_IMMEDIATE():
        Unknown1096(1300)
        Unknown3033()
        Unknown4061(2)
        Unknown23015(1)
    sprite('vr_ph216_03', 4)
    Unknown1099(15)
    sprite('vr_ph216_04', 4)
    sprite('vr_ph216_05', 4)

@State
def pheff_400Air():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown4007(2)
        Unknown4010(2)
        sendToLabelUpon(32, 1)

        def upon_33():
            clearUponHandler(33)
            Unknown1072(22500)

        def upon_34():
            clearUponHandler(34)
            Unknown1072(-22500)

        def upon_35():
            clearUponHandler(33)
            clearUponHandler(34)
            clearUponHandler(35)
            Unknown1072(0)
    sprite('vr_ph400_00', 2)
    Unknown3001(0)
    Unknown3004(51)
    GFX_1('phef400_nokosi', 0)
    GFX_0('pheff_400Fire', 0)
    GFX_1('phef400_nokosi', 1)
    GFX_0('pheff_400Fire', 1)
    GFX_1('phef400_nokosi', 2)
    GFX_0('pheff_400Fire', 2)
    GFX_1('phef400_nokosi', 3)
    label(0)
    sprite('vr_ph400_00', 2)
    GFX_1('phef400_nokosi', 0)
    GFX_1('phef400_nokosi', 1)
    GFX_1('phef400_nokosi', 2)
    GFX_1('phef400_nokosi', 3)
    sprite('vr_ph400_01', 2)
    GFX_1('phef400_nokosi', 0)
    GFX_1('phef400_nokosi', 1)
    GFX_1('phef400_nokosi', 2)
    GFX_1('phef400_nokosi', 3)
    gotoLabel(0)
    label(1)
    sprite('vr_ph400_00', 2)
    Unknown21012('pheff_400Fire', 32)
    sprite('vr_ph400_01', 2)
    sprite('vr_ph400_02', 4)
    sprite('vr_ph400_03', 4)
    sprite('vr_ph400_04', 2)
    Unknown3029(0)
    sprite('vr_ph400_04', 2)
    Unknown1072(0)
    Unknown1096(1500)
    teleportRelativeX(-40000)
    Unknown1007(-50000)
    Unknown4007(0)
    sprite('vr_ph400_05', 7)
    Unknown1096(1150)
    teleportRelativeX(40000)
    Unknown1007(50000)
    Unknown1007(200000)
    ScreenShake(10000, 10000)
    Unknown1099(15)
    GFX_0('pheff_400sub2', 1)
    GFX_1('phef_400_bom', 1)
    GFX_1('phef_400_blm', 1)
    sprite('vr_ph400_07', 3)
    sprite('vr_ph400_08', 3)
    GFX_1('phef321_shock2', -1)
    sprite('vr_ph400_09', 3)
    sprite('vr_ph400_06', 5)
    GFX_0('pheff_400sub3', 0)
    GFX_0('phEff400_corebom', 0)
    Unknown3004(-51)

@State
def pheff_400sub2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ph240eff_01', '')
        Unknown1096(300)
        teleportRelativeX(25000)
        Unknown3001(200)
    sprite('null', 23)
    Unknown1099(4)

@State
def pheff_400sub3():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ph240eff_02', '')
        Unknown1007(-100000)
        Unknown1096(500)
        Unknown2054(1)
    sprite('null', 13)
    sprite('null', 10)
    Unknown3004(-26)

@State
def MidAssault_Atk():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown1056(6000)
        Unknown1064(15000)
        Unknown1007(80000)
        if (SLOT_19 > 550000):
            Unknown1008()
            Unknown1086(22)
            Unknown1009()
        else:
            teleportRelativeX(550000)
        ProjectileHitsWall(1)
        Unknown4010(3)
        Unknown4011(3)
        AttackLevel_(5)
        Damage(1500)
        AirPushbackX(-12000)
        AirPushbackY(-30000)
        AirUntechableTime(45)
        HitAirUnblockable(3)
        HitOverhead(2)
        GroundedHitstunAnimation(9)
        StarterRating(3)
        GroundUntechableTime(10)
        AttackP1(90)
        AttackP2(85)
        Unknown9190(1)
        Unknown11089(10)
        Unknown9017(1)
        FatalCounter(1)
        HitAirUnblockable(0)
        Unknown3038(1)
        if SLOT_137:
            Unknown10000(80)
        Unknown9192(1)
        Unknown9120(50)
        Unknown9312(1)
        StarterRating(3)

        def upon_32():
            blockstun(25)

        def upon_33():
            sendToLabel(1)

        def upon_34():
            Damage(1625)

        def upon_12():
            Unknown21007(3, 32)

        def upon_60():
            AirPushbackX(-9000)
            AirPushbackY(-90000)
            StarterRating(3)
    sprite('null', 10)
    label(0)
    sprite('null', 4)
    GFX_0('Eff_402', -1)
    SFX_0('016_explode_1')
    sprite('vr_ph_magictest', 5)
    Unknown8003(104, 1, 1)
    ExitState()
    label(1)
    sprite('null', 4)
    Unknown1056(7200)
    Unknown1064(14400)
    GFX_0('Eff_402_G', -1)
    SFX_0('016_explode_2')
    sprite('vr_ph_magictest', 5)
    Unknown8003(104, 1, 1)
    ExitState()

@State
def Eff_402():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(2)
        Unknown4061(5)
        GFX_2('phef402_mc')
        Unknown1007(-60000)
        Unknown2007()
    sprite('ph402_cutin_a', 2)
    sprite('ph402_cutin_b', 1)
    Unknown3032()
    sprite('ph402_cutin_c', 1)
    sprite('ph402_cutin', 3)
    GFX_0('Eff_402Fire', -1)
    sprite('ph402_cutin', 15)
    Unknown4009(0)
    GFX_1('phef_402_end_g', -1)
    sprite('ph402_cutin', 2)
    Unknown3004(-26)
    GFX_1('phef402_end_sita', -1)
    GFX_1('phef402_end', 0)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 1)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 2)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 3)

@State
def Eff_402Fire():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown3001(160)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(2)
        Unknown4061(2)
        Unknown23015(3)
        GFX_2('phef402_sub')
    sprite('vr_ph402_00', 3)
    Unknown1096(1200)
    sprite('vr_ph402_00', 3)
    Unknown4009(0)
    sprite('vr_ph402_01', 3)
    sprite('vr_ph402_02', 3)
    sprite('vr_ph402_03', 3)
    Unknown3001(255)
    Unknown1096(1200)
    sprite('vr_ph402_04', 3)
    Unknown1096(1100)
    sprite('vr_ph402_05', 5)
    Unknown1096(1000)
    Unknown3004(-51)

@State
def Eff_402_G():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4061(5)
        GFX_2('phef402_mc')
        Unknown1007(-60000)
        Unknown2007()
        Unknown1097(150)
    sprite('ph402_cutin_a', 2)
    sprite('ph402_cutin_b', 1)
    Unknown3032()
    sprite('ph402_cutin_c', 1)
    sprite('ph402_cutin', 3)
    GFX_0('Eff_402Fire_G', -1)
    sprite('ph402_cutin', 15)
    Unknown4010(0)
    Unknown4009(0)
    GFX_1('phef_402_end_g', -1)
    sprite('ph402_cutin', 2)
    Unknown3004(-26)
    GFX_1('phef402_end_sita', -1)
    GFX_1('phef402_end', 0)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 1)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 2)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 3)

@State
def Eff_402Fire_G():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown3001(160)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown23015(3)
        GFX_2('phef402_sub')
    sprite('vr_ph402_00', 3)
    Unknown1096(1400)
    sprite('vr_ph402_00', 3)
    Unknown4010(0)
    Unknown4009(0)
    sprite('vr_ph402_01', 3)
    sprite('vr_ph402_02', 3)
    sprite('vr_ph402_03', 3)
    Unknown3001(255)
    sprite('vr_ph402_04', 3)
    Unknown1096(1300)
    sprite('vr_ph402_05', 5)
    Unknown1096(1200)
    Unknown3004(-51)

@State
def Eff_402Fire_PL():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown3001(255)
        Unknown4061(2)
        Unknown23015(3)
        Unknown1096(2000)
        Unknown4010(3)
        Unknown4011(3)
    sprite('vr_ph402_10', 3)
    GFX_2('phef402_mcadd_g')
    sprite('vr_ph402_10', 3)
    Unknown1096(1700)
    sprite('vr_ph402_11', 3)
    sprite('vr_ph402_12', 3)
    sprite('vr_ph402_13', 3)

@State
def Eff_401():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(5)
        Unknown23015(13)
        teleportRelativeX(-140000)
        Unknown3032()
        Unknown3001(0)
        AttackLevel_(4)
        Damage(1100)
        AirPushbackY(44000)
        AirUntechableTime(45)
        AirPushbackX(25000)
        AirPushbackY(50000)
        Unknown9072(50000)
        CounterHitAirPushbackY(40000)
        Unknown9180(1)
        Unknown9108(35)
        Unknown9360(60)
        Unknown9363(1)
        Unknown9365(30)
        HitAirUnblockable(3)
        GroundedHitstunAnimation(9)
        AttackP1(90)
        AttackP2(82)
        Unknown11089(10)
        Unknown9017(1)
        StarterRating(0)
        if SLOT_137:
            Unknown10000(80)

        def upon_12():
            Unknown21007(3, 32)
    sprite('null', 3)
    GFX_0('Eff_401Fire', -1)
    sprite('null', 3)
    sprite('ph401_cutin', 6)
    Unknown3001(255)
    sprite('ph401_cutin', 3)
    Unknown2001()
    Unknown4009(0)
    Unknown4007(0)
    sprite('ph401_cutin', 10)
    Unknown3004(-51)

@State
def Eff_401Fire():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(2)
        Unknown4061(2)
        Unknown23015(14)
        Unknown1096(1300)
        teleportRelativeX(35000)
        GFX_2('phef401_sub')
    sprite('vr_ph401_00', 3)
    sprite('vr_ph401_01', 3)
    teleportRelativeX(22500)
    sprite('vr_ph401_02', 5)
    teleportRelativeX(22500)
    sprite('vr_ph401_03', 3)
    Unknown4009(0)
    sprite('vr_ph401_04', 3)
    sprite('vr_ph401_05', 3)
    GFX_1('phef401_hinoko', -1)
    sprite('vr_ph401_06', 3)
    GFX_1('phef402_end', 0)
    GFX_1('phef402_end', 1)
    GFX_1('phef402_end', 2)
    GFX_1('phef402_end', 3)
    GFX_1('phef402_end', 4)
    sprite('vr_ph401_07', 3)
    sprite('null', 10)

@State
def Eff_401_G():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(5)
        Unknown23015(13)
        teleportRelativeX(-140000)
        Unknown3032()
        Unknown3001(0)
        Unknown1096(1000)
    sprite('null', 3)
    GFX_0('Eff_401Fire_G', -1)
    sprite('null', 3)
    sprite('ph401_cutin', 5)
    Unknown3001(255)
    sprite('ph401_cutin', 3)
    Unknown4009(0)
    Unknown4007(0)
    Unknown4010(0)
    sprite('ph401_cutin', 10)
    Unknown3004(-51)

@State
def Eff_401Fire_G():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(2)
        Unknown4061(2)
        Unknown23015(14)
        Unknown1096(2000)
        teleportRelativeX(35000)
        GFX_2('phef401_sub')
    sprite('vr_ph401_00', 3)
    sprite('vr_ph401_01', 3)
    teleportRelativeX(37500)
    sprite('vr_ph401_02', 5)
    teleportRelativeX(37500)
    sprite('vr_ph401_03', 3)
    Unknown4009(0)
    sprite('vr_ph401_04', 3)
    sprite('vr_ph401_05', 3)
    GFX_1('phef401_hinoko', -1)
    sprite('vr_ph401_06', 3)
    GFX_1('phef402_end', 0)
    GFX_1('phef402_end', 1)
    GFX_1('phef402_end', 2)
    GFX_1('phef402_end', 3)
    GFX_1('phef402_end', 4)
    sprite('vr_ph401_07', 3)
    sprite('null', 10)

@State
def Eff_MagicConv():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_2('phef403_flash')
    sprite('null', 60)

@State
def pheff_BufWaterMato():

    def upon_IMMEDIATE():
        Unknown2054(1)

        def upon_16():
            Unknown2071('0300000000000000e80300006400000001000000')
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    GFX_0('pheff_BufWater', -1)
    sprite('null', 2)
    GFX_0('pheff_BufWater', -1)
    Unknown36(1)
    Unknown2005()
    Unknown35()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown21012('pheff_BufWater', 32)

@State
def pheff_BufWater():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(4)
        Unknown1096(600)
        Unknown1102(-100, 400)
        Unknown1010(-130000, 130000)
        Unknown1011(-125000, 60000)
        Unknown3001(200)
        Unknown23015(11)
        Unknown4007(2)
        Unknown4025(3)
        sendToLabelUpon(32, 0)
    sprite('vrpheff_buffw00', 5)
    Unknown1067(40)
    Unknown1059(20)
    sprite('vrpheff_buffw01', 2)
    sprite('vrpheff_buffw02', 3)
    GFX_2('pheff404_sub2')
    Unknown4007(0)
    sprite('vrpheff_buffw03', 3)
    sprite('vrpheff_buffw04', 3)
    Unknown3004(-22)
    sprite('vrpheff_buffw05', 2)
    sprite('vrpheff_buffw06', 2)
    sprite('vrpheff_buffw07', 2)
    gotoLabel(1)
    label(0)
    sprite('keep', 9)
    Unknown3004(-25)
    gotoLabel(1)
    label(1)
    sprite('null', 1)

@State
def pheff_BufFireMato():

    def upon_IMMEDIATE():
        Unknown2054(1)

        def upon_16():
            Unknown2071('0300000000000000e80300006400000001000000')
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    GFX_0('pheff_BufFire', -1)
    sprite('null', 2)
    GFX_0('pheff_BufFire', -1)
    Unknown36(1)
    Unknown2005()
    Unknown35()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown21012('pheff_BufFire', 32)

@State
def pheff_BufFire():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown3029(1)
        Unknown3071(2)
        Unknown4061(4)
        Unknown3001(200)
        Unknown1096(825)
        Unknown1102(-100, 400)
        Unknown1062(0, 200)
        Unknown1010(-130000, 130000)
        Unknown1011(-125000, 60000)
        Unknown23015(11)
        Unknown4007(2)
        Unknown4025(3)
        Unknown21010(1)
        Unknown2054(1)
        sendToLabelUpon(32, 0)
    sprite('vrpheff_bufff00', 3)
    sprite('vrpheff_bufff01', 3)
    sprite('vrpheff_bufff02', 3)
    Unknown4007(0)
    GFX_2('pheff404_sub')
    sprite('vrpheff_bufff03', 3)
    sprite('vrpheff_bufff04', 3)
    Unknown3004(-16)
    sprite('vrpheff_bufff05', 3)
    sprite('vrpheff_bufff06', 3)
    sprite('vrpheff_bufff07', 3)
    gotoLabel(1)
    label(0)
    sprite('keep', 9)
    Unknown3004(-25)
    gotoLabel(1)
    label(1)
    sprite('null', 1)

@State
def pheff_BufWindMato():

    def upon_IMMEDIATE():
        Unknown2054(1)

        def upon_16():
            Unknown2071('0300000000000000e80300006400000001000000')
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 3)
    GFX_0('pheff_BufWind', -1)
    sprite('null', 3)
    GFX_0('pheff_BufWind', -1)
    Unknown36(1)
    Unknown2005()
    Unknown35()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown21012('pheff_BufWind', 32)

@State
def pheff_BufWind():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(4)
        Unknown3001(200)
        Unknown1096(800)
        Unknown1102(-100, 400)
        Unknown1010(-130000, 130000)
        Unknown1011(-125000, 60000)
        Unknown3029(1)
        Unknown3071(2)
        Unknown23015(11)
        Unknown4007(2)
        Unknown4025(3)
        Unknown21010(1)
        Unknown2054(1)
        sendToLabelUpon(32, 0)
    sprite('vrpheff_buffk00', 3)
    Unknown1067(35)
    Unknown1059(-7)
    sprite('vrpheff_buffk01', 3)
    sprite('vrpheff_buffk02', 3)
    Unknown4007(0)
    GFX_2('pheff404_sub3')
    physicsYImpulse(1500)
    sprite('vrpheff_buffk03', 3)
    sprite('vrpheff_buffk04', 3)
    Unknown3004(-16)
    sprite('vrpheff_buffk05', 3)
    sprite('vrpheff_buffk06', 3)
    sprite('vrpheff_buffk07', 3)
    gotoLabel(1)
    label(0)
    sprite('keep', 9)
    Unknown3004(-25)
    gotoLabel(1)
    label(1)
    sprite('null', 1)

@State
def Eff_BuffAtkR():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown1007(200000)
        Unknown4010(2)
        Unknown4007(3)
    sprite('null', 7)
    sprite('null', 24)
    GFX_0('Eff_BuffAtkRSub', -1)

@State
def Eff_BuffAtkRSub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(3)
        Unknown4003('pheff_buffatk00', '')
        GFX_2('pheff_buffatkR')
        Unknown1096(500)
    sprite('null', 9)
    Unknown21010(1)
    sprite('null', 10)
    Unknown21010(0)
    sprite('null', 4)
    Unknown1099(10)

@State
def Eff_BuffAtkB():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown1007(200000)
        Unknown4010(2)
        Unknown4007(3)
    sprite('null', 7)
    sprite('null', 24)
    GFX_0('Eff_BuffAtkBSub', -1)

@State
def Eff_BuffAtkBSub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(3)
        Unknown4003('pheff_buffatk01', '')
        GFX_2('pheff_buffatkB')
        Unknown1096(500)
    sprite('null', 9)
    Unknown21010(1)
    sprite('null', 10)
    Unknown21010(0)
    sprite('null', 4)
    Unknown1099(10)

@State
def Eff_BuffAtkG():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown1007(200000)
        Unknown4010(2)
        Unknown4007(3)
    sprite('null', 7)
    sprite('null', 24)
    GFX_0('Eff_BuffAtkGSub', -1)

@State
def Eff_BuffAtkGSub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(3)
        Unknown4003('pheff_buffatk02', '')
        GFX_2('pheff_buffatkG')
        Unknown1096(500)
    sprite('null', 9)
    Unknown21010(1)
    sprite('null', 10)
    Unknown21010(0)
    sprite('null', 4)
    Unknown1099(10)

@State
def UltimateShotAtk1st():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(3500)
        teleportRelativeX(850000)
        Unknown1007(180000)
        AttackLevel_(3)
        Damage(400)
        MinimumDamagePct(10)
        AttackP1(90)
        AttackP2(79)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirUntechableTime(30)
        hitstun(30)
        AirPushbackX(15000)
        AirPushbackY(4000)
        Unknown9190(1)
        Unknown9118(85)
        Hitstop(0)
        Unknown11001(3, 3, 5)
        Unknown11057(500)
        Unknown9016(1)
        StarterRating(2)
        Unknown3038(1)

        def upon_CLEAR_OR_EXIT():
            if Unknown2065(23):
                clearUponHandler(3)
                Unknown21007(3, 41)
    sprite('vr_ph_magictest', 8)
    GFX_0('Eff_430_Beam00', -1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('null', 1)
    Unknown21012('Eff_430_Beam00', 32)

@State
def Eff_430_cap():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4010(2)
        Unknown3029(1)
    sprite('vr_ph430_cap', 6)
    sprite('vr_ph430_cap', 5)
    physicsYImpulse(30000)
    physicsXImpulse(-7500)
    Unknown1074(3000)
    sprite('vr_ph430_cap', 5)
    Unknown3004(-51)

@State
def Eff_430_capFire():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        Unknown1007(20000)
        Unknown2054(1)
    sprite('vr_ph430_00', 4)
    sprite('vr_ph430_01', 4)
    sprite('vr_ph430_02', 4)
    sprite('vr_ph430_03', 4)
    sprite('vr_ph430_04', 4)
    sprite('vr_ph430_06', 4)
    sprite('vr_ph430_07', 4)

@State
def Eff_430_Beam00():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3032()
        Unknown4003('ph430eff_00', '')
        teleportRelativeX(-800000)
        Unknown1007(45000)
        GFX_2('phef430_mc')
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 2)
    Unknown1065(-75)
    SFX_0('014_electric_ll')
    SFX_3('phse_11')
    sprite('null', 2)
    Unknown1065(75)
    SFX_0('014_electric_l')
    SFX_3('phse_11')
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_1('phef430_beamend_00', -1)
    GFX_0('Eff_430_Beam01', -1)

@State
def Eff_430_Beam01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ph430eff_01', '')
        Unknown2054(1)
        Unknown21010(1)
    sprite('null', 3)
    sprite('null', 3)
    Unknown1065(25)
    sprite('null', 3)
    Unknown1065(25)
    sprite('null', 3)
    Unknown1065(25)
    sprite('null', 4)

@State
def Eff_430_hinoNemoto():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff430od_00', '')
        GFX_2('phef430_hngate')
        Unknown2054(1)
        Unknown4010(2)
        Unknown4007(2)
        Unknown1096(1400)
        sendToLabelUpon(32, 1)
    sprite('null', 32767)
    label(1)
    sprite('null', 3)
    sprite('null', 6)
    Unknown3004(-42)

@State
def Eff_430_hinoEnter():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff430od_01', '')
        Unknown2054(1)
        Unknown4010(2)
        Unknown4007(2)
    sprite('null', 5)
    Unknown1096(1200)
    sprite('null', 5)
    Unknown1096(1700)
    sprite('null', 5)
    Unknown3004(-17)
    sprite('null', 4)
    GFX_0('Eff_430_hinoEnterEnd', -1)

@State
def Eff_430_hinoEnterEnd():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff430od_02', '')
        Unknown2054(1)
        Unknown21010(1)
        Unknown1096(1000)
        teleportRelativeX(300000)
        physicsXImpulse(7500)
    sprite('null', 20)
    Unknown1099(30)

@State
def Eff_430_TameEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff430odbeam_00', '')
        GFX_2('phef430_beamtame')
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown1007(240000)
        teleportRelativeX(380000)
        Unknown1096(60)
        sendToLabelUpon(32, 1)
    sprite('null', 5)
    Unknown1099(300)
    sprite('null', 5)
    Unknown1099(0)
    label(0)
    sprite('null', 1)
    Unknown1097(200)
    ScreenShake(2500, 2500)
    sprite('null', 1)
    Unknown1097(-100)
    sprite('null', 1)
    Unknown1097(200)
    sprite('null', 1)
    Unknown1097(-100)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    ScreenShake(10000, 10000)
    Unknown1096(1000)
    Unknown3001(0)

@State
def Eff_430_HinoBeamEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3038(1)
        Unknown4003('pheff430odbeam_01', '')
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown1096(1000)
        Unknown1065(1200)
        teleportRelativeX(-650000)
        Unknown1007(250000)
        sendToLabelUpon(32, 1)
    sprite('vr_ph430_effpos', 5)
    Unknown1067(80)
    Unknown1064(120)
    SFX_0('016_explode_2')
    sprite('vr_ph430_effpos', 5)
    SFX_3('phse_02')
    sprite('vr_ph430_effpos', 5)
    Unknown1067(10)
    sprite('vr_ph430_effpos', 5)
    Unknown1067(0)
    GFX_1('phef_430_shock', 0)
    GFX_1('phef_430_shock', 2)
    label(0)
    sprite('vr_ph430_effpos', 1)
    Unknown1057(-50)
    Unknown1065(50)
    GFX_1('phef_430_shock', 0)
    GFX_1('phef_430_shock', 2)
    SFX_3('phse_02')
    sprite('vr_ph430_effpos', 1)
    Unknown1065(-50)
    Unknown1057(50)
    sprite('vr_ph430_effpos', 1)
    Unknown1057(-50)
    Unknown1065(50)
    sprite('vr_ph430_effpos', 1)
    Unknown1065(-50)
    Unknown1057(50)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_0('Eff_430_HinoBeamEffEnd', -1)

@State
def Eff_430_HinoBeamEffEnd():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff430odbeam_02', '')
        Unknown21010(1)
        Unknown2054(1)
    sprite('null', 10)
    Unknown4003('pheff430odbeam_02', '')
    sprite('vr_ph430odbeam_expos', 1)
    Unknown3038(1)
    GFX_1('phef430_beamend', 0)
    GFX_1('phef430_beamend', 1)
    GFX_1('phef430_beamend', 2)
    GFX_1('phef430_beamend', 3)
    GFX_1('phef430_beamend', 4)
    GFX_1('phef430_beamend', 5)

@State
def UltimateShotAtk2nd():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(7000)
        teleportRelativeX(850000)
        Unknown1007(130000)
        AttackLevel_(4)
        Damage(325)
        MinimumDamagePct(20)
        AttackP1(90)
        AttackP2(82)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirUntechableTime(30)
        hitstun(30)
        AirPushbackX(35000)
        AirPushbackY(4500)
        Unknown9178(1)
        WallbounceReboundTime(55)
        AirHitstunAfterWallbounce(60)
        Hitstop(0)
        Unknown11001(3, 3, 5)
        Unknown11057(500)
        Unknown9016(1)
        Unknown11108('03000000')
        StarterRating(2)
        Unknown3038(1)
    sprite('vr_ph_magictest', 7)
    GFX_0('Eff_430_Beam00', -1)
    Unknown36(1)
    Unknown1097(150)
    Unknown1007(30000)
    Unknown35()
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('null', 1)
    Unknown21012('Eff_430_Beam00', 32)

@State
def UltimateShotAtk1stOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(3500)
        teleportRelativeX(850000)
        Unknown1007(180000)
        AttackLevel_(3)
        Unknown9001(4)
        Damage(400)
        MinimumDamagePct(10)
        AttackP1(90)
        AttackP2(79)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirUntechableTime(30)
        hitstun(30)
        AirPushbackX(15000)
        AirPushbackY(4000)
        Unknown9190(1)
        Unknown9118(85)
        Hitstop(0)
        Unknown11001(3, 3, 5)
        Unknown11057(500)
        Unknown9016(1)
        StarterRating(2)
        Unknown3038(1)

        def upon_CLEAR_OR_EXIT():
            if Unknown2065(23):
                clearUponHandler(3)
                Unknown21007(3, 41)
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    GFX_0('Eff_430_Beam00', -1)
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    sprite('vr_ph_magictest', 8)
    RefreshMultihit()
    Unknown21012('Eff_430_Beam00', 32)

@State
def UltimateShotAtk2ndOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(7000)
        teleportRelativeX(850000)
        Unknown1007(130000)
        AttackLevel_(4)
        Unknown9001(4)
        Damage(325)
        MinimumDamagePct(20)
        AttackP1(90)
        AttackP2(82)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirUntechableTime(30)
        hitstun(30)
        AirPushbackX(35000)
        AirPushbackY(4500)
        Unknown9178(1)
        WallbounceReboundTime(55)
        AirHitstunAfterWallbounce(60)
        Hitstop(0)
        Unknown11001(3, 3, 5)
        Unknown11057(500)
        Unknown9016(1)
        Unknown11108('03000000')
        StarterRating(2)
        Unknown3038(1)
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    GFX_0('Eff_430_Beam00', -1)
    Unknown36(1)
    Unknown1097(150)
    Unknown1007(30000)
    Unknown35()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()
    sprite('vr_ph_magictest', 7)
    RefreshMultihit()

    def upon_12():
        Unknown21007(3, 32)
    Unknown21012('Eff_430_Beam00', 32)

@State
def UltimateShotAtk3rdOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(20000)
        teleportRelativeX(850000)
        Unknown1007(140000)
        AttackLevel_(5)
        Unknown9001(4)
        Damage(200)
        MinimumDamagePct(20)
        AttackP1(90)
        AttackP2(84)
        Unknown11092(1)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirUntechableTime(60)
        hitstun(60)
        AirPushbackX(40000)
        AirPushbackY(15000)
        Hitstop(0)
        Unknown11001(4, 4, 6)
        Unknown11057(500)
        Unknown9017(1)
        Unknown11108('03000000')
        StarterRating(2)
        Unknown3038(1)
    sprite('vr_ph_magictest', 5)
    GFX_0('Eff_430_HinoBeamEff', -1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('vr_ph_magictest', 5)
    RefreshMultihit()
    sprite('null', 10)
    Unknown21012('Eff_430_HinoBeamEff', 32)
    Unknown21012('UltimateShotHinokagutsuchi', 32)

@State
def UltimateShotODCamera():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)

        def upon_CLEAR_OR_EXIT():
            Unknown1086(3)
            SLOT_51 = SLOT_19
            SLOT_51 = (SLOT_51 / 2)
            Unknown48(23, 2, 52, 3, 2, 22)
            Unknown48(23, 2, 53, 22, 2, 22)
            if (SLOT_52 < SLOT_53):
                SLOT_22 = (SLOT_22 + SLOT_51)
            elif (SLOT_52 > SLOT_53):
                SLOT_22 = (SLOT_22 - SLOT_51)
            else:
                pass
            SLOT_22 = (SLOT_22 + 50000)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(1)
    label(0)
    sprite('null', 120)
    Unknown20000(1)
    Unknown20003(1)
    label(1)
    sprite('null', 1)
    Unknown20000(0)
    Unknown20003(0)

@State
def UltimateShotHinokagutsuchi():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(11)
        Unknown2054(1)
        Unknown4010(3)
        Unknown4011(3)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)
    sprite('ph430cutin_00', 15)
    Unknown3001(0)
    GFX_0('Eff_430_hinoEnter', 0)
    sprite('ph430cutin_00', 27)
    Unknown3004(51)
    ScreenShake(10000, 10000)
    GFX_0('Eff_430_hinoNemoto', 0)
    GFX_1('phef430_end', 1)
    GFX_1('phef430_end', 2)
    GFX_1('phef430_end', 3)
    GFX_1('phef430_end', 4)
    GFX_1('phef430_end', 5)
    GFX_1('phef430_end', 6)
    GFX_0('Eff_430_TameEff', -1)
    sprite('ph430cutin_01', 3)
    Unknown3026(-4934476)
    sprite('ph430cutin_02', 3)
    Unknown3026(-6250336)
    sprite('ph430cutin_03', 3)
    Unknown3026(-10197916)
    GFX_0('UltimateShotAtk3rdOD', -1)
    Unknown21012('Eff_430_TameEff', 32)
    Unknown1045(-20000)
    sprite('ph430cutin_03', 300)
    label(1)
    sprite('ph430cutin_02', 3)
    Unknown3004(-31)
    sprite('ph430cutin_01', 3)
    Unknown21012('Eff_430_hinoNemoto', 32)
    sprite('ph430cutin_00', 3)
    GFX_1('phef402_end', 1)
    GFX_1('phef402_end', 2)
    GFX_1('phef402_end', 3)
    GFX_1('phef402_end', 4)
    GFX_1('phef402_end', 5)
    GFX_1('phef402_end', 6)
    sprite('null', 2)

@Subroutine
def UltimateLock_Atk1stInit():
    AttackLevel_(3)
    Damage(250)
    MinimumDamagePct(20)
    Hitstop(3)
    Unknown11057(500)
    Unknown11083(1)
    Unknown11001(60, 60, 60)
    AttackP2(79)
    Unknown11092(1)
    Unknown9017(1)
    Unknown11072(1, 0, 50000)
    Unknown11064(1)
    Unknown11108('03000000')
    StarterRating(2)
    if SLOT_137:
        Unknown10000(80)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')

@State
def Eff_432_AtkFire():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4061(2)
        Unknown2005()
        Unknown1056(900)
        Unknown1064(1200)
        Unknown1007(-25000)
    sprite('vr_ph432_00', 6)
    GFX_0('Eff_432_AtkFireSub', -1)
    sprite('vr_ph432_01', 6)
    sprite('vr_ph432_02', 5)
    sprite('vr_ph432_03', 4)
    sprite('vr_ph432_04', 4)
    sprite('vr_ph432_05', 2)

@State
def Eff_432_AtkFireSub():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4061(2)
        Unknown1056(-700)
        Unknown1064(700)
    sprite('vr_ph432_00', 4)
    sprite('vr_ph432_01', 4)
    sprite('vr_ph432_02', 4)
    sprite('vr_ph432_03', 4)
    sprite('vr_ph432_04', 4)
    sprite('vr_ph432_05', 4)

@State
def UltimateLock_Atk1stLv1():

    def upon_IMMEDIATE():
        Unknown17011('UltimateLock_Atk1stLv1Exe', 3, 0, 0)
        Unknown2018(0, 50)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        ThrowRange(-1)
        Unknown11002(-1)
        Unknown1056(10000)
        Unknown1064(15000)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown3038(1)
    sprite('vr_ph_magictest', 5)
    StartMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    RefreshMultihit()
    GFX_0('Eff_432_yariLv1', -1)

@State
def Eff_432_yariLv1():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff432_yari00', '')
        Unknown2054(1)
        Unknown1096(1750)
    sprite('null', 20)
    GFX_0('Eff_432_Boya', -1)
    sprite('null', 50)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown21012('Eff_432_Boya', 32)

@State
def Eff_432_Boya():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown2054(1)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 8)
    GFX_1('phef432_fire00', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 1)

@State
def UltimateLock_Atk1stLv1Exe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown1056(10000)
        Unknown1064(25000)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown3038(1)
        callSubroutine('UltimateLock_Atk1stInit')
    sprite('vr_ph_magictest', 1)
    Unknown5000(24, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    DisableAttackRestOfMove()
    Unknown36(22)
    teleportRelativeY(50000)
    Unknown35()
    sprite('vr_ph_magictest', 3)
    Unknown5000(24, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()

@State
def UltimateLock_Atk1stLv2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateLock_Atk1stLv2Exe', 3, 0, 0)
        Unknown2018(0, 50)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        ThrowRange(-1)
        Unknown11002(-1)
        Unknown1056(10000)
        Unknown1064(15000)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown3038(1)
    sprite('vr_ph_magictest', 5)
    StartMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    GFX_0('Eff_432_yariLv2', -1)

@State
def Eff_432_yariLv2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff432_yari00', '')
        Unknown2054(1)
        Unknown1096(1750)
    sprite('null', 5)
    sprite('null', 45)
    GFX_0('Eff_432_yariLv2sub', -1)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown21012('Eff_432_yariLv2sub', 32)

@State
def Eff_432_yariLv2sub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff432_yari04', '')
        Unknown2054(1)
        Unknown1056(1200)
        Unknown1064(1400)
        Unknown1007(-20000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 8)
    GFX_1('phef432_fire00', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown1067(80)

@State
def UltimateLock_Atk1stLv2Exe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown1056(10000)
        Unknown1064(25000)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown3038(1)
        callSubroutine('UltimateLock_Atk1stInit')
    sprite('vr_ph_magictest', 1)
    Unknown5000(24, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    DisableAttackRestOfMove()
    Unknown36(22)
    teleportRelativeY(50000)
    Unknown35()
    SFX_0('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    Unknown5000(24, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    RefreshMultihit()
    SFX_0('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('015_blaze_0')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('015_blaze_0')

@State
def UltimateLock_Atk1stLv3():

    def upon_IMMEDIATE():
        Unknown17011('UltimateLock_Atk1stLv3Exe', 3, 0, 0)
        Unknown2018(0, 50)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        ThrowRange(-1)
        Unknown11002(-1)
        Unknown1056(10000)
        Unknown1064(15000)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown3038(1)
    sprite('vr_ph_magictest', 5)
    StartMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    GFX_0('Eff_432_yari', -1)

@State
def Eff_432_yari():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff432_yari00', '')
        Unknown2054(1)
        Unknown1096(1750)
    sprite('null', 4)
    GFX_0('Eff_432_Boya', -1)
    GFX_0('Eff_432_yari_sub2', -1)
    GFX_0('Eff_432_yari_sub1', -1)
    Unknown36(1)
    Unknown1007(50000)
    Unknown35()
    sprite('null', 4)
    GFX_0('Eff_432_yari_sub1', -1)
    Unknown36(1)
    Unknown1007(250000)
    Unknown1097(-300)
    Unknown35()
    sprite('null', 4)
    GFX_0('Eff_432_yari_sub1', -1)
    Unknown36(1)
    Unknown1007(435000)
    Unknown1097(-600)
    Unknown35()
    sprite('null', 14)
    GFX_0('Eff_432_yari_sub1', -1)
    Unknown36(1)
    Unknown1007(640000)
    Unknown1097(-900)
    Unknown35()
    sprite('null', 50)
    Unknown21012('Eff_432_yari_sub2', 32)
    Unknown21012('Eff_432_yari_sub1', 32)
    sprite('null', 10)
    Unknown21012('Eff_432_Boya', 32)
    Unknown3004(-26)

@State
def Eff_432_yari_sub1():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff432_yari01', '')
        Unknown2054(1)
        Unknown1096(4000)
        teleportRelativeX(50000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown1099(-120)

@State
def Eff_432_yari_sub2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff432_yari02', '')
        Unknown2054(1)
        Unknown1056(500)
        Unknown1064(2000)
        teleportRelativeX(50000)
        sendToLabelUpon(32, 0)
    sprite('null', 5)
    Unknown3001(0)
    Unknown3004(51)
    ScreenShake(15000, 15000)
    Unknown1059(300)
    sprite('null', 32767)
    Unknown1059(0)
    label(0)
    sprite('null', 5)
    Unknown3004(-26)
    Unknown1099(-120)
    sprite('null', 5)
    GFX_0('Eff_432_yari_sub3', -1)

@State
def Eff_432_yari_sub3():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4003('pheff432_yari03', '')
        Unknown2054(1)
        Unknown1096(2000)
    sprite('null', 15)

@State
def UltimateLock_Atk1stLv3Exe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown1056(10000)
        Unknown1064(25000)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown3038(1)
        callSubroutine('UltimateLock_Atk1stInit')
    sprite('vr_ph_magictest', 1)
    Unknown5000(24, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    DisableAttackRestOfMove()
    Unknown36(22)
    teleportRelativeY(50000)
    Unknown35()
    SFX_3('phse_02')
    sprite('vr_ph_magictest', 3)
    Unknown5000(24, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    RefreshMultihit()
    SFX_0('019_quake_1')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_3('phse_02')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('019_quake_1')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_3('phse_02')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('019_quake_1')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    SFX_0('019_quake_1')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()

@State
def UltimateLock_Atk1stLv3Exe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown1056(10000)
        Unknown1064(25000)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown3038(1)
        callSubroutine('UltimateLock_Atk1stInit')
    sprite('vr_ph_magictest', 1)
    Unknown5000(24, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    DisableAttackRestOfMove()
    Unknown36(22)
    teleportRelativeY(50000)
    Unknown35()
    sprite('vr_ph_magictest', 3)
    Unknown5000(24, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()

@Subroutine
def UltimateLock_Atk2ndInit():
    MinimumDamagePct(10)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirUntechableTime(60)
    hitstun(60)
    AirPushbackX(45000)
    AirPushbackY(15000)
    Unknown11057(400)
    Unknown11108('03000000')
    Unknown9178(1)
    WallbounceReboundTime(0)
    Hitstop(1)
    Unknown11001(10, 10, 10)
    Unknown11057(500)
    Unknown9017(1)
    StarterRating(2)

@Subroutine
def UltimateLock_Atk2ndODInit():
    MinimumDamagePct(10)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirUntechableTime(60)
    hitstun(60)
    AirPushbackX(7500)
    AirPushbackY(30000)
    Unknown11064(1)
    Unknown11057(400)
    Unknown9178(1)
    WallbounceReboundTime(0)
    Hitstop(1)
    Unknown11001(10, 10, 10)
    Unknown11057(500)
    Unknown9017(1)
    StarterRating(2)

@State
def UltimateLock_Atk2ndLv1():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(12000)
        teleportRelativeX(850000)
        Unknown1007(140000)
        callSubroutine('UltimateLock_Atk2ndInit')

        def upon_32():
            callSubroutine('UltimateLock_Atk2ndODInit')
            MinimumDamagePct(8)
        AttackLevel_(2)
        Damage(1250)
        MinimumDamagePct(8)
        if SLOT_137:
            Unknown10000(80)
        DisableAttackRestOfMove()
        Unknown3038(1)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash_SS', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash2_SS', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash3_SS', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash_SS', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash2_SS', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()

@State
def Eff_432_mgSlash_SS():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff432_slash00', '')
        GFX_2('phef432_aura')
        Unknown2054(1)
        Unknown1096(1000)
        teleportRelativeX(-1100000)
        Unknown1010(0, 100000)
    sprite('null', 10)
    ScreenShake(0, 5000)
    sprite('null', 6)
    physicsXImpulse(60000)
    sprite('null', 2)
    GFX_1('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash2_SS():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        GFX_2('phef432_aura')
        Unknown2054(1)
        Unknown1096(1000)
        teleportRelativeX(-900000)
        Unknown1007(150000)
        Unknown1010(0, 100000)
        Unknown1011(-50000, 50000)
    sprite('null', 10)
    ScreenShake(0, 5000)
    sprite('null', 6)
    physicsXImpulse(60000)
    sprite('null', 2)
    GFX_1('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash3_SS():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        Unknown2054(1)
        Unknown1096(1000)
        teleportRelativeX(-900000)
        Unknown1007(-100000)
        Unknown1010(0, 100000)
        Unknown1011(-50000, 50000)
    sprite('null', 10)
    ScreenShake(0, 5000)
    sprite('null', 6)
    physicsXImpulse(60000)
    sprite('null', 2)
    GFX_1('phef432_hinoko00', -1)

@State
def UltimateLock_Atk2ndLv2():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(12000)
        teleportRelativeX(850000)
        Unknown1007(140000)
        callSubroutine('UltimateLock_Atk2ndInit')

        def upon_32():
            callSubroutine('UltimateLock_Atk2ndODInit')
        AttackLevel_(3)
        Damage(1050)
        if SLOT_137:
            Unknown10000(80)
        DisableAttackRestOfMove()
        Unknown3038(1)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash_S', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 5)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash2_S', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 5)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash3_S', -1)
    SFX_3('phse_07')
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()

@State
def Eff_432_mgSlash_S():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        Unknown2054(1)
        Unknown1096(2000)
        teleportRelativeX(-1100000)
        Unknown1010(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 15000)
    sprite('null', 1)
    GFX_1('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash2_S():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        Unknown2054(1)
        Unknown1096(1700)
        teleportRelativeX(-900000)
        Unknown1007(150000)
        Unknown1010(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 15000)
    sprite('null', 1)
    GFX_1('phef432_hinoko00', -1)

@State
def Eff_432_mgSlash3_S():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        Unknown2054(1)
        Unknown1096(1700)
        teleportRelativeX(-900000)
        Unknown1007(-100000)
        Unknown1010(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 15000)
    sprite('null', 1)
    GFX_1('phef432_hinoko00', -1)

@State
def UltimateLock_Atk2ndLv3():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(12000)
        teleportRelativeX(850000)
        Unknown1007(140000)
        callSubroutine('UltimateLock_Atk2ndInit')

        def upon_32():
            callSubroutine('UltimateLock_Atk2ndODInit')
        AttackLevel_(4)
        Damage(630)
        if SLOT_137:
            Unknown10000(80)
        DisableAttackRestOfMove()
        Unknown3038(1)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash2_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash3_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash2_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash3_S', -1)
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()
    sprite('vr_ph_magictest', 3)
    RefreshMultihit()

@State
def UltimateLock_Atk2ndLv4():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        Unknown1056(45000)
        Unknown1064(12000)
        teleportRelativeX(850000)
        Unknown1007(140000)
        callSubroutine('UltimateLock_Atk2ndInit')

        def upon_32():
            callSubroutine('UltimateLock_Atk2ndODInit')
        AttackLevel_(5)
        Damage(550)
        if SLOT_137:
            Unknown10000(80)
        DisableAttackRestOfMove()
        Unknown3038(1)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash2', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash3', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash2', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 2)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash3', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('null', 8)
    sprite('null', 2)
    GFX_0('Eff_432_mgSlash', -1)
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()
    sprite('vr_ph_magictest', 2)
    RefreshMultihit()

@State
def Eff_432_mgSlash():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        Unknown2054(1)
        Unknown1096(2200)
        teleportRelativeX(-1100000)
        Unknown1010(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 20000)
    sprite('null', 1)
    Unknown4045('706865663433325f68696e6f6b6f303000000000000000000000000000000000ffffffff')

@State
def Eff_432_mgSlash2():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        Unknown2054(1)
        Unknown1096(1700)
        teleportRelativeX(-900000)
        Unknown1007(300000)
        Unknown1073(15000)
        Unknown1010(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 20000)
    sprite('null', 1)
    Unknown4048(15000)
    Unknown4045('706865663433325f68696e6f6b6f303000000000000000000000000000000000ffffffff')

@State
def Eff_432_mgSlash3():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('phef432_aura')
        Unknown4003('pheff432_slash00', '')
        Unknown2054(1)
        Unknown1096(1700)
        teleportRelativeX(-900000)
        Unknown1007(-300000)
        Unknown1073(-15000)
        Unknown1010(0, 50000)
    sprite('null', 17)
    ScreenShake(0, 20000)
    sprite('null', 1)
    Unknown4048(15000)
    Unknown4045('706865663433325f68696e6f6b6f303000000000000000000000000000000000ffffffff')

@State
def UltimateLock_AtkODAdd():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        Unknown1096(20000)
        AttackLevel_(5)
        Damage(250)
        Unknown9001(4)
        MinimumDamagePct(20)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(25000)
        AirUntechableTime(120)
        Hitstop(1)
        Unknown11001(25, 25, 25)
        Unknown11092(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11108('03000000')
        if SLOT_137:
            Unknown10000(80)
        Unknown3038(1)
    sprite('vr_ph_magictest', 1)
    Unknown1086(22)
    teleportRelativeY(0)
    GFX_0('Eff_BGRmato', -1)
    ScreenShake(0, 20000)
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 1)
    RefreshMultihit()
    sprite('vr_ph_magictest', 10)
    StartMultihit()
    ExitState()

@State
def UltimateChargeATK():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        AttackLevel_(5)
        ProjectileDurabilityLvl(2)
        Damage(1500)
        AttackP2(84)
        AirUntechableTime(60)
        AirPushbackX(500)
        AirPushbackY(41000)
        MinimumDamagePct(30)
        GroundedHitstunAnimation(10)
        AttackP1(70)
        Unknown9017(1)
        StarterRating(0)
        Unknown11001(0, -12, -12)
        if SLOT_31:
            Damage(2000)
        Unknown1056(11000)
        Unknown1064(11000)
        teleportRelativeX(150000)
        Unknown1007(100000)
        Unknown3038(1)
    sprite('vr_ph_magictest', 10)
    RefreshMultihit()

@State
def UltimateChargeODATK():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4011(3)
        AttackLevel_(5)
        ProjectileDurabilityLvl(2)
        Damage(1500)
        AttackP2(84)
        AirUntechableTime(60)
        AirPushbackX(500)
        AirPushbackY(41000)
        MinimumDamagePct(30)
        GroundedHitstunAnimation(10)
        AttackP1(70)
        Unknown9017(1)
        StarterRating(0)
        Unknown11001(0, -12, -12)
        Unknown9001(4)
        if SLOT_31:
            Damage(2000)
        Unknown1056(11000)
        Unknown1064(11000)
        teleportRelativeX(150000)
        Unknown1007(100000)
        Unknown3038(1)

        def upon_12():
            clearUponHandler(12)
            Unknown21012('UltimateChargeOD', 32)
    sprite('vr_ph_magictest', 10)
    RefreshMultihit()

@State
def UltimateChargeODAddAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        ProjectileDurabilityLvl(2)
        Damage(500)
        AttackP2(96)
        Unknown9001(4)
        AirUntechableTime(60)
        AirPushbackX(25000)
        AirPushbackY(38000)
        MinimumDamagePct(10)
        GroundedHitstunAnimation(9)
        AttackP1(70)
        Unknown9017(1)
        Unknown11108('03000000')
        StarterRating(2)
        Unknown1056(11000)
        Unknown1064(11000)
        Unknown3038(1)
    sprite('null', 17)
    sprite('vr_ph_magictest', 3)
    Unknown1086(22)
    teleportRelativeX(50000)
    Unknown2006()
    GFX_0('UltimateChargeODAddAtk_Bomb', -1)
    RefreshMultihit()
    sprite('null', 5)
    sprite('vr_ph_magictest', 3)
    Unknown1086(22)
    teleportRelativeX(50000)
    Unknown2006()
    GFX_0('UltimateChargeODAddAtk_Bomb', -1)
    RefreshMultihit()
    sprite('null', 3)
    sprite('vr_ph_magictest', 3)
    Unknown1086(22)
    teleportRelativeX(80000)
    Unknown2006()
    GFX_0('UltimateChargeODAddAtk_Bomb', -1)
    RefreshMultihit()
    AirHitstunAnimation(18)
    AirPushbackX(500)
    sprite('null', 30)

@State
def UltimateChargeODAddAtk_Bomb():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown4011(3)
        Unknown21010(1)
        Unknown1096(800)
    sprite('vr_ph400_04', 2)
    sprite('vr_ph400_05', 3)
    Unknown1007(200000)
    ScreenShake(10000, 10000)
    Unknown1099(15)
    GFX_0('pheff_400sub2', 1)
    Unknown36(1)
    Unknown21010(1)
    Unknown1077(-40000, 40000)
    Unknown35()
    GFX_1('phef_400_bom', 1)
    GFX_1('phef_400_blm', 1)
    sprite('vr_ph400_07', 2)
    sprite('vr_ph400_08', 2)
    GFX_1('phef321_shock2', -1)
    sprite('vr_ph400_09', 2)
    sprite('vr_ph400_06', 3)
    GFX_0('ph320BombEff_Circle', -1)
    Unknown36(1)
    Unknown21010(1)
    Unknown1077(20000, 30000)
    Unknown1097(-600)
    Unknown35()
    GFX_0('phEff400_corebom', 0)
    Unknown3004(-51)

@State
def Eff_431_obi():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4003('pheff431_obi00', '')
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown1096(2700)
        Unknown1007(-10000)
        teleportRelativeX(-38000)
    sprite('null', 6)
    Unknown4003('pheff431_obi00', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi01', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi02', '')
    sprite('null', 8)
    Unknown4003('pheff431_obi03', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi04', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi05', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi06', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi07', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi08', '')
    sprite('null', 6)
    Unknown4003('pheff431_obi09', '')
    Unknown3004(-18)
    sprite('null', 6)
    Unknown4003('pheff431_obi10', '')

@State
def Eff_431_mc():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4003('pheff431_mc00', '')
        Unknown3001(160)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown1096(1500)
        Unknown1007(250000)
        teleportRelativeX(-38000)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 5)
    Unknown1099(150)
    Unknown3004(-26)
    physicsXImpulse(42500)

@State
def Eff_431_mc_sub1():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff431_mc01', '')
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown1096(3000)
        Unknown1007(250000)
        teleportRelativeX(-38000)
        sendToLabelUpon(32, 0)
    sprite('null', 20)
    Unknown3001(0)
    Unknown3004(10)
    sprite('null', 32767)
    Unknown3004(0)
    label(0)
    sprite('null', 5)
    Unknown3004(-26)
    Unknown1099(-200)
    physicsXImpulse(42500)

@State
def Eff_431_BomBall():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4003('pheff431_tameball00', '')
        GFX_2('pheff431_tameball')
        Unknown4010(2)
        Unknown1007(280000)
        teleportRelativeX(100000)
        Unknown1056(1400)
        Unknown1064(1200)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
    sprite('null', 10)
    Unknown3001(0)
    Unknown1099(-75)
    Unknown3004(26)
    label(0)
    sprite('null', 5)
    physicsXImpulse(10000)
    Unknown1099(5)
    sprite('null', 32767)
    physicsXImpulse(0)
    label(1)
    sprite('null', 5)
    physicsXImpulse(-5000)
    Unknown1099(10)
    sprite('null', 32767)
    physicsXImpulse(0)
    label(2)
    sprite('null', 1)
    teleportRelativeX(22500)
    Unknown1007(-10000)
    Unknown1057(200)
    Unknown1065(300)
    sprite('null', 1)
    Unknown1057(200)
    Unknown1065(300)
    teleportRelativeX(10000)
    Unknown1007(-10000)
    sprite('null', 1)
    Unknown1057(200)
    Unknown1065(300)
    teleportRelativeX(10000)
    Unknown1007(-10000)

@State
def Eff_431_bomb():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff431_bomb00', '')
        GFX_2('phef431_blm')
        Unknown4010(2)
        Unknown1007(200000)
        teleportRelativeX(100000)
        Unknown1096(600)
    sprite('null', 2)
    ScreenShake(20000, 20000)
    sprite('null', 2)
    Unknown1097(200)
    Unknown1007(25000)
    sprite('null', 2)
    Unknown1007(25000)
    sprite('null', 1)
    GFX_0('ph320BombEff_Circle', -1)
    GFX_0('Eff_431_bombEnd', -1)
    Unknown1097(100)
    Unknown1007(25000)
    Unknown3004(-51)
    GFX_1('phef_400_bom', -1)
    GFX_1('phef_400_blm', -1)
    sprite('null', 10)
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    Unknown1007(-105000)
    Unknown1097(900)
    Unknown35()
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    Unknown1007(-205000)
    teleportRelativeX(200000)
    Unknown1097(550)
    Unknown1073(20000)
    Unknown35()
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    Unknown1007(-205000)
    teleportRelativeX(-200000)
    Unknown1097(550)
    Unknown1073(-20000)
    Unknown35()

@State
def Eff_431_bombEnd():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff431_bomb01', '')
        Unknown2054(1)
        Unknown1096(250)
        Unknown1007(-260000)
    sprite('null', 14)
    GFX_1('phef_402_end_g', -1)
    sprite('null', 9)
    GFX_1('pheff431_gsmoke_pos', -1)
    Unknown3004(-26)

@State
def AstralHeatAtk():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown1056(8000)
        Unknown1064(10000)
        AttackLevel_(3)
        Damage(0)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        HitstunP2(810)
        Unknown9142(800)
        AirUntechableTime(600)
        Unknown9016(1)
        PushbackX(0)
        Unknown11072(1, 0, 0)
        Unknown11064(1)
        Unknown11056(0)
        Unknown3038(1)

        def upon_12():
            Unknown21007(3, 32)
    sprite('vr_ph_magictest', 8)
    if (SLOT_19 > 450000):
        Unknown1086(22)
        teleportRelativeY(0)
    else:
        teleportRelativeX(500000)
    GFX_1('phef450_ahatk', -1)
    SFX_0('022_magiccircle_c')
    SFX_0('014_electric_ll')

@State
def AstralHeatAtk2nd():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown1056(8000)
        Unknown1064(10000)
        AttackLevel_(5)
        Damage(5000)
        MinimumDamagePct(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(600)
        Unknown9016(1)
        PushbackX(0)
        Unknown11072(1, 0, 0)
        Unknown11056(0)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    Unknown1086(22)
    teleportRelativeY(0)

@State
def AstralHeatLastAtk():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown1056(8000)
        Unknown1064(8000)
        AttackLevel_(5)
        Damage(30000)
        MinimumDamagePct(100)
        Unknown11064(3)
        AirPushbackY(-50000)
        GroundedHitstunAnimation(11)
        Unknown1086(22)
    sprite('vr_ph_magictest', 5)

@State
def Eff_450_EyeBurning():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(2)
    label(0)
    sprite('vr_ph450_00', 3)
    sprite('vr_ph450_01', 3)
    sprite('vr_ph450_02', 3)
    sprite('vr_ph450_03', 3)
    sprite('vr_ph450_04', 3)
    gotoLabel(0)

@State
def Eff_450_Terepo():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4061(2)
    sprite('vr_ph450_10', 6)
    sprite('vr_ph450_11', 3)
    sprite('vr_ph450_12', 3)
    GFX_1('phef450_terepo', -1)
    sprite('vr_ph450_12', 10)
    physicsYImpulse(25000)
    Unknown1067(2400)
    GFX_0('Eff_450_circle', -1)
    GFX_0('Eff_450_circle2', -1)

@State
def Eff_450_circle():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4003('pheff450_AddCircle', '')
        Unknown1007(300000)
    sprite('null', 5)
    Unknown1099(300)
    sprite('null', 5)
    Unknown3004(-51)

@State
def Eff_450_circle2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(1)
        Unknown4003('pheff450_AddCircle', '')
    sprite('null', 5)
    Unknown1099(300)
    Unknown3004(-51)

@State
def AstralHeat_Hibi():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1096(1350)
        sprite('vr_ph450_20', 4)
        Unknown23015(2)
        sprite('vr_ph450_21', 4)
        Unknown23015(0)
        sprite('vr_ph450_22', 4)
        ScreenShake(10000, 10000)
        sprite('vr_ph450_22', 4)
        ScreenShake(10000, 10000)
        GFX_1('phef450_groundray', 0)
        GFX_1('phef450_groundsmoke_R', 5)
        GFX_1('phef450_groundsmoke_L', 6)
        sprite('vr_ph450_22', 4)
        ScreenShake(10000, 10000)
        GFX_1('phef450_groundray', 1)
        GFX_1('phef450_groundray', 2)
        GFX_1('phef450_groundsmoke_R', 5)
        GFX_1('phef450_groundsmoke_L', 6)
        sprite('vr_ph450_22', 10)
        ScreenShake(10000, 10000)
        GFX_1('phef450_groundray', 3)
        GFX_1('phef450_groundray', 4)
        GFX_1('phef450_groundsmoke_R', 5)
        GFX_1('phef450_groundsmoke_L', 6)
        sprite('vr_ph450_22', 4)
        ScreenShake(10000, 10000)
        GFX_1('phef450_groundray', 0)
        GFX_1('phef450_groundsmoke_R', 5)
        GFX_1('phef450_groundsmoke_L', 6)
        sprite('vr_ph450_22', 4)
        ScreenShake(10000, 10000)
        GFX_1('phef450_groundray', 1)
        GFX_1('phef450_groundray', 2)
        GFX_1('phef450_groundsmoke_R', 5)
        GFX_1('phef450_groundsmoke_L', 6)
        sprite('null', 8)
        GFX_1('phef_450_groundstone', -1)

@State
def AstralHeat_Hinokagutsuchi():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown4061(5)
        teleportRelativeX(-25000)
    sprite('null', 40)
    GFX_0('AstralHeat_Hibi', -1)
    SFX_0('019_quake_1')
    sprite('ph450_cutin00', 10)
    ScreenShake(80000, 80000)
    SFX_0('019_quake_1')
    SFX_0('016_explode_2')
    GFX_0('AstralHeatEff_SetugouFire', 0)
    GFX_0('AstralHeatEff_SetugouFire', 1)
    GFX_0('AstralHeatEff_SetugouFire', 2)
    GFX_0('AstralHeatEff_SetugouFire', 3)
    GFX_0('AstralHeatEff_SetugouFire', 4)
    sprite('ph450_cutin01', 6)
    SFX_0('019_quake_0')
    sprite('ph450_cutin02', 6)
    SFX_0('019_quake_0')
    sprite('ph450_cutin03', 6)
    SFX_0('019_quake_1')
    sprite('ph450_cutin04', 6)
    ScreenShake(20000, 20000)
    SFX_0('019_quake_1')
    Unknown36(22)
    Unknown3038(1)
    Unknown35()
    sprite('ph450_cutin05', 6)
    SFX_0('019_quake_1')
    sprite('ph450_cutin06', 6)
    sprite('ph450_cutin07', 6)
    sprite('ph450_cutin08', 6)
    sprite('ph450_cutin09', 6)
    sprite('ph450_cutin10', 6)
    GFX_0('AstralHeatEff_HinoAdd', -1)
    SFX_0('016_explode_1')
    SFX_0('015_blaze_2')
    SFX_0('015_blaze_2')
    sprite('ph450_cutin10', 1)
    GFX_0('AstralHeatEff_DelFire', 0)
    SFX_0('019_quake_1')
    sprite('ph450_cutin10', 1)
    GFX_0('AstralHeatEff_DelFire2', 1)
    sprite('ph450_cutin10', 1)
    GFX_0('AstralHeatEff_DelFire', 2)
    SFX_0('019_quake_0')
    sprite('ph450_cutin10', 1)
    sprite('ph450_cutin10', 1)
    SFX_0('015_blaze_2')
    SFX_0('019_quake_1')
    sprite('ph450_cutin10', 1)
    sprite('ph450_cutin10', 10)
    Unknown3004(-26)
    SFX_0('019_quake_0')
    sprite('ph450_cutin10', 10)
    GFX_0('AstralHeatEff_Rougoku', -1)
    Unknown3038(1)
    Unknown36(22)
    Unknown3038(0)
    Unknown35()
    SFX_0('019_quake_1')
    SFX_0('015_blaze_2')
    sprite('ph450_cutin10', 2)
    GFX_0('AstralHeatEff_DelFire', 0)
    sprite('ph450_cutin10', 2)
    GFX_0('AstralHeatEff_DelFire2', 1)
    sprite('ph450_cutin10', 2)
    GFX_0('AstralHeatEff_DelFire', 2)
    sprite('ph450_cutin10', 2)
    sprite('ph450_cutin10', 2)
    sprite('ph450_cutin10', 2)
    sprite('ph450_cutin10', 20)
    SFX_0('019_quake_1')
    sprite('ph450_cutin10', 2)
    GFX_0('AstralHeatEff_DelFire', 0)
    sprite('ph450_cutin10', 2)
    GFX_0('AstralHeatEff_DelFire2', 1)
    SFX_0('015_blaze_2')
    sprite('ph450_cutin10', 2)
    GFX_0('AstralHeatEff_DelFire', 2)
    sprite('ph450_cutin10', 2)
    sprite('ph450_cutin10', 2)
    SFX_0('019_quake_1')
    sprite('ph450_cutin10', 2)

@State
def AstralHeatEff_SetugouFire():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown4010(2)
        EnableCollision(0)
        ProjectileHitsWall(0)
        Unknown2034(0)
    label(0)
    sprite('null', 25)
    GFX_0('AstralHeatEff_DelFire', -1)
    gotoLabel(0)

@State
def AstralHeatEff_HinoAdd():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown23015(3)
        Unknown21010(1)
        Unknown2054(1)
        Unknown4061(2)
        Unknown3001(0)
    sprite('vrph450_30', 10)
    Unknown3004(26)
    sprite('vrph450_30', 10)
    Unknown3004(0)
    sprite('vrph450_30', 20)
    Unknown3004(-13)

@State
def AstralHeatEff_Rougoku():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('pheff450_ori00', '')
        Unknown1096(825)
        Unknown1007(-3000)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(26)
    sprite('null', 100)

@State
def AstralHeatEff_DelFire():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown4061(2)
        Unknown1096(1600)
        Unknown1099(7)
    sprite('vr_phcmn_00', 4)
    sprite('vr_phcmn_01', 4)
    sprite('vr_phcmn_02', 4)
    sprite('vr_phcmn_03', 4)
    sprite('vr_phcmn_04', 3)
    sprite('vr_phcmn_05', 3)
    GFX_1('phef450_hinoko', 0)
    GFX_1('phef450_hinoko', 1)
    GFX_1('phef450_hinoko', 2)
    sprite('vr_phcmn_06', 3)
    sprite('vr_phcmn_07', 3)

@State
def AstralHeatEff_DelFire2():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown1096(1800)
        Unknown1099(7)
        Unknown1007(-30000)
    sprite('vr_phcmn_00', 3)
    sprite('vr_phcmn_01', 3)
    sprite('vr_phcmn_02', 3)
    sprite('vr_phcmn_03', 3)
    sprite('vr_phcmn_04', 3)
    sprite('vr_phcmn_05', 3)
    GFX_1('phef450_hinoko', 0)
    GFX_1('phef450_hinoko', 1)
    GFX_1('phef450_hinoko', 2)
    sprite('vr_phcmn_06', 3)
    sprite('vr_phcmn_07', 3)

@State
def AstralHeat_Camera():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown20000(1)
        Unknown20003(1)
        Unknown20004(1)
        EnableCollision(0)
        ProjectileHitsWall(0)
        Unknown2034(0)
        Unknown20001(1)
    sprite('null', 7)
    teleportRelativeX(400000)
    Unknown1007(-800000)
    physicsYImpulse(48000)
    sprite('null', 30)
    Unknown20001(0)
    physicsYImpulse(18000)
    GFX_2('phef_shashaend')
    sprite('null', 10)
    physicsYImpulse(3000)
    sprite('null', 5)
    physicsYImpulse(1500)
    sprite('null', 210)
    physicsYImpulse(0)
    sprite('null', 10)
    Unknown20001(1)
    Unknown1007(-1200000)
    Unknown1000(0)
    Unknown36(22)
    Unknown3038(0)
    Unknown35()
    GFX_0('AstralHeatEff_Rougoku2', -1)
    sprite('null', 32767)
    Unknown20001(0)
    Unknown20009(1300)

@State
def AstralHeatEff_Rougoku2():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('pheff450_ori00', '')
        GFX_2('phef450_rou_jizoku')
        Unknown1096(600)
        Unknown1007(300000)
        Unknown3038(1)
    sprite('ph450_cutin06', 160)
    GFX_0('AstralHeatEff_Rougoku2Sub', -1)

@State
def AstralHeatEff_Rougoku2Sub():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1096(700)
        Unknown4010(2)
        Unknown3001(0)
    label(0)
    sprite('ph450_cutin06', 2)
    GFX_0('AstralHeatEff_DelFire', 0)
    Unknown36(1)
    Unknown1097(-450)
    Unknown3001(180)
    Unknown35()
    sprite('ph450_cutin06', 2)
    GFX_0('AstralHeatEff_DelFire2', 1)
    Unknown36(1)
    Unknown1097(-450)
    Unknown3001(180)
    Unknown35()
    sprite('ph450_cutin06', 2)
    GFX_0('AstralHeatEff_DelFire', 2)
    Unknown36(1)
    Unknown1097(-450)
    Unknown3001(180)
    Unknown35()
    sprite('ph450_cutin06', 2)
    GFX_0('AstralHeatEff_DelFire2', 3)
    Unknown36(1)
    Unknown1097(-450)
    Unknown3001(180)
    teleportRelativeX(30000)
    Unknown35()
    sprite('ph450_cutin06', 2)
    GFX_0('AstralHeatEff_DelFire', 4)
    Unknown36(1)
    Unknown1097(-450)
    teleportRelativeX(-30000)
    Unknown3001(180)
    Unknown35()
    sprite('ph450_cutin06', 2)
    GFX_0('AstralHeatEff_DelFire2', 5)
    Unknown36(1)
    Unknown1097(-200)
    Unknown1007(60000)
    Unknown3001(180)
    Unknown35()
    sprite('ph450_cutin06', 13)
    gotoLabel(0)

@State
def AstralHeat_ShakeFallMeteo():

    def upon_IMMEDIATE():
        Unknown2054(1)
        teleportRelativeX(-400000)
        Unknown1007(-800000)
    label(0)
    sprite('null', 5)
    ScreenShake(5000, 5000)
    gotoLabel(0)

@State
def AstralHeatEff_MeteoLast():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('pheff450_meteo01', '')
        Unknown1073(-45000)
        Unknown1056(3500)
        Unknown1064(3500)
        teleportRelativeX(650000)
        Unknown23015(1)
        EnableCollision(0)
        ProjectileHitsWall(0)
        Unknown2034(0)
    sprite('null', 7)
    physicsYImpulse(-40000)
    physicsXImpulse(28000)
    GFX_0('AstralHeat_ShakeFallMeteo', -1)
    sprite('null', 7)
    physicsYImpulse(-30000)
    physicsXImpulse(21000)
    sprite('null', 15)
    physicsYImpulse(-20000)
    physicsXImpulse(14000)
    sprite('null', 6)
    physicsYImpulse(-20000)
    physicsXImpulse(14000)

@State
def Eff_450_Lastbomb():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff450_lastbomb00', '')
        Unknown1096(1200)
        teleportRelativeY(0)
        Unknown1000(0)
        Unknown23015(1)
    sprite('null', 2)
    sprite('null', 2)
    Unknown1097(200)
    Unknown1007(25000)
    sprite('null', 2)
    Unknown1007(25000)
    sprite('null', 5)
    GFX_0('Eff_450_LastbombEnd', -1)
    Unknown1097(100)
    Unknown1007(25000)
    Unknown3004(-51)

@State
def Eff_450_LastbombEnd():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff450_lastbomb01', '')
        Unknown2054(1)
        Unknown1096(500)
        Unknown1007(-300000)
        Unknown23015(1)
    sprite('null', 4)
    sprite('null', 10)
    GFX_1('phef_lastbomb_end', -1)
    sprite('null', 9)
    Unknown3004(-26)

@State
def Eff_450_Burning():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff450_winbg', '')
        Unknown2054(1)
        teleportRelativeX(600000)
        Unknown1096(800)
        GFX_2('pheff450_winbg')
    label(0)
    sprite('null', 10)
    SFX_0('019_quake_0')
    sprite('null', 10)
    SFX_0('019_quake_1')
    loopRest()
    gotoLabel(0)

@State
def AstralHeatEff_Meteo():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('pheff450_meteo00', '')
        physicsYImpulse(-48000)
        physicsXImpulse(48000)
        Unknown1073(-45000)
        sendToLabelUpon(2, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    GFX_1('phef_bgr_atk_end', -1)
    Unknown3001(0)
    physicsYImpulse(0)
    physicsXImpulse(0)
    GFX_0('AstralHeatEff_MeteoMag', -1)
    ScreenShake(0, 10000)

@State
def AstralHeatEff_MeteoMag():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown1096(1000)
        Unknown4010(2)
        Unknown4013(2)
        Unknown1062(-300, 0)
    sprite('null', 10)
    GFX_0('Eff_450_bomb', -1)
    Unknown3001(0)
    ScreenShake(10000, 10000)
    sprite('null', 10)
    Unknown3001(255)
    Unknown1067(75)
    label(0)
    sprite('null', 2)
    Unknown1067(0)
    Unknown1057(-300)
    teleportRelativeX(10000)
    sprite('null', 2)
    Unknown1057(300)
    teleportRelativeX(-10000)
    gotoLabel(0)

@State
def Eff_450_bomb():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4003('pheff431_bomb00', '')
        GFX_2('phef431_blm')
        Unknown1007(200000)
        teleportRelativeX(100000)
        Unknown1096(600)
    sprite('null', 2)
    sprite('null', 2)
    Unknown1097(200)
    Unknown1007(25000)
    sprite('null', 2)
    Unknown1007(25000)
    sprite('null', 5)
    GFX_0('Eff_450_bombEnd', -1)
    Unknown1097(100)
    Unknown1007(25000)
    Unknown3004(-51)
    GFX_1('phef_400_bom', -1)
    GFX_1('phef_400_blm', -1)

@State
def Eff_450_bombEnd():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff431_bomb01', '')
        Unknown2054(1)
        Unknown1096(250)
        Unknown1007(-250000)
    sprite('null', 14)
    GFX_1('phef_402_end_g', -1)
    sprite('null', 9)
    GFX_1('pheff431_gsmoke_pos', -1)
    Unknown3004(-26)

@State
def AstralHeatEff_MeteoMato():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1000(-800000)
        teleportRelativeY(0)
        Unknown1007(500000)
        sendToLabelUpon(2, 0)
    sprite('null', 8)
    GFX_0('AstralHeatEff_Meteo', -1)
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    sprite('null', 8)
    GFX_0('AstralHeatEff_Meteo', -1)
    Unknown36(1)
    teleportRelativeX(1000000)
    Unknown1097(400)
    Unknown35()
    SFX_0('016_explode_2')
    SFX_0('213_bound_1')
    sprite('null', 8)
    GFX_0('AstralHeatEff_Meteo', -1)
    Unknown36(1)
    teleportRelativeX(500000)
    Unknown1097(500)
    Unknown35()
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    sprite('null', 8)
    GFX_0('AstralHeatEff_Meteo', -1)
    Unknown36(1)
    teleportRelativeX(-1000000)
    Unknown1097(600)
    Unknown35()
    SFX_0('016_explode_2')
    SFX_0('213_bound_1')
    sprite('null', 6)
    GFX_0('AstralHeatEff_Meteo', -1)
    Unknown36(1)
    teleportRelativeX(-500000)
    Unknown1097(700)
    Unknown35()
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    sprite('null', 6)
    GFX_0('AstralHeatEff_Meteo', -1)
    Unknown36(1)
    teleportRelativeX(750000)
    Unknown1097(800)
    Unknown35()
    SFX_0('016_explode_2')
    SFX_0('213_bound_0')
    sprite('null', 4)
    GFX_0('AstralHeatEff_Meteo', -1)
    Unknown36(1)
    teleportRelativeX(250000)
    Unknown1097(900)
    Unknown35()
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    sprite('null', 15)
    GFX_0('AstralHeatEff_Meteo', -1)
    Unknown36(1)
    teleportRelativeX(-250000)
    Unknown1097(1000)
    Unknown35()
    SFX_0('016_explode_2')
    SFX_0('213_bound_0')
    sprite('null', 15)
    GFX_0('AstralHeatEff_MeteoLast', -1)
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    sprite('null', 15)
    sprite('null', 10)
    GFX_0('Eff_450_Lastbomb', -1)
    Unknown26('AstralHeatEff_Meteo')
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    SFX_0('213_bound_1')
    sprite('null', 4)
    GFX_0('Eff_450_Burning', -1)

@State
def phAst_ShaSha00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown4003('pheff450_shasha00', '')
        Unknown4007(2)
        Unknown23015(1)
        Unknown1007(-400000)
    sprite('null', 39)

@State
def Entry_Hinokagutsuchi():

    def upon_IMMEDIATE():
        pass
    sprite('ph601cutin_ex01', 5)

@State
def Entry_HinoEff():

    def upon_IMMEDIATE():
        GFX_2('phef601_root')
        Unknown4010(2)
        sendToLabelUpon(32, 1)
        Unknown2037(0)

        def upon_33():
            clearUponHandler(33)
            SLOT_51 = 1
            Unknown2037(1)
    label(0)
    sprite('null', 16)
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    teleportRelativeX(-350000)
    Unknown35()
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown1007(100000)
    Unknown1097(500)
    Unknown23015(2)
    Unknown35()
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown1007(100000)
    Unknown1097(800)
    Unknown23015(2)
    Unknown35()
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    teleportRelativeX(180000)
    Unknown1007(25000)
    Unknown1097(600)
    Unknown35()
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    teleportRelativeX(-200000)
    Unknown1097(600)
    Unknown35()
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    Unknown1057(300)
    Unknown35()
    if SLOT_2:
        SFX_0('019_quake_1')
    gotoLabel(0)
    label(1)
    sprite('null', 15)
    GFX_0('Entry_FireEnd', -1)
    Unknown3004(25)

@State
def Entry_Fire():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown1096(1000)
        Unknown1067(15)
        Unknown2054(1)
        Unknown21010(1)
        Unknown1010(-25000, 25000)
        Unknown1007(-50000)
    sprite('vr_phcmn_00', 3)
    sprite('vr_phcmn_01', 3)
    sprite('vr_phcmn_02', 3)
    sprite('vr_phcmn_03', 3)
    sprite('vr_phcmn_04', 3)
    sprite('vr_phcmn_05', 3)
    Unknown3004(-26)
    GFX_1('phef450_hinoko', 2)
    sprite('vr_phcmn_06', 3)
    sprite('vr_phcmn_07', 3)

@State
def Entry_FireEnd():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown3033()
        Unknown4003('pheff601_fire00', '')
        Unknown1096(800)
    sprite('null', 2)
    ScreenShake(5000, 5000)
    GFX_1('phef601_endray', -1)
    GFX_0('Entry_FireEndsub_b', -1)
    Unknown36(1)
    Unknown1007(100000)
    Unknown1097(1000)
    Unknown35()
    sprite('null', 2)
    GFX_0('Entry_FireEndsub_a', -1)
    Unknown36(1)
    Unknown1007(100000)
    Unknown1097(-2000)
    Unknown35()
    sprite('null', 2)
    GFX_0('Entry_FireEndsub_a', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    sprite('null', 2)
    GFX_0('Entry_FireEndsub_a', -1)
    Unknown36(1)
    Unknown1007(300000)
    Unknown1097(-2000)
    Unknown35()
    sprite('null', 2)
    GFX_0('Entry_FireEndsub_a', -1)
    Unknown36(1)
    Unknown1007(400000)
    Unknown1097(-1500)
    Unknown35()
    sprite('null', 2)
    GFX_0('Entry_FireEndsub_a', -1)
    Unknown36(1)
    Unknown1007(550000)
    Unknown1097(-1200)
    Unknown35()
    sprite('null', 3)
    GFX_0('Entry_FireEndsub2', -1)

@State
def Entry_FireEndsub_a():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff432_yari01', '')
        Unknown2054(1)
        Unknown1096(3800)
        Unknown1007(10000)
    sprite('null', 5)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown1099(240)
    GFX_0('Entry_FireEndsub_b2', -1)

@State
def Entry_FireEndsub_b():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff432_yari01', '')
        Unknown2054(1)
        Unknown1096(3800)
        Unknown1007(10000)
    sprite('null', 10)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown1099(120)

@State
def Entry_FireEndsub_b2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('pheff_rrr00', '')
        Unknown1096(2500)
        Unknown3001(255)
        Unknown1072(20000)
    sprite('null', 5)
    sprite('null', 10)
    Unknown1099(120)
    Unknown3004(-26)

@State
def Entry_FireEndsub2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4003('pheff432_yari03', '')
        Unknown2054(1)
        Unknown1056(1500)
        Unknown1064(1700)
    sprite('null', 10)
    sprite('null', 4)
    GFX_0('Entry_Fire', -1)
    Unknown36(1)
    Unknown1007(100000)
    Unknown1097(1200)
    Unknown23015(2)
    Unknown35()

@State
def BurstDDEff():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(5)
        GFX_2('phef402_mc3')
        Unknown1086(22)
        Unknown1072(90000)
    sprite('ph402_cutin_a', 2)
    SFX_0('005_swing_grap_2_2')
    sprite('ph402_cutin_b', 1)
    SFX_0('016_explode_2')
    sprite('ph402_cutin_c', 1)
    sprite('ph402_cutin', 3)
    GFX_0('Eff_402Fire', -1)
    Unknown36(1)
    Unknown1072(90000)
    teleportRelativeX(28000)
    Unknown35()
    sprite('ph402_cutin', 15)
    Unknown4010(0)
    Unknown4009(0)
    sprite('ph402_cutin', 2)
    Unknown3004(-26)
    GFX_1('phef402_end_sita', -1)
    GFX_1('phef402_end', 0)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 1)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 2)
    sprite('ph402_cutin', 2)
    GFX_1('phef402_end', 3)

@State
def BurstDDRevEff():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(2400)
        AttackP2(100)
        Unknown9001(4)
        AirPushbackX(-1000)
        AirPushbackY(40000)
        AirUntechableTime(60)
        AirHitstunAnimation(18)
        Hitstop(0)
        Unknown11001(15, 15, 18)
        Unknown11043(0)
        ChipDamagePct(0)
        MinimumDamagePct(10)
        Unknown11069('BurstDDBomb')
        Unknown11108('03000000')
        Unknown11066(1)
        Unknown11084(1)

        def upon_12():
            ScreenShake(50000, 10000)
            SFX_0('025_cleanhit_grap')
            if SLOT_2:
                GFX_0('BurstDDBomb', -1)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(5)
        Unknown3032()
        GFX_2('phef402_mc2')
        Unknown1086(22)
        Unknown1072(-90000)

        def upon_32():
            Unknown11064(1)
            Unknown2037(1)
    sprite('ph402_cutin_aRev', 2)
    sprite('ph402_cutin_bRev', 1)
    sprite('ph402_cutin_cRev', 1)
    sprite('ph402_cutinRev', 3)
    GFX_0('Eff_402Fire', -1)
    Unknown36(1)
    Unknown1072(-90000)
    Unknown1007(-45000)
    teleportRelativeX(-28000)
    Unknown35()
    sprite('ph402_cutinRev', 15)
    Unknown4010(0)
    Unknown4009(0)
    sprite('ph402_cutinRev', 2)
    Unknown3004(-26)
    GFX_1('phef402_end_sita', -1)
    GFX_1('phef402_end', 0)
    sprite('ph402_cutinRev', 2)
    GFX_1('phef402_end', 1)
    sprite('ph402_cutinRev', 2)
    GFX_1('phef402_end', 2)
    sprite('ph402_cutinRev', 2)
    GFX_1('phef402_end', 3)
    if (not SLOT_2):
        Unknown21007(3, 32)

@State
def BurstDDBomb():

    def upon_IMMEDIATE():
        callSubroutine('MagicInit')
        Unknown2011()
        Unknown9001(4)
        Unknown1096(20000)
        AttackLevel_(5)
        Damage(2800)
        AttackP2(100)
        Unknown9017(1)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(25000)
        AirUntechableTime(120)
        Unknown11023(1)
        Unknown11043(0)
        ChipDamagePct(0)
        MinimumDamagePct(10)
        Unknown11069('BurstDDBomb')
        Unknown11108('03000000')
        Unknown11066(1)
        Unknown11084(1)
        Unknown3038(1)
    sprite('null', 20)
    sprite('null', 5)
    GFX_0('BurstDDBomb2', -1)
    Unknown36(1)
    Unknown1097(400)
    Unknown1007(-175000)
    Unknown35()
    sprite('vr_ph_magictest', 3)
    ScreenShake(25000, 100000)
    sprite('null', 5)
    Unknown21007(3, 32)

@State
def BurstDDBomb2():

    def upon_IMMEDIATE():
        Unknown4061(3)
        Unknown4011(3)
        Unknown1096(800)
    sprite('vr_ph400_04', 2)
    Unknown21010(1)
    sprite('vr_ph400_05', 3)
    Unknown1007(200000)
    ScreenShake(10000, 10000)
    Unknown1099(15)
    GFX_0('pheff_400sub2', 1)
    Unknown36(1)
    Unknown1077(-40000, 40000)
    Unknown21010(1)
    Unknown35()
    GFX_1('phef_400_bom', 1)
    GFX_1('phef_400_blm', 1)
    sprite('vr_ph400_07', 2)
    sprite('vr_ph400_08', 2)
    GFX_1('phef321_shock2', -1)
    sprite('vr_ph400_09', 2)
    sprite('vr_ph400_06', 3)
    GFX_0('ph320BombEff_Circle', -1)
    Unknown36(1)
    Unknown21010(1)
    Unknown1077(20000, 30000)
    Unknown1097(-600)
    Unknown35()
    GFX_0('phEff400_corebom', 0)
    Unknown3004(-51)

@State
def BurstDDCamera():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)

        def upon_CLEAR_OR_EXIT():
            Unknown1086(3)
            SLOT_51 = SLOT_19
            SLOT_51 = (SLOT_51 / 4)
            Unknown48(23, 2, 52, 3, 2, 22)
            Unknown48(23, 2, 53, 22, 2, 22)
            if (SLOT_52 < SLOT_53):
                SLOT_22 = (SLOT_22 + SLOT_51)
            elif (SLOT_52 > SLOT_53):
                SLOT_22 = (SLOT_22 - SLOT_51)
            else:
                pass
            SLOT_22 = (SLOT_22 + 200000)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(1)
    label(0)
    sprite('null', 120)
    Unknown20000(1)
    Unknown20003(1)
    label(1)
    sprite('null', 1)
    Unknown20000(0)
    Unknown20003(0)

@State
def ph900Eff():

    def upon_IMMEDIATE():
        Unknown3032()
        EnableCollision(0)
        ProjectileHitsWall(0)
        Unknown2034(0)
        Unknown4010(2)
        Unknown1096(260)
        Unknown4003('pheff001_fire00', '')
        GFX_2('phef001_hinoko')
    sprite('null', 15)
    Unknown3001(0)
    sprite('null', 50)
    Unknown3004(4)
    label(0)
    sprite('null', 25)
    physicsYImpulse(150)
    Unknown3004(0)
    Unknown1099(-2)
    sprite('null', 5)
    Unknown1099(-1)
    physicsYImpulse(75)
    sprite('null', 25)
    physicsYImpulse(-150)
    Unknown1099(2)
    sprite('null', 5)
    Unknown1099(1)
    physicsYImpulse(-75)
    gotoLabel(0)

@State
def ph900Eff2():

    def upon_IMMEDIATE():
        Unknown3032()
        EnableCollision(0)
        ProjectileHitsWall(0)
        Unknown2034(0)
        Unknown4010(2)
        GFX_2('phef432_yuge')
        Unknown1007(-22500)
    sprite('null', 15)
    Unknown3001(0)
    sprite('null', 50)
    Unknown3004(5)
    sprite('null', 32767)

@State
def ph900Eff3():

    def upon_IMMEDIATE():
        Unknown3032()
        EnableCollision(0)
        ProjectileHitsWall(0)
        Unknown2034(0)
        Unknown4010(2)
    sprite('null', 20)
    label(0)
    sprite('null', 22)
    Unknown4049(300)
    Unknown4045('706865663930305f666972653030000000000000000000000000000000000000ffffffff')
    gotoLabel(0)

@State
def EventBGBlack():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 1)
        Unknown4061(3)
        Unknown3032()
        Unknown1056(20000)
        Unknown1064(20000)
        Unknown23032(50)
        Unknown23033(50)
        Unknown23015(15)
        Unknown2019(10000)
    sprite('vr_screen_black', 30)
    Unknown3001(0)
    Unknown3004(3)
    label(0)
    sprite('vr_screen_black', 32767)
    Unknown3001(90)
    Unknown3004(0)
    gotoLabel(0)
    label(1)
    sprite('vr_screen_black', 30)
    Unknown3004(-3)

@State
def Event_ph032FireEff2():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown2054(1)
        Unknown3032()
        Unknown4061(2)
        Unknown3033()
    sprite('vr_ph32_00', 3)
    sprite('vr_ph32_01', 3)
    sprite('vr_ph32_02', 3)
    Unknown3004(-12)
    sprite('vr_ph32_03', 3)
    sprite('vr_ph32_04', 3)
    sprite('vr_ph32_05', 3)
    sprite('vr_ph32_06', 3)
    sprite('vr_ph32_07', 3)

@State
def Event_MidAssault_Atk():

    def upon_IMMEDIATE():
        Unknown1056(6000)
        Unknown1064(15000)
        Unknown1007(80000)
        ProjectileHitsWall(1)
        Unknown1086(22)
        Unknown1007(80000)
        Unknown4010(3)
        Unknown4011(3)
        Unknown3038(1)
        Unknown2003(1)
    sprite('null', 10)
    sprite('null', 4)
    GFX_0('Eff_402', -1)
    SFX_0('016_explode_1')
    sprite('vr_ph_magictest', 5)
    Unknown8003(104, 1, 1)
    ExitState()

@State
def Event_DriveAtk_RRR():

    def upon_IMMEDIATE():
        Unknown1056(6000)
        Unknown1064(15000)
        teleportRelativeX(360000)
        Unknown1007(75000)
        Unknown3038(1)
    sprite('vr_ph_magictest', 3)
    GFX_0('Eff_RRR', -1)

@State
def Event_phef_600_bg():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(3)
        Unknown3032()
        Unknown1056(20000)
        Unknown1064(20000)
        Unknown23032(50)
        Unknown23033(50)
        Unknown23015(15)
        Unknown2019(10000)
    sprite('vr_screen_black', 30)
    Unknown3001(0)
    Unknown3004(3)
    sprite('vr_screen_black', 60)
    Unknown3001(95)
    Unknown3004(0)
    sprite('vr_screen_black', 30)
    Unknown3004(-3)

@State
def Event_phef_600_Fire():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 1)
    GFX_1('phef_600bigen', 100)

@State
def Event_phef_600_Fire2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()
    sprite('phef600_10', 4)
    sprite('phef600_11', 4)
    sprite('phef600_12', 4)

@State
def Event_phef_600_FireWall():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4003('pheff600_firewall', '')
        Unknown4015()
        Unknown3033()
        GFX_2('phef_600ground')
    sprite('null', 6)
    Unknown3001(0)
    Unknown3004(32)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_0')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_1')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_0')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_1')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    SFX_0('019_quake_0')
    sprite('null', 6)
    GFX_1('phef_600fireblow', -1)
    sprite('null', 16)
    Unknown3004(-16)
    GFX_0('Event_phef_600_Fire_End', -1)

@State
def Event_phef_600_Fire_End():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
    sprite('null', 1)
    GFX_1('phef_600fire_end', -1)

@State
def Act3Event_phEff_RRB():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown4007(2)
        Unknown4010(2)
        sendToLabelUpon(32, 10)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 11)
        Unknown1084(1)
    sprite('vr_phrrb_01', 2)
    GFX_0('Act3Event_phEff_RRBSub', -1)
    SFX_3('phse_04')
    SFX_0('019_quake_1')
    physicsXImpulse(-1000)
    physicsYImpulse(1000)
    sprite('vr_phrrb_02', 2)
    sprite('vr_phrrb_03', 2)
    sprite('vr_phrrb_04', 2)
    GFX_2('phef_rrb_jizoku')
    sprite('vr_phrrb_05', 2)
    sprite('vr_phrrb_00', 4)
    label(0)
    sprite('vr_phrrb_00', 6)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(3)
    Unknown3076(1200)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_phrrb_00', 6)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(3)
    Unknown3076(1200)
    SFX_0('019_quake_1')
    ScreenShake(4000, 4000)
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('vr_phrrb_00', 10)
    physicsXImpulse(80000)
    physicsYImpulse(-80000)
    label(11)
    sprite('null', 10)
    Unknown3004(-26)
    loopRest()

@State
def Act3Event_phEff_RRBSub():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4013(2)
        Unknown1072(-45000)
        Unknown1084(1)
    sprite('null', 30)
    GFX_2('phef_rrb_start')
    loopRest()