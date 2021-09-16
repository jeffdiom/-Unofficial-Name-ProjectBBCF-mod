@State
def EMB_HA():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(240000)
        Unknown2054(1)
        IsInvisibility(1)
        Unknown4003('ef_emb_HA.DIG', 'ef_emb_HA_motion_000.mmot')
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
def EMB_HA_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        GFX_OffsetY(240000)
        Unknown2054(1)
        IsInvisibility(1)
        Unknown4003('ef_emb_HA.DIG', 'ef_emb_HA_motion_000.mmot')
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
def EMB_HA_AH():

    def upon_IMMEDIATE():
        Unknown2008()
        GFX_OffsetY(240000)
        Unknown2054(1)
        Unknown4003('ef_emb_HA.DIG', 'ef_emb_HA_motion_000.mmot')
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
def EventRCStand():

    def upon_43():
        if (SLOT_48 == 10):
            enterState('EventRCWarpOut')
    GFX_SetPalette(7)
    label(0)
    sprite('rc000_00', 7)
    sprite('rc000_01', 7)
    sprite('rc000_02', 7)
    sprite('rc000_03', 7)
    sprite('rc000_04', 7)
    sprite('rc000_05', 7)
    sprite('rc000_06', 7)
    sprite('rc000_07', 7)
    sprite('rc000_08', 7)
    gotoLabel(0)

@State
def EventRCWarpIn():
    Unknown3032()
    GFX_SetPalette(7)
    sprite('rc000_00', 7)
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    Unknown3001(0)
    Unknown3004(10)
    sprite('rc000_01', 7)
    sprite('rc000_02', 7)
    sprite('rc000_03', 7)
    sprite('rc000_04', 7)
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('rc000_05', 7)
    sprite('rc000_06', 7)
    sprite('rc000_07', 7)
    sprite('rc000_08', 7)
    Unknown3001(255)
    Unknown3004(0)
    GFX_1('haef_event_lose_end', 0)
    enterState('EventRCStand')

@State
def EventRCWarpOut():
    Unknown3032()
    GFX_SetPalette(7)
    sprite('rc000_00', 7)
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    Unknown3004(-10)
    sprite('rc000_01', 7)
    sprite('rc000_02', 7)
    sprite('rc000_03', 7)
    sprite('rc000_04', 7)
    IsInvisibility(1)
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('rc000_05', 7)
    sprite('rc000_06', 7)
    sprite('rc000_07', 7)
    sprite('rc000_08', 7)
    Unknown3004(0)
    GFX_1('haef_event_lose_end', 103)
    sprite('rc000_08', 32767)

@State
def ha_D():

    def upon_IMMEDIATE():
        GFX_SetPalette(1)
        ProjectileDisapperOnHit(3)
        Unknown4007(3)
    sprite('null', 40)
    Unknown4047(240, 241, 242)
    Unknown23067('haef_D')
    sprite('null', 21)
    Unknown4007(0)

@State
def ha_D_usui():

    def upon_IMMEDIATE():
        GFX_SetPalette(1)
        ProjectileDisapperOnHit(3)
        Unknown4007(3)
    sprite('null', 10)
    Unknown4047(240, 241, 242)
    Unknown23067('haef_D')
    Unknown3001(150)
    Unknown3004(-5)
    sprite('null', 51)
    Unknown4007(0)

@State
def ha_D_no_link_pos():

    def upon_IMMEDIATE():
        GFX_SetPalette(1)
        ProjectileDisapperOnHit(3)
        Unknown4007(3)
    sprite('null', 10)
    Unknown4047(240, 241, 242)
    Unknown23067('haef_D')
    sprite('null', 51)
    Unknown3001(140)
    Unknown3004(-20)
    Unknown4007(0)

@State
def ha_5D():

    def upon_IMMEDIATE():
        GFX_SetPalette(1)
        ProjectileDisapperOnHit(3)
        Unknown4007(3)
        sendToLabelUpon(32, 0)

        def upon_33():
            Unknown4007(0)
    sprite('null', 32767)
    Unknown4047(240, 241, 242)
    Unknown23067('haef_D')
    label(0)
    sprite('null', 10)
    Unknown3005(-20)

@State
def ha_2D():

    def upon_IMMEDIATE():
        GFX_SetPalette(1)
        ProjectileDisapperOnHit(3)
        Unknown4007(3)

        def upon_32():
            Unknown4007(0)
    sprite('null', 8)
    Unknown4047(240, 241, 242)
    Unknown23067('haef_D')
    sprite('null', 20)
    Unknown3005(-15)

@State
def ha_6D():

    def upon_IMMEDIATE():
        GFX_SetPalette(1)
        ProjectileDisapperOnHit(3)
        Unknown4007(3)
        sendToLabelUpon(32, 0)

        def upon_33():
            Unknown4007(0)
    sprite('null', 32767)
    Unknown4047(240, 241, 242)
    Unknown23067('haef_D')
    label(0)
    sprite('null', 7)
    Unknown3001(140)
    Unknown3004(-20)

@State
def ha_202():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4009(3)
        Unknown3033()
        GFX_SetPalette(1)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(243)
        Unknown3041(244)
        Unknown3043(245)
        Unknown3044(1)
        Unknown3001(245)
    sprite('vrhaef202_00', 120)

@State
def ha_232():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4009(3)
        Unknown3033()
        GFX_SetPalette(1)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(243)
        Unknown3041(244)
        Unknown3043(245)
        Unknown3044(1)
        Unknown3001(245)
    sprite('vrhaef232_00', 2)
    sprite('vrhaef232_00', 2)
    Unknown3004(-5)
    Unknown3001(160)
    Unknown4007(0)
    Unknown4010(0)
    sprite('vrhaef232_00', 14)
    Unknown3001(120)

@State
def ha_212():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4009(3)
        Unknown3033()
        GFX_SetPalette(1)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(243)
        Unknown3041(244)
        Unknown3043(245)
        Unknown3044(1)
        Unknown3001(245)
    sprite('vrhaef212_00', 3)
    sprite('vrhaef212_01', 2)
    Unknown3004(-5)
    Unknown3001(160)
    Unknown4007(0)
    Unknown4010(0)
    sprite('vrhaef212_01', 14)
    Unknown3001(120)

@State
def ha_234():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4009(3)
        Unknown3033()
        GFX_SetPalette(1)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(243)
        Unknown3041(244)
        Unknown3043(245)
        Unknown3044(1)
        Unknown3001(245)
    sprite('vrhaef234_00', 3)
    sprite('vrhaef234_01', 16)

@State
def ha_252():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4009(3)
        Unknown3033()
        GFX_SetPalette(1)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(243)
        Unknown3041(244)
        Unknown3043(245)
        Unknown3044(1)
        Unknown3001(245)
    sprite('vrhaef252_00', 2)
    sprite('vrhaef252_01', 2)
    sprite('vrhaef252_02', 2)
    sprite('vrhaef252_03', 3)
    sprite('vrhaef252_04', 16)

@State
def ha_214():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4009(3)
        Unknown3033()
        GFX_SetPalette(1)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(243)
        Unknown3041(244)
        Unknown3043(245)
        Unknown3044(1)
        Unknown3001(245)
    sprite('vrhaef214_00', 2)
    Unknown3004(-5)
    sprite('vrhaef214_00', 2)
    Unknown3001(160)
    Unknown4007(0)
    Unknown4010(0)
    sprite('vrhaef214_00', 16)
    Unknown3001(120)

@State
def ha_260():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4009(3)
        Unknown3033()
        GFX_SetPalette(1)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(243)
        Unknown3041(244)
        Unknown3043(245)
        Unknown3044(1)
        Unknown3001(220)
    sprite('vrhaef260_00', 2)
    Unknown3004(-5)
    sprite('vrhaef260_00', 2)
    Unknown3001(120)
    sprite('vrhaef260_00', 6)
    Unknown3001(80)
    sprite('vrhaef260_00', 6)
    Unknown4007(0)
    Unknown4010(0)

@State
def ha_406():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4009(3)
        Unknown3033()
        GFX_SetPalette(1)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(243)
        Unknown3041(244)
        Unknown3043(245)
        Unknown3044(1)
        Unknown3001(245)
    sprite('vrhaef406_00', 2)
    Unknown3004(-5)
    sprite('vrhaef406_01', 2)
    Unknown3001(160)
    Unknown4007(0)
    Unknown4010(0)
    sprite('vrhaef406_01', 16)
    Unknown3001(120)

@State
def ha_power_circle():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_Scale(0)
        Unknown3001(0)
        Unknown2007()
        Unknown2019(-1000)
        GFX_OffsetY(256000)
    sprite('vrhaef_power_circle', 6)
    Unknown1099(225)
    Unknown3004(43)
    sprite('vrhaef_power_circle', 25)
    Unknown1099(4)
    Unknown3004(-10)

@State
def ha_power_light():

    def upon_IMMEDIATE():
        Unknown3033()
        GFX_Scale(0)
        Unknown3001(0)
        Unknown2007()
        Unknown2019(501)
        GFX_OffsetY(256000)
    sprite('vrhaef_power_light', 6)
    Unknown1099(250)
    Unknown3004(43)
    sprite('vrhaef_power_light', 25)
    Unknown1099(8)
    Unknown3004(-10)

@State
def ha_power_bluelight():

    def upon_IMMEDIATE():
        Unknown3033()
        GFX_Scale(0)
        Unknown3001(0)
        Unknown2007()
        Unknown2019(-999)
        GFX_OffsetY(256000)
    sprite('vrhaef_power_bluelight', 6)
    Unknown1099(250)
    Unknown3004(43)
    sprite('vrhaef_power_bluelight', 25)
    Unknown1099(5)
    Unknown3004(-10)

@State
def ha_power_1():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_Scale(0)
        Unknown3001(0)
        Unknown2007()
        Unknown2019(-1000)
        GFX_OffsetY(256000)
    sprite('vrhaef_power_1', 6)
    Unknown1099(167)
    Unknown3004(43)
    sprite('vrhaef_power_1', 15)
    Unknown1099(4)
    Unknown3004(0)
    sprite('vrhaef_power_1', 10)
    Unknown3004(-26)

@State
def ha_power_2():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_Scale(0)
        Unknown3001(0)
        Unknown2007()
        Unknown2019(-1000)
        GFX_OffsetY(256000)
    sprite('vrhaef_power_2', 6)
    Unknown1099(167)
    Unknown3004(43)
    sprite('vrhaef_power_2', 15)
    Unknown1099(4)
    Unknown3004(0)
    sprite('vrhaef_power_2', 10)
    Unknown3004(-26)

@State
def ha_power_3():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_Scale(0)
        Unknown3001(0)
        Unknown2007()
        Unknown2019(-1000)
        GFX_OffsetY(256000)
    sprite('vrhaef_power_3', 6)
    Unknown1099(167)
    Unknown3004(43)
    sprite('vrhaef_power_3', 15)
    Unknown1099(4)
    Unknown3004(0)
    sprite('vrhaef_power_3', 10)
    Unknown3004(-26)

@State
def GuardCrash():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4009(3)
        Unknown3033()
        GFX_SetPalette(0)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(36)
        Unknown3041(37)
        Unknown3043(38)
        Unknown3044(1)
        Unknown3001(247)
    sprite('vrhaef408_00', 2)
    sprite('vrhaef408_01', 120)

@State
def ha_402a():

    def upon_IMMEDIATE():
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4009(3)
        Unknown3053(1)
        Unknown3033()
        GFX_SetPalette(1)
        Unknown3040(2)
        Unknown3042(243)
        Unknown3041(244)
        Unknown3043(245)
        Unknown3044(1)
        Unknown3001(245)
    sprite('vrhaef402_00', 16)
    GFX_OffsetX(-96000)

@State
def ha_402b():

    def upon_IMMEDIATE():
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4009(3)
        Unknown3053(1)
        GFX_SetPalette(1)
        Unknown3033()
        Unknown3040(2)
        Unknown3042(243)
        Unknown3041(244)
        Unknown3043(245)
        Unknown3044(1)
        Unknown3001(245)
    sprite('vrhaef402_10', 16)
    GFX_OffsetX(-128000)

@State
def ha_409():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)

        def upon_32():
            Unknown4007(0)
    sprite('null', 8)
    GFX_SetPalette(1)
    Unknown4047(240, 241, 242)
    Unknown23067('haef_D')
    sprite('null', 20)
    Unknown3005(-15)

@State
def ha_409_dash():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
    label(0)
    sprite('null', 5)
    GFX_1('haef_409dash', -1)
    gotoLabel(0)

@State
def ha_404():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        ProjectileDisapperOnHit(3)
        Unknown4009(3)
        Unknown3053(1)
        GFX_SetPalette(1)
        Unknown3033()
        Unknown3040(2)
        Unknown3042(243)
        Unknown3041(244)
        Unknown3043(245)
        Unknown3044(1)
        Unknown3001(245)
    sprite('vrhaef404_00', 3)
    sprite('vrhaef404_01', 16)

@State
def haef410_kick():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3032()
        GFX_SetPalette(1)
        Unknown3053(1)
        Unknown3040(1)
        Unknown3041(32)
        Unknown3042(246)
        Unknown3043(246)
        Unknown3044(2147483948)
        GFX_OffsetX(96000)
        GFX_OffsetY(32000)
    sprite('vrhaef410_00', 32)
    GFX_1('haef_kick_splash', 0)
    PFX_Scale(875)
    PFX('haef_kick_drop', 1)
    GFX_0('haef410_kick_blm', -1)

@State
def haef410_kick_blm():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3032()
    sprite('vrhaef410_01', 12)
    sprite('vrhaef410_01', 20)
    Unknown3004(-12)

@State
def haef410_kick2():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3053(1)
        Unknown3032()
        GFX_SetPalette(1)
        Unknown3040(1)
        Unknown3041(16)
        Unknown3042(246)
        Unknown3043(246)
        Unknown3044(2147483948)
        GFX_OffsetX(50000)
        GFX_OffsetY(44000)
    sprite('vrhaef410_10', 16)
    GFX_1('haef_kick_splash', 0)
    PFX_Scale(875)
    PFX('haef_kick_drop', 1)
    GFX_0('haef410_kick2_blm', -1)

@State
def haef410_kick2_blm():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown4006(2)
        Unknown4013(2)
        Unknown3032()
    sprite('vrhaef410_11', 1)
    sprite('vrhaef410_11', 15)
    Unknown3004(-17)

@State
def ha_kick():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3053(1)
        Unknown3032()
        GFX_SetPalette(1)
        Unknown3040(1)
        Unknown3041(16)
        Unknown3042(246)
        Unknown3043(246)
        Unknown3044(2147483898)
        GFX_OffsetX(50000)
        GFX_OffsetY(50000)
    sprite('vrhaef401_00', 16)
    GFX_1('haef_kick_splash', 0)

@State
def ha_kick_b():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3032()
        GFX_OffsetX(50000)
        GFX_OffsetY(50000)
    sprite('vrhaef401_01', 16)
    Unknown3004(-16)

@State
def ha_kick2():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3053(1)
        Unknown3032()
        GFX_SetPalette(1)
        Unknown3040(1)
        Unknown3041(20)
        Unknown3042(246)
        Unknown3043(246)
        Unknown3044(2147483898)
        GFX_OffsetX(50000)
        GFX_OffsetY(50000)
    sprite('vrhaef401_10', 18)

@State
def ha_kick2b():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3032()
        GFX_OffsetX(50000)
        GFX_OffsetY(50000)
    sprite('vrhaef401_11', 20)
    Unknown3004(-13)

@State
def ha_kick3():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3053(1)
        GFX_SetPalette(1)
        Unknown3032()
        Unknown3040(1)
        Unknown3041(16)
        Unknown3042(246)
        Unknown3043(246)
        Unknown3044(2147483898)
        GFX_OffsetX(50000)
        GFX_OffsetY(50000)
    sprite('vrhaef401_20', 16)

@State
def ha_kick3b():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3032()
        GFX_OffsetX(50000)
        GFX_OffsetY(50000)
    sprite('vrhaef401_21', 16)
    Unknown3004(-16)

@State
def ha_kick4():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3053(1)
        Unknown3032()
        GFX_SetPalette(1)
        Unknown3040(1)
        Unknown3041(16)
        Unknown3042(246)
        Unknown3043(246)
        Unknown3044(2147483898)
        GFX_OffsetX(50000)
        GFX_OffsetY(50000)
    sprite('vrhaef401_30', 16)
    GFX_1('haef_kick_splash', 0)

@State
def ha_kick4b():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3032()
        GFX_OffsetX(50000)
        GFX_OffsetY(50000)
    sprite('vrhaef401_31', 16)
    Unknown3004(-16)

@State
def ha_FastEnma():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3053(1)
        Unknown3032()
        GFX_SetPalette(1)
        Unknown3040(1)
        Unknown3041(16)
        Unknown3042(246)
        Unknown3043(246)
        Unknown3044(2147483898)
        GFX_Scale(1050)
        Unknown3032()
    sprite('vrhaef403_00', 3)
    GFX_0('ha_FastEnmab', -1)
    sprite('vrhaef403_10', 5)
    GFX_1('haef_kick_drop', 1)
    GFX_1('haef_kick_drop', 2)
    sprite('vrhaef403_10', 5)
    Unknown3004(-26)

@State
def ha_FastEnmab():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3032()
        GFX_Scale(1050)
    sprite('vrhaef403_01', 3)
    sprite('vrhaef403_11', 10)
    Unknown3004(-26)

@State
def ha_air_kick():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3053(1)
        Unknown3032()
        GFX_SetPalette(1)
        Unknown3040(1)
        Unknown3041(16)
        Unknown3042(246)
        Unknown3043(246)
        Unknown3044(2147483898)
        GFX_OffsetY(150000)
    sprite('vrhaef405_00', 16)
    GFX_1('haef_kick_splash', 0)

@State
def ha_air_kick_b():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3032()
        GFX_OffsetY(150000)
    sprite('vrhaef405_01', 16)
    Unknown3004(-16)

@State
def ha_407():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(950)
        AttackP1(70)
        AttackP2(92)
        SameMoveProration(-1)
        Hitstop(9)
        Unknown11001(3, 3, 8)
        AirPushbackX(0)
        AirPushbackY(-45000)
        YImpluseBeforeWallbounce(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(40)
        CounterHitAirPushbackY(-50000)
        EnableCounterHitGroundBounce(1)
        Unknown9120(50)
        Unknown23078(1)
        GroundUntechableTime(1)
        GroundUntechableTimeCTonly(-1)
        Unknown11065(1)
        if SLOT_110:
            Unknown23181(0)
        SameMoveProration(1)
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3053(1)
        Unknown3032()
        GFX_SetPalette(1)
        Unknown3040(1)
        Unknown3041(16)
        Unknown3042(246)
        Unknown3043(246)
        Unknown3044(2147483898)
        GFX_OffsetX(-50000)
        GFX_OffsetY(4294867296)

        def upon_12():
            HeatChange(1250)

        def upon_60():
            HeatChange(3750)

        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrhaef407_00', 4)
    GFX_1('haef_kick_splash', 1)
    GFX_1('haef_kick_splash', 0)
    sprite('vrhaef407_00', 12)
    StartMultihit()

@State
def ha_407_b():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3032()
        GFX_OffsetX(-50000)
        GFX_OffsetY(4294867296)
    sprite('vrhaef407_01', 16)
    Unknown3004(-16)

@State
def ha_407_hasei():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        AttackP2(92)
        SameMoveProration(-1)
        Hitstop(7)
        Unknown11001(5, 5, 8)
        AirPushbackX(0)
        AirPushbackY(-50000)
        YImpluseBeforeWallbounce(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        EnableGroundBounce(1)
        GroundbounceHeight(55)
        FatalCounter(1)
        Unknown23078(1)
        if SLOT_110:
            Unknown23181(0)
        if SLOT_80:
            AirUntechableTime(60)
            EnableGroundBounce(1)
            GroundbounceHeight(55)

            def upon_12():
                SLOT_4 = (SLOT_4 + 1)
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3053(1)
        Unknown3032()
        GFX_SetPalette(1)
        Unknown3040(1)
        Unknown3041(16)
        Unknown3042(246)
        Unknown3043(246)
        Unknown3044(2147483898)
        GFX_OffsetX(-50000)
        GFX_OffsetY(4294867296)
    sprite('vrhaef407_00', 4)
    GFX_1('haef_kick_splash', 1)
    GFX_1('haef_kick_splash', 0)
    sprite('vrhaef407_00', 12)
    StartMultihit()

@State
def ha_407_b_hasei():

    def upon_IMMEDIATE():
        Unknown4009(3)
        ProjectileDisapperOnHit(3)
        Unknown3032()
        GFX_OffsetX(-50000)
        GFX_OffsetY(4294867296)
    sprite('vrhaef407_01', 16)
    Unknown3004(-16)

@State
def ShotDelete():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(900)
        AirUntechableTime(40)
        GroundedHitstunAnimation(9)
        AttackP1(85)
        GFX_2('haef_shotkiller')
        Unknown2037(90)

        def upon_3():
            Unknown2038(-1)
            if (SLOT_2 < 0):
                Unknown23090(23)

        def upon_42():
            Unknown2037(90)

        def upon_11():
            Unknown23090(23)

        def upon_53():
            Unknown22006(0)
            Unknown23090(23)

        def upon_39():
            Unknown23090(23)
        FireBall(1, 1, 1, 1, 0, 0, 0, 0)

        def upon_54():
            sendToLabel(1)
        GuardPoint_(1)
        Unknown22022(0)
        Unknown22032(1)
        Unknown23142(1)
        Unknown11084(1)
        SameMoveProration(1)
    sprite('vr_white_huuma_atk', 1)
    RefreshMultihit()
    GFX_Scale(700)
    Unknown1099(50)
    GFX_0('ShotDeleteMoji', -1)
    GFX_0('ShotDeleteMagicCircle', -1)
    GFX_0('ShotDeleteColorCircle', -1)
    sprite('vr_white_huuma_atk', 1)
    RefreshMultihit()
    sprite('vr_white_huuma_atk', 1)
    RefreshMultihit()
    sprite('vr_white_huuma_atk', 1)
    RefreshMultihit()
    sprite('vr_white_huuma_atk', 1)
    RefreshMultihit()
    sprite('vr_white_huuma_atk', 1)
    RefreshMultihit()
    sprite('vr_white_huuma_atk', 1)
    Unknown1099(0)
    RefreshMultihit()
    loopRest()
    label(0)
    sprite('vr_white_huuma_atk', 1)
    RefreshMultihit()
    sprite('vr_white_huuma_atk', 30)
    RefreshMultihit()
    SFX_3('hase_25')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown1099(-100)
    PFX('haef_shotkiller_del', -1)

@State
def ShotDeleteMoji():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4010(2)
        GFX_2('haef_shotkiller_m')
        Unknown2007()
    sprite('null', 32767)
    Unknown1074(1000)

@State
def ShotDeleteMagicCircle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4010(2)
        GFX_SetPalette(1)
        Unknown4047(208, 208, 208)
        Unknown23067('haef_shotkiller_mc')
    sprite('null', 32767)
    Unknown1074(500)

@State
def ShotDeleteColorCircle():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown4010(2)
        GFX_SetPalette(1)
        Unknown3033()
        Unknown21004(239)
    sprite('vrhaef_shotkiller', 32767)
    Unknown1074(1000)

@State
def ha_DD_1_aura():

    def upon_IMMEDIATE():
        Unknown4010(3)
    sprite('null', 1)
    Unknown4051(0)
    PFX('haef_DD_1', 0)

@State
def ha_DD_1_shot():

    def upon_IMMEDIATE():
        Unknown2011()
        SlashFX(1)
        AttackLevel_(4)
        ProjectileDurabilityLvl(3)
        HeatGainMultiplier(0)
        Damage(2500)
        AttackP2(80)
        AirPushbackX(20000)
        AirUntechableTime(50)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        StarterRating(2)
        GFX_SetPalette(1)

        def upon_32():
            Unknown2003(1)
            clearUponHandler(32)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('null', 4)
    physicsXImpulse(64000)
    GFX_0('ha_DD_1_shot_a', -1)
    GFX_0('ha_DD_1_shot_b', -1)
    sprite('vrhaef430_dummy', 90)

@State
def ha_DD_1_shot_a():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Hitstop(0)
    label(0)
    sprite('null', 1)
    GFX_1('haef_DD_1_shot', -1)
    loopRest()
    gotoLabel(0)

@State
def ha_DD_1_shot_b():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Hitstop(0)
    label(0)
    sprite('null', 4)
    GFX_1('haef_DD_1_shot_b', -1)
    loopRest()
    gotoLabel(0)

@State
def ha_DD_1_shotSP():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown9001(4)
        AttackLevel_(5)
        ProjectileDurabilityLvl(3)
        HeatGainMultiplier(0)
        Damage(3000)
        AttackP2(80)
        AirUntechableTime(50)
        Hitstop(0)
        Unknown11001(13, 13, 13)
        AirPushbackX(80000)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        StunLength(60)
        StunRecoveryLength(50)
        SlashFX(1)
        StarterRating(2)
        Unknown53(1)
        GFX_SetPalette(2)
        EnableAfterimage(1)
        AfterimageType(2)
        AfterimageCount(10)
        AfterimageSize_1(1000)
        AfterimageSize_2(500)
        Unknown3033()

        def upon_32():
            Unknown2003(1)
            clearUponHandler(32)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('null', 4)
    ProjectileDisapperOnHit(0)
    physicsXImpulse(64000)
    Unknown1028(800)
    Unknown2055(120)
    label(0)
    sprite('vrjnef430_00', 2)
    Unknown3001(255)
    SFX_3('jnse_01')
    sprite('vrjnef430_01', 2)
    SFX_3('jnse_01')
    loopRest()
    gotoLabel(0)

@State
def ha_DD_2_ex():

    def upon_IMMEDIATE():
        ProjectileDisapperOnHit(3)
        Unknown4007(3)
        Unknown2054(1)
    sprite('null', 16)
    Unknown23067('haef_DD_2_ex')
    sprite('null', 1)
    GFX_0('ha_DD_2_ex_usui', -1)
    sprite('null', 60)

@State
def ha_DD_2_ex_usui():

    def upon_IMMEDIATE():
        ProjectileDisapperOnHit(3)
        Unknown4007(3)
        Unknown2054(1)
    sprite('null', 70)
    Unknown23067('haef_DD_2_ex')
    Unknown3001(150)
    Unknown3004(-5)

@State
def ha_AH():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
    sprite('null', 1)
    GFX_1('haef_AH', -1)

@State
def ha_AH_fude():

    def upon_IMMEDIATE():
        Unknown2055(220)
        Unknown4007(3)
    sprite('null', 60)
    GFX_0('ha_451_fude00', -1)
    sprite('null', 16)
    GFX_0('ha_451_fude01', -1)
    sprite('null', 16)
    GFX_0('ha_451_fude02', -1)
    sprite('null', 14)
    GFX_0('ha_451_fude03', -1)
    sprite('null', 14)
    GFX_0('ha_451_fude04', -1)
    sprite('null', 12)
    GFX_0('ha_451_fude05', -1)
    sprite('null', 12)
    GFX_0('ha_451_fude06', -1)
    sprite('null', 10)
    GFX_0('ha_451_fude07', -1)
    sprite('null', 10)
    GFX_0('ha_451_fude08', -1)
    sprite('null', 8)
    GFX_0('ha_451_fude08', -1)
    sprite('null', 8)
    GFX_0('ha_451_fude08', -1)
    sprite('null', 6)
    GFX_0('ha_451_fude08', -1)
    sprite('null', 6)
    GFX_0('ha_451_fude08', -1)
    sprite('null', 4)
    GFX_0('ha_451_fude01', -1)
    sprite('null', 4)
    GFX_0('ha_451_fude08', -1)
    sprite('null', 4)
    GFX_0('ha_451_black00', -1)
    sprite('null', 4)
    GFX_0('ha_451_black01', -1)
    sprite('null', 4)
    GFX_0('ha_451_black02', -1)
    sprite('null', 8)
    GFX_0('ha_451_black03', -1)

@State
def haef_AH_RedBG():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        GFX_2('haef_AH_slash')
    sprite('null', 450)

@State
def ha_451_fude00():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown3035()
        Unknown3001(128)
        Unknown3004(9)
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(1)
        GFX_OffsetX(-180000)
        Unknown1006(224000)
        Unknown1056(1000)
        Unknown1064(1500)
        Unknown1059(1)
        Unknown1067(2)
        GFX_Rotation(-14000)
        physicsXImpulse(-100)
        physicsYImpulse(-100)
    sprite('vrhaef451_fude', 32767)
    GFX_1('haef_AH_2_hit', 1)
    GFX_1('haef_AH_2_drop', 0)
    GFX_0('haef_AH_RedBG', 0)
    SFX_0('020_blood_1')
    SFX_0('015_blaze_2')
    SFX_0('101_hit_slash_3')
    ScreenShake(0, 5000)

@State
def ha_451_fude01():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(1)
        GFX_OffsetX(320000)
        Unknown1006(320000)
        GFX_Rotation(60000)
        Unknown1059(5)
        Unknown1067(2)
        GFX_2('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    GFX_1('haef_AH_2_hit', 0)
    SFX_0('020_blood_1')
    SFX_0('015_blaze_1')
    SFX_0('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    Unknown3004(-2)

@State
def ha_451_fude02():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(1)
        GFX_OffsetX(-16000)
        Unknown1006(288000)
        GFX_Rotation(150000)
        Unknown1059(5)
        Unknown1067(2)
        GFX_2('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    GFX_1('haef_AH_2_hit', 0)
    SFX_0('020_blood_1')
    SFX_0('015_blaze_1')
    SFX_0('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    Unknown3004(-2)

@State
def ha_451_fude03():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(1)
        GFX_OffsetX(-256000)
        Unknown1006(288000)
        GFX_Rotation(285000)
        Unknown1059(5)
        Unknown1067(2)
        GFX_2('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    GFX_1('haef_AH_2_hit', 0)
    SFX_0('020_blood_1')
    SFX_0('015_blaze_1')
    SFX_0('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    Unknown3004(-2)

@State
def ha_451_fude04():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(1)
        GFX_OffsetX(192000)
        Unknown1006(288000)
        GFX_Rotation(30000)
        Unknown1059(5)
        Unknown1067(2)
        GFX_2('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    GFX_1('haef_AH_2_hit', 0)
    SFX_0('020_blood_1')
    SFX_0('015_blaze_1')
    SFX_0('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    Unknown3004(-2)

@State
def ha_451_fude05():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(1)
        GFX_OffsetX(-32000)
        Unknown1006(480000)
        GFX_Rotation(165000)
        Unknown1059(5)
        Unknown1067(2)
        GFX_2('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    GFX_1('haef_AH_2_hit', 0)
    SFX_0('020_blood_1')
    SFX_0('015_blaze_1')
    SFX_0('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    Unknown3004(-2)

@State
def ha_451_fude06():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(1)
        GFX_OffsetX(128000)
        Unknown1006(224000)
        GFX_Rotation(20000)
        Unknown1059(5)
        Unknown1067(2)
        GFX_2('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    GFX_1('haef_AH_2_hit', 0)
    SFX_0('020_blood_1')
    SFX_0('015_blaze_1')
    SFX_0('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    Unknown3004(-2)

@State
def ha_451_fude07():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(1)
        GFX_OffsetX(-512000)
        Unknown1006(448000)
        GFX_Rotation(275000)
        Unknown1059(5)
        Unknown1067(2)
        GFX_2('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    GFX_1('haef_AH_2_hit', 0)
    SFX_0('020_blood_1')
    SFX_0('015_blaze_1')
    SFX_0('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    Unknown3004(-2)

@State
def ha_451_fude08():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(1)
        Unknown1010(-128000, 128000)
        Unknown1011(-128000, 512000)
        Unknown1077(0, 364000)
        Unknown1059(5)
        Unknown1067(2)
        GFX_2('haef_AH_2_slash')
    sprite('vrhaef451_fude', 60)
    GFX_1('haef_AH_2_hit_pos', 0)
    SFX_0('020_blood_1')
    SFX_0('015_blaze_1')
    SFX_0('101_hit_slash_3')
    ScreenShake(0, 5000)
    sprite('vrhaef451_fude', 125)
    Unknown3004(-2)

@State
def ha_451_black00():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(1)
        GFX_OffsetX(360000)
        Unknown1006(288000)
        Unknown1056(4000)
        Unknown1064(320000)
        GFX_Rotation(10000)
        Unknown3001(64)
    sprite('vrhaef451_black', 32767)
    SFX_0('020_blood_1')
    SFX_0('015_blaze_1')
    SFX_0('101_hit_slash_3')
    ScreenShake(0, 5000)

@State
def ha_451_black01():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(1)
        GFX_OffsetX(480000)
        Unknown1006(288000)
        Unknown1056(5000)
        Unknown1064(320000)
        GFX_Rotation(-15000)
        Unknown3001(64)
    sprite('vrhaef451_black', 32767)
    SFX_0('020_blood_1')
    SFX_0('015_blaze_1')
    SFX_0('101_hit_slash_3')
    ScreenShake(0, 5000)

@State
def ha_451_black02():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(1)
        GFX_OffsetX(-576000)
        Unknown1006(288000)
        Unknown1056(10000)
        Unknown1064(320000)
        GFX_Rotation(-10000)
        Unknown3001(64)
    sprite('vrhaef451_black', 32767)
    SFX_0('020_blood_1')
    SFX_0('015_blaze_1')
    SFX_0('101_hit_slash_3')
    ScreenShake(0, 5000)

@State
def ha_451_black03():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown3035()
        Unknown4010(2)
        Unknown4007(2)
        GFX_SetPalette(1)
        Unknown1006(288000)
        Unknown1056(320000)
        Unknown1064(320000)
        GFX_Rotation(-10000)
        Unknown3001(255)
    sprite('vrhaef451_black', 32767)
    SFX_0('020_blood_1')
    SFX_0('015_blaze_1')
    SFX_0('101_hit_slash_3')

@State
def ha_451_finish():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown11064(3)
        Damage(38000)
        MinimumDamagePct(100)
        Unknown23011(18)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        StunLength(70)
        StunRecoveryLength(67)
        SlashFX(1)
        Unknown11057(2000)
        Unknown11023(1)
        HitOverhead(4)
        HitLow(4)
        HitAirUnblockable(4)
        Unknown4007(3)
        GFX_SetPalette(1)
        sendToLabelUpon(12, 0)

        def upon_ON_HIT_OR_BLOCK():
            GFX_1('haef_AH_2_hit', 101)
    sprite('vrhaef451_dummy', 3)
    Unknown1006(288000)
    Hitstop(25)
    GFX_1('haef_AH_2_finish03', -1)
    SFX_0('025_cleanhit_slash')
    SFX_0('101_hit_slash_3')
    loopRest()
    label(0)
    sprite('null', 1)

@State
def HaAstBG_Start():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown1006(200000)
        GFX_1('haef_AH_ground', -1)
        Unknown23032(50)
        Unknown23033(50)
        Unknown2019(500)
        Unknown3033()
        Unknown3001(0)
        Unknown3004(50)
        Unknown1056(10000)
        Unknown1064(2200)
    sprite('vr_white', 32767)

@State
def HaAstBG_Finish():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown1006(200000)
        GFX_1('haef_AH_ground00', -1)
        Unknown23032(50)
        Unknown23033(50)
        Unknown2019(500)
        Unknown3033()
        Unknown3001(0)
        Unknown3004(4)
        Unknown1056(10000)
        Unknown1064(2200)
    sprite('vr_white', 32767)

@State
def EventEffectHAVsRG_TB():
    Unknown1000(-460000)
    sendToLabelUpon(32, 1)
    GFX_SetPalette(6)
    label(0)
    sprite('tb070_03', 1)
    gotoLabel(0)
    label(1)
    clearUponHandler(32)
    sprite('tb070_03', 6)
    sprite('tb070_02', 5)
    sprite('tb070_01', 4)
    sprite('tb070_00', 4)
    sprite('tb033_00', 2)
    sprite('tb033_01', 2)
    physicsXImpulse(-25000)
    physicsYImpulse(11000)
    setGravity(1550)
    SFX_0('205_runjump_garden_1')
    sprite('tb033_02', 2)
    sprite('tb033_02', 1)
    sprite('tb033_03', 3)
    loopRest()
    sendToLabelUpon(2, 3)
    label(2)
    sprite('tb033_02', 3)
    sprite('tb033_03', 3)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('tb033_04', 2)
    endMomentum(1)
    sprite('tb033_05', 2)
    sprite('null', 32767)
    loopRest()

@State
def NOISE():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('ef_eventnoise.DIG', '')
        Unknown4015()
        Unknown23015(4)
        Unknown23032(50)
        Unknown23033(50)
    sprite('null', 80)
    loopRest()

@State
def SummonTrinity():

    def upon_IMMEDIATE():
        GFX_SetPalette(5)
        Unknown3001(0)
        Unknown3032()
        GFX_OffsetY(50000)
        GFX_OffsetX(40000)
    sprite('pt999_00', 75)
    Unknown3004(3)
    sprite('pt999_00', 10)
    Unknown3004(0)
    Unknown23119(3289650, 120, 120)
    label(0)
    sprite('pt999_00', 50)
    physicsYImpulse(100)
    sprite('pt999_00', 50)
    sprite('pt999_00', 20)
    physicsYImpulse(0)
    sprite('pt999_00', 100)
    physicsYImpulse(-100)
    sprite('pt999_00', 10)
    physicsYImpulse(0)
    loopRest()
    gotoLabel(0)

@Subroutine
def ShotDelete_dmy():
    ProjectileDisapperOnHit(2)
    Unknown4010(2)
    Unknown4007(2)
    Unknown4009(2)
    GuardPoint_(1)
    setInvincible(1)
    defineInvincibility(0, 0, 0, 1, 0)
    Unknown22031(0, 0)
    Unknown22032(1)
    Unknown2037(1)

    def upon_3():
        if (not SLOT_30):

            def upon_42():
                if SLOT_2:
                    Unknown21007(3, 32)
                    HeatChange(1250)
                    Unknown2038(-1)
                    Unknown21012('ShotDelete', 39)
                    GFX_0('ShotDelete', 102)
                    SFX_3('hase_23')

@State
def ha202_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha202_col_dmy_00', 1)
    sprite('ha202_col_dmy_01', 2)

@State
def ha212_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha212_col_dmy_00', 2)
    sprite('ha212_col_dmy_01', 3)

@State
def ha232_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha232_col_dmy_00', 3)
    sprite('ha232_col_dmy_03', 3)
    sprite('ha232_col_dmy_04', 3)

@State
def ha234_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha234_col_dmy_00', 1)
    sprite('ha234_col_dmy_01', 3)
    sprite('ha234_col_dmy_02', 4)

@State
def ha214_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha214_col_dmy_00', 1)
    sprite('ha214_col_dmy_01', 1)
    sprite('ha214_col_dmy_02', 1)

@State
def ha252_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha252_col_dmy_00', 2)
    sprite('ha252_col_dmy_01', 3)
    sprite('ha252_col_dmy_02', 1)

@State
def ha260_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha260_col_dmy_00', 6)
    sprite('ha260_col_dmy_01', 4)
    sprite('ha260_col_dmy_02', 4)
    sprite('ha260_col_dmy_03', 4)

@State
def ha406_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha406_col_dmy_00', 2)
    sprite('ha406_col_dmy_01', 2)
    sprite('ha406_col_dmy_02', 6)

@State
def ha402_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha402_col_dmy_00', 3)
    sprite('null', 14)
    sprite('ha402_col_dmy_01', 3)

@State
def ha404_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha404_col_dmy_00', 3)

@State
def ha430_col_dmy():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha430_col_dmy_00', 4)

@State
def ha430_col_dmy_OD():

    def upon_IMMEDIATE():
        callSubroutine('ShotDelete_dmy')
    sprite('ha430_col_dmy_00', 4)

@State
def BurstDD_Camera_Super():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        Unknown1006(0)
    sprite('null', 10)

@State
def BurstDD_Camera_Normal():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        Unknown20003(1)
        Unknown1086(22)
    sprite('null', 300)

@State
def Act3Event_havsno_01():
    sprite('null', 32767)
    Unknown1000(360000)
    CameraControlEnable(1)

@State
def Act3Event_ObjCol():

    def upon_IMMEDIATE():
        loopRelated(17, 50)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('null', 1)
    SLOT_52 = (SLOT_52 + 1)
    Unknown48(2, 2, 52, 23, 2, 52)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 1)

@State
def Act3Event_ha_DD_1_shot():

    def upon_IMMEDIATE():
        GFX_SetPalette(1)
    sprite('null', 30)
    physicsXImpulse(64000)
    GFX_0('ha_DD_1_shot_a', -1)
    GFX_0('ha_DD_1_shot_b', -1)