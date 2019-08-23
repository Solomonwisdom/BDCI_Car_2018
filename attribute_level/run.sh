#! /bin/bash

python /workspace/BDCI_Car_2018/attribute_level/attribute.py --mode 2 --test_dir cp_CNN_0#cp_CNN_ft2#cp_CNN_2#cp_CNN_tc#cp_AttA3_0#cp_AttA3_ft2#cp_AttA3_2#cp_AttA3_tc#cp_Bert --saved 1
python /workspace/BDCI_Car_2018/polarity_level_aspect/ab_polarity.py --mode 2 --test_dir cp_HEAT_0#cp_AT_LSTM_0#cp_HEAT_ft2#cp_AT_LSTM_ft2#cp_HEAT_2#cp_AT_LSTM_2#cp_HEAT_tc#cp_AT_LSTM_tc#cp_GCAE_0#cp_GCAE_2#cp_GCAE_ft2#cp_GCAE_tc#cp_Bert --saved 1
python /workspace/BDCI_Car_2018/data/submit2.py