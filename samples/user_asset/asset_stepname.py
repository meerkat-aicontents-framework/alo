# -*- coding: utf-8 -*-
import os
import sys
from alolib.asset import Asset

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
## 동일 위치의 *.py 를 제작한 경우 해당 위헤서는 import
# from algorithm_engine import TITANIC

#--------------------------------------------------------------------------------------------------------------------------
#    CLASS
#--------------------------------------------------------------------------------------------------------------------------
class UserAsset(Asset):
    def __init__(self, asset_structure):
        super().__init__(asset_structure)
        ############################ ASSET API (v.1.0) ####################################
        # collab : http://mod.lge.com/hub/dxadvtech/aicontents-framework/alo

        # self.asset.check_args(arg_key, is_required=False, default="", chng_type="str")

        # self.asset.save_summary(result='OK', score=0.613, note='aloalo.csv', probability={'OK':0.715, 'NG':0.135, 'NG1':0.15}  )
        # model_path = self.asset.get_model_path(use_inference_path=False)     
        # report_path = self.asset.get_report_path() 
        # output_path = self.asset.get_output_path()
        ###################################################################################### 

        ## experimental_plan.yaml 에서 작성한 user parameter 를 dict 로 저장
        self.args       = self.asset.load_args()
        self.config     = self.asset.load_config()

        ## Asset 간에 전달해야 정보를 dict 로 저장
        ##  - self.config['new_key'] = 'new_value' 로 next asset 으로 정보 전달 가능 
        ## 이전 step 의 데이터 가져오기
        self.input_data    = self.asset.load_data()['dataframe'].copy()

    @Asset.decorator_run
    def run(self):
        
        ## 데이터 전달하기 
        output_data = self.input_data 

        self.asset.save_data(output_data)
        self.asset.save_config(self.config)
        
if __name__ == "__main__":
    ua = UserAsset(envs={}, argv={}, data={}, config={})
    ua.run()