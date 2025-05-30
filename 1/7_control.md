# 수행 목표
피드백 제어의 개념 및 PID제어에 대해 학습한다.

# 로봇을 제어하는 기초 제어 이론 학습

## 1.제어 시스템의 기초(제어 시스템의 개념과 제어의 목표)
 - 제어 시스템은 원하는 목표 상태를 실현하기 위해 시스템의 동작을 제어하는 시스템이다.  

 - **제어의 목표는 출력이 입력(목표값, 설정값)에 최대한 정확하게 도달하도록 시스템을 조정** 하는 것 이다.   

 - 시스템에서 우리가 원하는 출력을 산출할 수 있도록 적절한 동작신호를 생성하는 방법을 파악하는 것이 중요하다.  

## 2.피드백 제어의 기본 개념(피드백, 목표값 및 오차)
### 2-1. 정의
 - 출력 결과를 실시간으로 측정해서, 원하는 목표값과 비교한 후, 그 **오차를 줄이도록 제어입력을 조절** 하는 제어 방식이다.  
 - 즉 **피드백 제어는 오차를 최소화하는 방향으로 제어 신호를 생성하여 시스템을 조정** 한다.  

### 2-2. 구성요소
  - **목표값(input):** 우리가 원하는 값(목표값)  

  - **센서 측정값(Output):** 실제 로봇이 어디에 있는지 측정한 값  

  - **오차 연산기(Error):** 오차값(목표값-실제값)을 측정한다. 

  - **제어기(Controller):** 오차값을 토대로 입력 신호를 조정한다.
     - 대표적으로 PID 제어기가 있다.  

  - **액추에이터(Actuator):** 제어기에서 받은 신호를 실제 물리적인 운동, 힘, 토크 등으로 변환하는 장치이다.
     - 예시로는 DC모터, 서보모터, 유압 실린더 등이 있다.

  - **플랜트(Plant):** 제어하려는 대상이 되는 전체 시스템 또는 물체이다.
     - 예시로는 바퀴 달린 로봇, 로봇 팔, 드론 등이 있다.

## 3.피드백 제어의 기본 구조(제어 시스템의 구성 요소, 오픈 루프와 클로즈드 루프)

### 3-1. 오픈 루프(Open-Loop)
 - 출력을 측정하지 않고, **미리 정해진 입력만 내보내는 제어 방식** 이다.  
 - **피드백이 없기 때문에 오차를 수정하는 것이 불가능** 하다.  
 - 여러 **외부 요인변화에 대한 대응이 어렵다.**  
 - 사용 예: 세탁기를 1시간 돌리는 경우 옷의 더러움정도나 양을 고려하지 않고 시간에만 맞추어 동작한다.  

### 3-2. 클로즈드 루프(Closed-Loop)
 - **출력 상태를 측정하여 다시 입력으로 사용하는 피드백 루프가 구성** 되어 있다.  
 - 입력으로 들어오는 실제값과 목표값의 차이를 계산하여 오차값을 도출한다.  
 - 도출된 **오차값을 줄여나가며 목표값에 도달** 한다.  

## 4.PID 제어의 개념

### 4-1. PID 제어
 - PID 제어는 제어 대상(플랜트)의 출력을 목표값에 도달하게 하기 위해 사용되는 피드백 제어이다.  
 - 오차값을 바탕으로 **Proportional(비례), Integral(적분), Derivative(미분)** 세 가지 요소를 결합해 제어 입력을 생성한다. 

### 4-2. P(Proportional, 비례제어)
 - 현재에 중점을 둔다.  
 - **현재 오차의 크기에 비례하여 제어**한다. 
 - 즉 오차가 클수록 강하게 제어한다.  
 - 하지만 **정상 상태 오차**로 인해 오차가 0으로 수렴하지 않고, 오차가 약간 남아있을 가능성이 존재한다.

### 4-3. I(Integral, 적분 제어)
 - 과거에 중점을 둔다.  
 - **오차의 누적값을 사용하여 제어**한다.
 - 오차가 계속 남아있으면 그 오차가 점점 더 커지는 효과를 줘서 오차를 0으로 만든다.
 - 따라서 **정상 상태 오차를 제거**하는데 사용된다.  
 - 하지만 너무 크면 과도한 누적으로 인해 **오버슈팅**이 발생하게 되는 단점이 있다.  

### 4-4. D(Derivative, 미분 제어)
 - 미래에 중점을 둔다. 
 - 오차의 **변화율(속도)을 고려하여 예측적 제어**를 한다. 
 - **빠른 변화를 감지해서 예방적으로 제동** 한다. 
 - 따라서 **오버슈팅을 억제** 하는데 사용되고, **급격한 변화를 방지**하여 시스템을 안정화한다.  
 - 하지만 **노이즈에 민감** 하기 때문에 노이즈로 부터 필터를 보호하기 위해 필터링된 미분기가 주로 사용된다.  

## 5.P, I, D 각 항목의 역할과 수학적 표현

### 5-1. P (Proportional, 비례제어)
 - **Up(t)=Kp⋅e(t)**
   - **현재 시간의 오차 e(t)** 에 비례적으로 반응한다.

   - Kp의 게인 값을 조절하여 비례 경로의 세기를 조절한다.

   - **빠른 제어가 가능하지만, 오차가 0에 수렴하지 않을 가능성이 있다.**

### 5-2. I (Integral, 적분 제어)
 - **Ui(t)=Ki⋅∫e(τ)dτ (시간 0에서 t까지 적분)**
   - **과거부터 지금까지의 오차를 누적해서 반영** 하고, 만약 오차가 계속 조금씩 남아있다면 그 누적값을 통해 더 강하게 오차를 보정한다.

   - **∫e(τ)dτ는 오차 면적 또는 누적된 에너지**를 나타낸다.(즉 시간에 따라 오차가 쌓인 정도를 나타낸다.)

   - 비례 제어에서 해결하지 못한 **잔여 오차를 제거할 수 있지만, 너무 커지면 반응이 느려지고 진동을 유발** 할 수 있다.
     - 여기서 **진동이라는 것은 출력이 목표값 근처에서 왔다갔다를 반복하는 현상**을 말한다.

### 5-3. D (Derivative, 미분 제어)
 - **Ud(t)=Kd⋅de(t)/dt**
   - **오차가 어떻게 변화하고 있는지를 반영** 하여 오차가 빠르게 줄어들고 있다면, 제어신호를 약하게 해서 오버슈트(overshoot)를 방지한다.
     - 여기서 **오버슈트라는 것은 목표값을 처음 도달할 때, 너무 많이 넘어서 지나치는 현상**이다.

   - **dt/de(t)는 오차를 시간에 대해 미분한, 즉 오차의 변화율**이다.(즉 미래의 오차 방향을 예측해서 보정한다.)
     - 오차가 **5 --> 5** 로 계속 유지하고 있다면, **de(t)/dt = 0**
     - 오차가 **5 --> 4 --> 3** 으로 줄어들고 있다면, **de(t)/dt < 0**
     - 오차가 **5 --> 6 --> 7** 로 커지고 있다면, **de(t)/dt > 0**

   - **오버슈트, 진동을 억제해서 더 안정된 제어를 할 수 있지만, 센서 노이즈에 매우 민감** 하다.(노이즈가 있으면 미분값이 튄다.)

### 5-4. PID
 - **​U(t)=Kp⋅e(t) + Ki⋅∫e(τ)dτ + Kd⋅de(t)/dt**
   - **U(t):** 제어기에서 출력되는 제어 신호
   - **e(t):** 시간 t에서의 오차(목표값-측정값)
   - **Kp, Ki, Kd:** 각각의 게인 값(비례, 적분, 미분 항의 세기 조절)

## 6.PID 튜닝
 - PID 튜닝은 Kp, Ki, Kd 이 3가지 파라미터의 값을 조정하여 시스템의 정확성, 반응속도, 안정성 등을 최적화 하는 과정이다.

### 6-1. 수동 튜닝
 - 초기값을 잡고 손으로 하나씩 조정하는 방법
   1. **Ki, Kd = 0으로 두고 시작한다.** (우선 Kp만 작동)
   2. **Kp를 서서히 증가시켜 반응을 빠르게 한다.** (너무 크면 진동이 발생한다.)
   3. **Ki를 증가시켜 정상 상태 오차를 제거한다.** (너무 크면 오버슈트와 느린 응답이 발생한다.)
   4. **Kd를 증가시켜 진동과 오버슈트를 억제한다.** (노이즈를 잘 신경써야 한다.)

### 6-2. Ziegler-Nichols 튜닝
 - 실험 기반 자동 튜닝 기법 중 하나 이다.
   1. **Ki, Kd = 0으로 설정하고 시작한다.**
   2. **Kp를 점점 증가시켜  계속 진동만 하는 임계점(Ku)을 찾는다.**
   3. **그때의 진동 주기(Tu) 를 기록한다.**
   4. **만약 Ku = 10, Tu = 2초면 --> Kp = 6, Ki = 6 * 2 = 12, Kd = 6 * 2 / 8 = 1.5 이런식으로 최적의 파리미터를 설정한다.**

### 6-3. 시뮬레이션 기반 튜닝
 - **MATLAB simulink** 같은 툴에서 실제 모델을 시뮬레이션하여 자동 튜닝한다.
 - **Python(control, matplotib패키지)** 으로도 가능하다.

### 6-4. PID 튜닝 목표
 - 빠른 응답 속도  
 - 오버슈트(초과 반응)최소화  
 - 안정적인 제어(진동 최소화)  
 - 목표값 도달 정확도 향상(정상 상태 오차 최소화)  

 ## 7. 질문
 ### Ziegler-Nichols 튜닝에서 임계 이득(Ku)값을 정확하게 찾는 방법이 있는지 알고 싶다.