import paho.mqtt.client as mqtt
import json
import argparse
import time
from datetime import datetime
import random
# from cloud.process.RBI import DM_CAL

# This is the Publisher
# d = DM_CAL.DM_CAL(HighlyEffectDeadleg=True, ContainsDeadlegs=False, OnlineMonitoring="Sulfuric acid (H2S/H2) corrosion high velocity - Key process parameters")
# print(d.DF_THIN(5.08))

# 79 inputs can determine by sensor
def set_data(Op7, BrittleFacture, H2SInWater, ReleasePercentToxic, PresenceofSulphides, 
    PreviousFailures, EnvCaustic, maxOP, CylicLoad, minOP, ExternalCoatingQuality, 
    HydrogenFluoric, NorminalDiameter, 
    maxOT, ToxicConstituents, SteamedOut, 
    PresenceCracks, PersonDensity, PressurisationControlled, ExposureAmine, SulphurContent, 
    CylicOper, DetectionType, EquipmentVolumn, Chromium, PHWater, CurrentCorrosionRate, minOT, 
    InterfaceSoilWater, BranchDiameter, Op2, 
    ChemicalInjection, NaOHConcentration, Op1, ExternalInsulation, CurrentThickness, Op9, NorminalThickness, 
    System, ExternalCoating, CO3, 
    materialExposedFluid, Op6, ThermalHistory, Op4, exposureAcid, 
    ToxicPercent, EnvCH2S, InsulationType,
    OpHydrogenPressure, minTemp, hydrogen, PresenceCyanides, ExposedSulfur, 
    CladdingCorrosionRate, Op10, SusceptibleTemper, InternalLinerCondition, 
    RiskAnalystPeriod, ShakingAmount, ChlorideIon, Op8, AqueShutdown, 
    PresenceofSulphidesShutdown, DFDI, InternalLining, 
    VASD, ExternalEnvironment, Op3, MaxBrinell, timeShakingPipe, SigmaPhase, 
    EquOper, MFTF, PipeCondition, complex, MinReqThickness, Op5, SulfurContent, AqueOp):
    data = []
    # rw_assessment
    # data["RiskAnalystPeriod"] = RiskAnalystPeriod
    #end rw_assessment

    # rw_equipment
    data_equipment = {}
    data_equipment["CylicOper"] = CylicOper
    data_equipment["ExternalEnvironment"] = ExternalEnvironment
    data_equipment["InterfaceSoilWater"] = InterfaceSoilWater
    data_equipment["MFTF"] = MFTF
    data_equipment["minTemp"] = minTemp
    data_equipment["PresenceofSulphidesShutdown"] = PresenceofSulphidesShutdown
    data_equipment["PresenceofSulphides"] = PresenceofSulphides
    data_equipment["PressurisationControlled"] = PressurisationControlled
    data_equipment["ThermalHistory"] = ThermalHistory
    data_equipment["SteamedOut"] = SteamedOut
    data_equipment["EquOper"] = EquOper
    data_equipment["EquipmentVolumn"] = EquipmentVolumn
    data.append(data_equipment)
    # end rw_equipment

    # rw_component
    data_component = {}
    data_component["MaxBrinell"] = MaxBrinell
    data_component["NorminalDiameter"] = NorminalDiameter
    data_component["NorminalThickness"] = NorminalThickness
    data_component["CurrentThickness"] = CurrentThickness
    data_component["MinReqThickness"] = MinReqThickness
    data_component["CurrentCorrosionRate"] = CurrentCorrosionRate
    data_component["BranchDiameter"] = BranchDiameter
    data_component["ChemicalInjection"] = ChemicalInjection
    data_component["complex"] = complex
    data_component["PresenceCracks"] = PresenceCracks
    data_component["CylicLoad"] = CylicLoad
    data_component["DFDI"] = DFDI
    data_component["PipeCondition"] = PipeCondition
    data_component["PreviousFailures"] = PreviousFailures
    data_component["ShakingAmount"] = ShakingAmount
    data_component["VASD"] = VASD
    data_component["timeShakingPipe"] = timeShakingPipe
    data.append(data_component)
    # end rw_component

    # rw_stream
    data_stream = {}
    data_stream["AqueShutdown"] = AqueShutdown
    data_stream["AqueOp"] = AqueOp
    data_stream["ToxicConstituents"] = ToxicConstituents
    data_stream["EnvCaustic"] = EnvCaustic
    data_stream["ChlorideIon"] = ChlorideIon
    data_stream["CO3"] = CO3
    data_stream["PresenceCyanides"] = PresenceCyanides
    data_stream["exposureAcid"] = exposureAcid
    data_stream["ExposedSulfur"] = ExposedSulfur
    data_stream["ExposureAmine"] = ExposureAmine
    data_stream["EnvCH2S"] = EnvCH2S
    data_stream["H2SInWater"] = H2SInWater
    data_stream["hydrogen"] = hydrogen
    data_stream["HydrogenFluoric"] = HydrogenFluoric
    data_stream["materialExposedFluid"] = materialExposedFluid
    data_stream["maxOP"] = maxOP
    data_stream["maxOT"] = maxOT
    data_stream["minOP"] = minOP
    data_stream["minOT"] = minOT
    data_stream["NaOHConcentration"] = NaOHConcentration
    data_stream["ReleasePercentToxic"] = ReleasePercentToxic
    data_stream["PHWater"] = PHWater
    data_stream["OpHydrogenPressure"] = OpHydrogenPressure
    data.append(data_stream)
    # end rw_stream

    # rw_excor
    data_excor = {}
    data_excor["Op1"] = Op1
    data_excor["Op2"] = Op2
    data_excor["Op3"] = Op3
    data_excor["Op4"] = Op4
    data_excor["Op5"] = Op5
    data_excor["Op6"] = Op6
    data_excor["Op7"] = Op7
    data_excor["Op8"] = Op8
    data_excor["Op9"] = Op9
    data_excor["Op10"] = Op10
    data.append(data_excor)
    # end rw_excor
    
    # rw_coat
    data_coat = {}
    data_coat["ExternalCoating"] = ExternalCoating
    data_coat["ExternalInsulation"] = ExternalInsulation
    data_coat["InternalLining"] = InternalLining
    data_coat["ExternalCoatingQuality"] = ExternalCoatingQuality
    data_coat["InternalLinerCondition"] = InternalLinerCondition
    data_coat["CladdingCorrosionRate"] = CladdingCorrosionRate
    data.append(data_coat)
    # end rw_coat

    # rw_material
    data_material = {}
    data_material["BrittleFacture"] = BrittleFacture
    data_material["SigmaPhase"] = SigmaPhase
    data_material["SulfurContent"] = SulfurContent
    data_material["SusceptibleTemper"] = SusceptibleTemper
    data_material["Chromium"] = Chromium
    data_material["SulphurContent"] = SulphurContent
    data.append(data_material)
    # end rw_material

    # ca
    data_ca = {}
    data_ca["System"] = System
    data_ca["DetectionType"] = DetectionType
    data_ca["InsulationType"] = InsulationType
    data_ca["ToxicPercent"] = ToxicPercent
    data.append(data_ca)
    # end ca
    return data
def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server_ip', default='localhost', help='Server IP address')
    parser.add_argument('--port', default=1883, help='Port listen')
    # parser.add_argument('--u', defaul='$ACCESS_TOKEN', help="User access token")
    return parser.parse_args()

def publish_data(data, strType):
    print("Collecting " + strType + " data...")
    args = parse_command_line_args()
    CLOUD_URL = args.server_ip
    PORT = int(args.port)
    client = mqtt.Client()
    client.connect (CLOUD_URL, PORT, 60)
    time.sleep(random.random())
    print("Publishing " + strType + "...")
    send_data = json.dumps(data)
    client.publish("7/proposal_" + str(datetime.now()) + "/" + strType, send_data)
    client.disconnect()
    print("Published!")

def main():
    args = parse_command_line_args()
    CLOUD_URL = args.server_ip
    PORT = int(args.port)
    
    client = mqtt.Client()
    client.connect (CLOUD_URL, PORT, 60)

    data = set_data(Chromium=False, materialExposedFluid=False, Op3=0, RiskAnalystPeriod=36, 
        PressurisationControlled=False, NorminalThickness=19.05,  EquOper=False,
        PipeCondition="Broken gussets or gussets welded directly to pipe", ThermalHistory="Solution Annealed", 
        EquipmentVolumn=100, Op4=0,
        OpHydrogenPressure=10000, EnvCaustic=False, Op9=0, Op6=0, ExposureAmine="Low Lean Amine",
        minOT=20, CO3=0, PresenceCyanides=False, Op7=100, DFDI=False, ExternalCoatingQuality="Please select coat quality..", 
        HydrogenFluoric=False, ToxicConstituents=True, H2SInWater=1000, InsulationType='C', 
        MinReqThickness=16.68, SusceptibleTemper=False, PreviousFailures="Greater than one", 
        BranchDiameter="Any branch less than or equal to 2\" Nominal OD", MaxBrinell="Below 200", 
        CylicOper=True, PHWater=5, ExposedSulfur=False, CladdingCorrosionRate=0.29, 
        Op10=0, Op2=0, ChlorideIon=1000, PersonDensity=0.005, 
        SulphurContent="High > 0.01%", complex="Above Average",
        SteamedOut=False, CurrentThickness=19.05, Op8=0, AqueShutdown=False, MFTF=False, 
        ReleasePercentToxic=1, Op1=0, BrittleFacture=1, ExternalEnvironment="Arid/dry", maxOP=1000, 
        timeShakingPipe="13 to 52 weeks", ChemicalInjection=False,
        DetectionType='C', ShakingAmount="Moderate", SigmaPhase=1, 
        InternalLinerCondition="Poor", System="Vapor", minOP=200, 
        NaOHConcentration=11, hydrogen=False, PresenceCracks=False, VASD=True, PresenceofSulphides=False, 
        maxOT=100, exposureAcid=False, InternalLining=True, Op5=0, ExternalCoating=False, 
        CylicLoad="Valve with high pressure drop", PresenceofSulphidesShutdown=False, EnvCH2S=False, 
        NorminalDiameter=97.62, ExternalInsulation=1, minTemp=45, 
        CurrentCorrosionRate=0.29, InterfaceSoilWater=False, 
        ToxicPercent=0, SulfurContent=0, AqueOp=0)
    time.sleep(3)
    sub_type_list = ["equipment", "component", "stream", "excor", "coating", "material", "CA"]
    for i in range(0, 7):
        publish_data(data[i], sub_type_list[i])
        time.sleep(3)

if __name__ == "__main__":
    main()


