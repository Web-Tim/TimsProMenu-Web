import pymem
import pymem.process
import keyboard
import time

# Mathematical 
def divide(num, times):
    if times == 1 or times == 0:
        return num
    if times == -1 or times == -0:
        return -num
    if times == 2:
        return num * num
    if times == 3:
        return num * num * num
    if times == 4:
        return num * num * num * num
    if times == 5:
        return num * num * num * num * num
    if times == 6:
        return num * num * num * num * num * num
    if times == 7:
        return num * num * num * num * num * num * num
    if times == 8:
        return num * num * num * num * num * num * num * num
    if times == 9:
        return num * num * num * num * num * num * num * num * num
    if times == 10:
        return num * num * num * num * num * num * num * num * num * num
    if times == 11:
        return num * num * num * num * num * num * num * num * num * num * num
    if times == 12:
        return num * num * num * num * num * num * num * num * num * num * num * num
    if times == 13:
        return num * num * num * num * num * num * num * num * num * num * num * num * num
    if times == 14:
        return num * num * num * num * num * num * num * num * num * num * num * num * num * num
    if times == 15:
        return num * num * num * num * num * num * num * num * num * num * num * num * num * num * num
    if times == 16:
        return num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num
    if times == 17:
        return num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num
    if times == 18:
        return num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num
    if times == 19:
        return num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num
    if times == 20:
        return num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num
    if times == 21:
        return num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num
    if times == 22:
        return num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num
    if times == 23:
        return num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num
    if times == 24:
        return num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num
    
    if times == -2:
        return -(num * num)
    if times == -3:
        return -(num * num * num)
    if times == -4:
        return -(num * num * num * num)
    if times == -5:
        return -(num * num * num * num * num)
    if times == -6:
        return -(num * num * num * num * num * num)
    if times == -7:
        return -(num * num * num * num * num * num * num)
    if times == -8:
        return -(num * num * num * num * num * num * num * num)
    if times == -9:
        return -(num * num * num * num * num * num * num * num * num)
    if times == -10:
        return -(num * num * num * num * num * num * num * num * num * num)
    if times == -11:
        return -(num * num * num * num * num * num * num * num * num * num * num)
    if times == -12:
        return -(num * num * num * num * num * num * num * num * num * num * num * num)
    if times == -13:
        return -(num * num * num * num * num * num * num * num * num * num * num * num * num)
    if times == -14:
        return -(num * num * num * num * num * num * num * num * num * num * num * num * num * num)
    if times == -15:
        return -(num * num * num * num * num * num * num * num * num * num * num * num * num * num * num)
    if times == -16:
        return -(num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num)
    if times == -17:
        return -(num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num)
    if times == -18:
        return -(num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num)
    if times == -19:
        return -(num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num)
    if times == -20:
        return -(num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num)
    if times == -21:
        return -(num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num)
    if times == -22:
        return -(num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num)
    if times == -23:
        return -(num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num)
    if times == -24:
        return -(num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num * num)
    
    if times > 24:
        print("The Maximum number to divide the number is 24!")
        return num


# Process (Attaching | Writing | Reading)
pm = pymem.Pymem("csgo.exe")
dllg = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

def attach(process, dllName):
    pm = pymem.Pymem(process)
    dllg = pymem.process.module_from_name(pm.process_handle, dllName).lpBaseOfDll

def free(address):
    pymem.Pymem.free(pm, address)

def rpm(hex, type):
    if pm:
        if type == "int":
            return pm.read_int(hex)

        if type == "byte":
            return pm.read_byte(hex)

        if type == "char":
            return pm.read_char(hex)

        if type == "double":
            return pm.read_double(hex)

        if type == "float":
            return pm.read_float(hex)

        if type == "long":
            return pm.read_long(hex)

        if type == "longlong":
            return pm.read_longlong(hex)

        if type == "short":
            return pm.read_short(hex)

        if type == "string":
            return pm.read_string(hex)

        if type == "uchar":
            return pm.read_uchar(hex)

        if type == "uint":
            return pm.read_uint(hex)

        if type == "ulong":
            return pm.read_ulong(hex)

        if type == "ulonglong":
            return pm.read_ulonglong(hex)

        if type == "ushort":
            return pm.read_ushort(hex)
    else:
        print("Before Reading Process Memory, attach the process! \n")
        exit(-1)
        return None

def wpm(hex, type, newVal):
    if pm:
        if type == "int":
            pm.write_int(hex, newVal)

        if type == "byte":
            pm.write_byte(hex, newVal)

        if type == "char":
            pm.write_char(hex, newVal)

        if type == "double":
            pm.write_double(hex, newVal)

        if type == "float":
            pm.write_float(hex, newVal)

        if type == "long":
            pm.write_long(hex, newVal)

        if type == "longlong":
            pm.write_longlong(hex, newVal)

        if type == "short":
            pm.write_short(hex, newVal)

        if type == "string":
            pm.write_string(hex, newVal)

        if type == "uchar":
            pm.write_uchar(hex, newVal)

        if type == "uint":
            pm.write_uint(hex, newVal)

        if type == "ulong":
            pm.write_ulong(hex, newVal)

        if type == "ulonglong":
            pm.write_ulonglong(hex, newVal)

        if type == "ushort":
            pm.write_ushort(hex, newVal)
    else:
        print("Before Reading Process Memory, attach the process! \n")
        exit(-1)

def close(process):
    if pm:
        pymem.Pymem.close_process(pm)
    else:
        print("No Process is attached, first attach a Process!")
        exit(-1)

def getdll():
    if dllg:
        return dllg
    else:
        print("Before getting the Dll, you need to attach it!")
        return None

# CSGO Specialized CONFIG

# (VARIABLES: [GITHUB_HAZEDUMPER:NETVARS])
cs_gamerules_data = (0x0)
m_ArmorValue = (0xB378)
m_Collision = (0x320)
m_CollisionGroup = (0x474)
m_Local = (0x2FBC)
m_MoveType = (0x25C)
m_OriginalOwnerXuidHigh = (0x31C4)
m_OriginalOwnerXuidLow = (0x31C0)
m_SurvivalGameRuleDecisionTypes = (0x1328)
m_SurvivalRules = (0xD00)
m_aimPunchAngle = (0x302C)
m_aimPunchAngleVel = (0x3038)
m_angEyeAnglesX = (0xB37C)
m_angEyeAnglesY = (0xB380)
m_bBombPlanted = (0x9A5)
m_bFreezePeriod = (0x20)
m_bGunGameImmunity = (0x3944)
m_bHasDefuser = (0xB388)
m_bHasHelmet = (0xB36C)
m_bInReload = (0x32A5)
m_bIsDefusing = (0x3930)
m_bIsQueuedMatchmaking = (0x74)
m_bIsScoped = (0x3928)
m_bIsValveDS = (0x7C)
m_bSpotted = (0x93D)
m_bSpottedByMask = (0x980)
m_bStartedArming = (0x33F0)
m_bUseCustomAutoExposureMax = (0x9D9)
m_bUseCustomAutoExposureMin = (0x9D8)
m_bUseCustomBloomScale = (0x9DA)
m_clrRender = (0x70)
m_dwBoneMatrix = (0x26A8)
m_fAccuracyPenalty = (0x3330)
m_fFlags = (0x104)
m_flC4Blow = (0x2990)
m_flCustomAutoExposureMax = (0x9E0)
m_flCustomAutoExposureMin = (0x9DC)
m_flCustomBloomScale = (0x9E4)
m_flDefuseCountDown = (0x29AC)
m_flDefuseLength = (0x29A8)
m_flFallbackWear = (0x31D0)
m_flFlashDuration = (0xA420)
m_flFlashMaxAlpha = (0xA41C)
m_flLastBoneSetupTime = (0x2924)
m_flLowerBodyYawTarget = (0x3A90)
m_flNextAttack = (0x2D70)
m_flNextPrimaryAttack = (0x3238)
m_flSimulationTime = (0x268)
m_flTimerLength = (0x2994)
m_hActiveWeapon = (0x2EF8)
m_hMyWeapons = (0x2DF8)
m_hObserverTarget = (0x338C)
m_hOwner = (0x29CC)
m_hOwnerEntity = (0x14C)
m_iAccountID = (0x2FC8)
m_iClip1 = (0x3264)
m_iCompetitiveRanking = (0x1A84)
m_iCompetitiveWins = (0x1B88)
m_iCrosshairId = (0xB3E4)
m_iDefaultFOV = (0x332C)
m_iEntityQuality = (0x2FAC)
m_iFOVStart = (0x31E8)
m_iGlowIndex = (0xA438)
m_iHealth = (0x100)
m_iItemDefinitionIndex = (0x2FAA)
m_iItemIDHigh = (0x2FC0)
m_iMostRecentModelBoneCounter = (0x2690)
m_iObserverMode = (0x3378)
m_iShotsFired = (0xA390)
m_iState = (0x3258)
m_iTeamNum = (0xF4)
m_lifeState = (0x25F)
m_nFallbackPaintKit = (0x31C8)
m_nFallbackSeed = (0x31CC)
m_nFallbackStatTrak = (0x31D4)
m_nForceBone = (0x268C)
m_nTickBase = (0x3430)
m_rgflCoordinateFrame = (0x444)
m_szCustomName = (0x303C)
m_szLastPlaceName = (0x35B4)
m_thirdPersonViewAngles = (0x31D8)
m_vecOrigin = (0x138)
m_vecVelocity = (0x114)
m_vecViewOffset = (0x108)
m_viewPunchAngle = (0x3020)

# (VARIABLES: [GITHUB_HAZEDUMPER:SIGNATURES])
anim_overlays = (0x2980)
clientstate_choked_commands = (0x4D30)
clientstate_delta_ticks = (0x174)
clientstate_last_outgoing_command = (0x4D2C)
clientstate_net_channel = (0x9C)
convar_name_hash_table = (0x2F0F8)
dwClientState = (0x58EFE4)
dwClientState_GetLocalPlayer = (0x180)
dwClientState_IsHLTV = (0x4D48)
dwClientState_Map = (0x28C)
dwClientState_MapDirectory = (0x188)
dwClientState_MaxPlayer = (0x388)
dwClientState_PlayerInfo = (0x52C0)
dwClientState_State = (0x108)
dwClientState_ViewAngles = (0x4D90)
dwEntityList = (0x4DA2F44)
dwForceAttack = (0x31D44D4)
dwForceAttack2 = (0x31D44E0)
dwForceBackward = (0x31D448C)
dwForceForward = (0x31D44F8)
dwForceJump = (0x524CEA4)
dwForceLeft = (0x31D4480)
dwForceRight = (0x31D44A4)
dwGameDir = (0x62D7F8)
dwGameRulesProxy = (0x52C018C)
dwGetAllClasses = (0xDB2F8C)
dwGlobalVars = (0x58ECE8)
dwGlowObjectManager = (0x52EB540)
dwInput = (0x51F4528)
dwInterfaceLinkList = (0x945874)
dwLocalPlayer = (0xD8B2BC)
dwMouseEnable = (0xD90E60)
dwMouseEnablePtr = (0xD90E30)
dwPlayerResource = (0x31D2800)
dwRadarBase = (0x51D7CBC)
dwSensitivity = (0xD90CFC)
dwSensitivityPtr = (0xD90CD0)
dwSetClanTag = (0x8A1A0)
dwViewMatrix = (0x4D94844)
dwWeaponTable = (0x51F4FE8)
dwWeaponTableIndex = (0x325C)
dwYawPtr = (0xD90AC0)
dwZoomSensitivityRatioPtr = (0xD95D60)
dwbSendPackets = (0xD745A)
dwppDirect3DDevice9 = (0xA7050)
find_hud_element = (0x2E19E320)
force_update_spectator_glow = (0x3AD962)
interface_engine_cvar = (0x3E9EC)
is_c4_owner = (0x3BA430)
m_bDormant = (0xED)
m_flSpawnTime = (0xA370)
m_pStudioHdr = (0x294C)
m_pitchClassPtr = (0x51D7F58)
m_yawClassPtr = (0xD90AC0)
model_ambient_min = (0x59205C)
set_abs_angles = (0x1DF9C0)
set_abs_origin = (0x1DF800)

# Credits to "https://github.com/frk1/hazedumper/" all Hexideximal Vaules are from there!

# CS:GO | GET Functions
def cs_get_local_player():
    return rpm(getdll() + dwLocalPlayer, "int")

def cs_get_crosshair_id():
    return rpm(cs_get_local_player() + m_iCrosshairId, "int")

def cs_get_local_team():
    return rpm(cs_get_local_player() + m_iTeamNum, "int")

def cs_get_force_jump():
    return rpm(getdll() + dwForceJump, "int")

def cs_get_glow_manager():
    return rpm(getdll() + dwGlowObjectManager, "int")

def cs_get_enemy():
    for i in range(1, 64):
        enemy = rpm(getdll() + dwEntityList + i * 0x10, "int")
        if not enemy == cs_get_local_player():
            return enemy

def cs_get_local_player_fov():
    return rpm(cs_get_local_player() + m_iDefaultFOV, "int")

def cs_get_local_player_on_ground():
    return rpm(cs_get_local_player() + m_fFlags, "int")

# CS:GO | SET Functions / implemented Cheats
def cs_toggle_bhop(bool):
    if bool == True:
        while True:
            if keyboard.is_pressed("space"):
                force_jump = cs_get_force_jump()
                player = cs_get_local_player()
                onGround = cs_get_local_player_on_ground()
                if player and onGround and onGround == 257:
                    wpm(force_jump, 5, "int")
                    time.sleep(0.08)
                    wpm(force_jump, 4, "int")

def cs_toggle_glow(bool):
    if bool == True:
        while True:
            glow_manager = cs_get_glow_manager()
            for i in range(1, 64):
                entity = rpm(getdll() + dwEntityList + i * 0x10, "int")

                if entity:
                    entity_team_id = rpm(entity + m_iTeamNum, "int")
                    entity_glow = rpm(entity + m_iGlowIndex, "int")
                        
                    if entity_team_id == 3:
                        wpm(glow_manager + entity_glow * 0x38 + 0x4, float(1), "float")
                        wpm(glow_manager + entity_glow * 0x38 + 0x8, float(0), "float")
                        wpm(glow_manager + entity_glow * 0x38 + 0xC, float(0), "float")
                        wpm(glow_manager + entity_glow * 0x38 + 0x10, float(1), "float")
                        wpm(glow_manager + entity_glow * 0x38 + 0x24, 1, "float")
                    elif entity_team_id == 2:
                        wpm(glow_manager + entity_glow * 0x38 + 0x4, float(0), "float")
                        wpm(glow_manager + entity_glow * 0x38 + 0x8, float(1), "float")
                        wpm(glow_manager + entity_glow * 0x38 + 0xC, float(0), "float")
                        wpm(glow_manager + entity_glow * 0x38 + 0x10, float(1), "float")
                        wpm(glow_manager + entity_glow * 0x38 + 0x24, 1, "float")

def cs_set_local_player_fov(value):
    wpm(cs_get_local_player_fov(), "int", value)



##          !!!                        Copyright by Tim                        !!!
##          !!! USING THIS LIBRARY FREE IS ALLOWED, BUT SKIDING THIS CODE ISNT !!!