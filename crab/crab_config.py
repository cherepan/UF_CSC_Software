from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'RAW2DIGI_RealVal'
config.General.workArea =  'crab_area_ZMMRelVal_09_08_2024'
config.General.transferLogs = True


config.section_("JobType")
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ProduceReco_v2_py_RAW2DIGI_L1Reco_RECO_RECOSIM.py'
config.JobType.maxMemoryMB      = 8000
config.JobType.maxJobRuntimeMin = 2750
config.JobType.numCores = 4

config.section_("Data")

#config.Data.inputDataset = '/RelValZMM_PU_13p6/CMSSW_12_4_12-PU_124X_mcRun3_2022_realistic_postEE_forPixelIneff_v5_PDMVRELVALS188_HS_2023PU-v1/GEN-SIM-DIGI-RAW'
#config.Data.inputDataset = '/RelValSingleMuPt100/CMSSW_12_4_14_patch2-124X_mcRun3_2022_realistic_v12_RV205-v1/GEN-SIM-DIGI-RAW'
#config.Data.inputDataset = '/RelValZMM_14/CMSSW_12_4_13-124X_mcRun3_2022_realistic_v12_2021-v1/GEN-SIM-DIGI-RAW'
config.Data.inputDataset = '/RelValZMM_14/CMSSW_13_3_0-133X_mcRun3_2024_realistic_v7_Winter24Validation-v1/GEN-SIM-DIGI-RAW'

config.Data.inputDBS  = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits  = 61
#config.Data.lumiMask = 'Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
config.Data.publication = True
config.Data.outLFNDirBase = '/store/user/cherepan'
config.Data.outputDatasetTag = 'RelValZMM_CMSSW_13_3_0_FullTier_09_08_2024'


config.section_("Site")
##config.Site.whitelist = ['T2_US_Wisconsin','T2_US_Purdue','T1_US_FNAL']
##config.Data.ignoreLocality = True
#config.Site.storageSite = 'T2_US_Florida'
config.Site.whitelist = ['T2_US_Florida','T2_US_Wisconsin','T2_US_Purdue','T1_US_FNAL']
config.Data.ignoreLocality = True
config.Site.storageSite = 'T2_US_Florida'

