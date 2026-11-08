# CH15 Instancing과 반복 배치

## 무엇인가

Instancing은 공통 메시 같은 데이터를 공유하면서 위치·회전·크기 등의 배치별 정보를 따로 두어 여러 복사본을 처리하는 방식입니다. 같은 형상을 반복하는 데 적합한 데이터·실행 구조입니다.

## 렌더링에서 맡는 역할

반복 오브젝트를 개별적으로 관리하고 제출하는 부담을 줄일 수 있습니다. 여러 복사본이 보이는 사실 자체를 없애는 것이 아니라 중복 데이터와 준비를 공유하는 역할입니다.

## 입력과 출력

입력은 공통 메시·재질과 인스턴스별 Transform 등입니다. 이를 이용해 각 위치에 복사본을 표시하며 각 복사본의 가시 형상과 픽셀은 여전히 처리합니다.

## 작동 과정

공통 형상과 재질을 준비합니다. Transform은 위치·회전·크기의 변환 정보이며 같은 형상을 장면의 다른 위치에 배치하게 합니다.

ISM은 반복 배치를 하나의 Instanced Static Mesh Component에서 관리합니다. 인스턴스별 색 같은 변주는 공유 재질에서 별도의 배치별 데이터로 읽을 수 있습니다.

렌더러가 인스턴스의 가시성과 실행 조건을 고려해 처리합니다. HISM은 공간 계층을 사용하는 확장이며 갱신·LOD·컬링 조건에 따라 적합성이 달라집니다.

![외부 렌더 이미지 · 공통 사각형을 인스턴싱하면서 배치별 위치와 크기를 달리한 예입니다.](../Images/External/instance-data-print.png)

외부 렌더 이미지 · 공통 사각형을 인스턴싱하면서 배치별 위치와 크기를 달리한 예입니다.

읽을 곳  같은 기본 형상을 공유해도 복사본마다 변환 정보가 다릅니다. OpenGL 학습 예시이며 UE ISM의 호출 수나 속도를 측정한 자료는 아닙니다. 외관을 유지하며 제출 비용이 줄었는지는 목표 장면에서 검증합니다.

[© Joey de Vries · LearnOpenGL · @JoeyDeVriez · 출처 52](https://learnopengl.com/Advanced-OpenGL/Instancing)

원본 전체 유지 · 투명 배경은 흰색으로 표시

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 왜 배경 제작에 필요한가

울타리 기둥·식생·가로등·군집 소품처럼 같은 형상이 반복될 때 필요합니다. 배치마다 독립 재질을 만드는 대신 공통 데이터와 개별 변주를 나눠 설계합니다.

## 성능과 제작 비용

관리·제출 부담을 줄일 수 있지만 정점·픽셀·그림자와 위치 갱신은 남습니다. 자동 묶음과 Nanite 조건에 따라 제출 이득은 달라질 수 있습니다.

## 원리 확인 예제

이 예제는 위에서 설명한 주제의 일부 관계를 확인합니다. 특정 예제가 기술 전체의 정의나 유일한 사용 목적은 아닙니다.

### 예제 학습 목표

동일 반복 배치를 개별 Actor와 ISM으로 관리할 때의 차이를 확인합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part03_GeometryAndTextures/CH15_Instancing/Maps/L_CH15_Instancing`

### 실습 절차

같은 메시·재질의 기둥 200개를 개별 Actor로 둔 버전과 ISM으로 둔 버전을 준비합니다. 배치·충돌·그림자를 맞추고 같은 카메라에서 Actor·컴포넌트 구성과 CPU·GPU 시간을 비교합니다.

### 예상 결과와 이유

ISM에서는 독립적으로 관리할 Actor·컴포넌트 수가 줄 것입니다. CPU 관리나 제출이 문제였던 장면이라면 그 구간의 개선을 기대할 수 있습니다.

### 결과를 어떻게 해석할까

GPU 픽셀 비용이 지배하면 전체 프레임 변화는 작을 수 있습니다. 엔진의 자동 인스턴싱 때문에 제출 차이가 작아도 데이터 관리 방식의 차이는 남습니다.

## 이 챕터에서 기억할 것

인스턴싱은 공통 데이터를 공유하는 반복 처리입니다. 복사본의 화면 계산까지 한 번으로 사라지는 것은 아닙니다.

## 이해한 뒤 확인할 조건

HISM은 공간 계층을 사용하는 확장입니다. 잦은 위치 갱신과 컬링·LOD·Nanite 조건에 따라 선택이 달라지므로 별도 성능 과제로 다룹니다.

## 공식 자료와 확장

- [Mesh Drawing Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-drawing-pipeline-in-unreal-engine)
- [Instanced Static Mesh Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-static-mesh-component-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
