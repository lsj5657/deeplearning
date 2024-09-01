**지능형 LPMS 프로젝트 (리얼게인 현장실습)**

이 프로젝트는 주식회사 리얼게인에서 진행한 현장실습 중 개발된 지능형 LPMS (Loose Part Monitoring System) 시스템입니다. 이 시스템은 AI를 활용하여 산업 현장에서 발생할 수 있는 금속 이물질 충격을 실시간으로 감지하고 분석하는 것을 목표로 합니다.

**프로젝트 기능**

**-AI Decision 탭:**

폴더 지정 및 데이터 처리: 사용자가 bin 파일이 포함된 폴더를 지정하면, 각 bin 파일에서 이벤트 채널의 시계열 데이터를 읽어들입니다.
STFT 이미지 생성 및 AI 판단: 이벤트 채널의 시계열 데이터를 기반으로 STFT(Short-Time Fourier Transform) 이미지를 생성하고, AI 모델을 통해 충격 / 비충격 여부를 판단합니다.

결과 저장: 분석 결과를 요약하여 excel 파일로 저장합니다.

**-Analysis 탭:**

데이터 확인: Excel 파일에 저장된 요약 정보를 시각적으로 확인할 수 있는 기능을 제공합니다. 이를 통해 각 bin 파일의 처리 결과를 손쉽게 검토할 수 있습니다.

이 프로젝트에서 저는 **CNN(Convolutional Neural Network)**을 이용하여 충격 / 비충격 이미지를 판단하는 AI 모델 개발을 담당하였습니다. 해당 모델은 생성된 STFT 이미지를 분석하여, 금속 이물질 충격 여부를 정확하게 예측하는 역할을 합니다.

시연영상

![LPMS simulation](https://github.com/user-attachments/assets/5ef19650-6dfc-43a4-ba59-5ef795c42939)
