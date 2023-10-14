# AI Learning Organizer (ALO)


------------
### asset_{step_name}.py 에 제공되는 사용자 API
```python
self.asset.check_args(arg_key, is_required=False, default="", chng_type="str" )
``` 
User parameter 의 type 을 변경하거나, default 값을 변경하기 위해 사용합니다. 
experimental_plan.yaml 에서 Asset 의 user parameter 를 삭제경우에도 정상적인 실행을 위해 필수로 삽입 합니다. 
AI Conductor 로 upload 시, 삽입 여부를 check 합니다. 
- args (dict) : Asset self.args 
- arg_key (str) : 사용자 라미미터 이름 
- is_required (bool) : 필수 존재 여부 
- default (str) : 사용자 파라미터가 존재하지 않을 경우, 강제로 입력될 값
- chng_type (str): 타입 변경 list, str, int, float, bool, 


```python
self.asset.save_summary(result='OK', score=0.613, note='aloalo.csv', probability={'OK':0.715, 'NG':0.135, 'NG1':0.15}  )
``` 
추론 결과를 Edge App 에 전달하여 Display 하기 위해 사용. Edge Conductor 에서는 결과를 누적하여 재학습 필요 여부를 사용자가 선택 하도록 함.AI Conductor 에 등록 시, 함수 사용 여부 체크.

- result (str, length limit: 25) : Inference result summarized info. 
- score (float, 0 ~ 1.0) : model performance score to be used for model retraining 
- note (str, length limit: 100): optional & additional info. for inference result (optional)
- probability (dict - key:str, value:float): Classification Solution의 경우 라벨 별로 확률 값을 제공합니다. (optional) >> (ex) {'OK': 0.6, 'NG':0.4}

```python
model_path = self.asset.get_model_path(use_inference_path=False)     
```
Train pipeline 에서 생성한 모델 파일을 Inference pipeline 에 전달하고 싶을 경우에 사용하며, 동일한 step name (experimental_plan.yaml) 끼리만 전달할 수 있다.  
- use_inference_path (bool, default=False): inference pipeline 진행 시, 생성된 모델을 inference storage 
영역에 저장하고 싶을 때 사용 
---- Return 
-model_path (str): 저장 공간 경로를 반환 한다. 


```python
report_path = self.asset.get_report_path() 
```
Train pipeline 에서 생성한 report.html 을 저장하기 위한 사용. html 파일모델 파일을 Inference pipeline 에 전달하고 싶을 경우에 사용하며, 동일한 step name (experimental_plan.yaml) 끼리만 전달할 수 있다.  

---- Return 
-model_path (str): 저장 공간 경로를 반환 한다. 


```python
output_path = self.asset.get_output_path()
```
Train pipeline 또는 Inference pipeline 실행 결과를 저장할 때 사용한다. 
Inference pipeline 은 output.csv, output.jpg, output.csv & output.jpg 중에 하나를 포함하고 있어야 한다 (필수). Inference 결과는 Model Conductor 로 수집되어 re-train 시 학습데이터롤 사용된다. 

---- Return 
-model_path (str): 저장 공간 경로를 반환 한다.

------------



## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
ALO is Free software, and may be redistributed under the terms of specified in the [LICENSE]() file.

