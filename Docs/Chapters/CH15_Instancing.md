# Instancing 반복되는 배치에서 무엇을 공유할까

울타리 기둥 수백 개는 형상보다 위치가 다릅니다. 그 공통점과 차이를 데이터 구조에 반영하는 방식이 인스턴싱입니다. 반복되는 물체를 각각 완전히 독립된 대상으로 다루지 않아도 되는 이유가 여기에 있습니다.

Instancing은 공통 메시 같은 데이터를 공유하면서 위치·회전·크기 등의 배치별 정보를 따로 두어 여러 복사본을 처리하는 방식입니다. 같은 형상을 반복하는 데 적합한 데이터·실행 구조입니다.

반복 오브젝트를 개별적으로 관리하고 제출하는 부담을 줄일 수 있습니다. 여러 복사본이 보이는 사실 자체를 없애는 것이 아니라 중복 데이터와 준비를 공유하는 역할입니다.

## 공통 형상과 배치별 정보를 나누는 구조

공통 메시와 재질에 각 배치의 Transform이 더해져 여러 위치의 복사본이 됩니다. 형상 데이터는 공유해도 각 위치에서 보이는 삼각형과 픽셀은 여전히 처리해야 합니다.

공통 형상과 재질을 준비합니다. Transform은 위치·회전·크기의 변환 정보이며 같은 형상을 장면의 다른 위치에 배치하게 합니다. ISM은 반복 배치를 하나의 Instanced Static Mesh Component에서 관리합니다. 인스턴스별 색 같은 변주는 공유 재질에서 별도의 배치별 데이터로 읽을 수 있습니다. 렌더러가 인스턴스의 가시성과 실행 조건을 고려해 처리합니다. HISM은 공간 계층을 사용하는 확장이며 갱신·LOD·컬링 조건에 따라 적합성이 달라집니다.

![외부 인스턴스 배열은 공통 형상에 배치별 정보를 더하는 한 사례입니다. 화면의 복사본을 모두 한 번만 셰이딩한다는 뜻은 아닙니다.](../Images/External/instance-data-print.png)

외부 인스턴스 배열은 공통 형상에 배치별 정보를 더하는 한 사례입니다. 화면의 복사본을 모두 한 번만 셰이딩한다는 뜻은 아닙니다.

[© Joey de Vries · LearnOpenGL · @JoeyDeVriez · 출처 52](https://learnopengl.com/Advanced-OpenGL/Instancing)

원본 전체 유지 · 투명 배경은 흰색으로 표시

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 같은 기둥에 다른 색을 주는 방법

울타리 기둥·식생·가로등·군집 소품처럼 같은 형상이 반복될 때 필요합니다. 배치마다 독립 재질을 만드는 대신 공통 데이터와 개별 변주를 나눠 설계합니다.

인스턴스별 색 변화는 메시와 재질을 매번 새로 만들지 않고 배치별 데이터로 전달할 수 있습니다. 공통 재질이 그 값을 읽으면 형상과 계산 구조를 공유하면서도 변주가 생깁니다. 반복 배치의 효율과 화면의 다양성이 반드시 반대인 것은 아닙니다.

## 공유해도 복사본의 픽셀은 남는다

관리·제출 부담을 줄일 수 있지만 정점·픽셀·그림자와 위치 갱신은 남습니다. 자동 묶음과 Nanite 조건에 따라 제출 이득은 달라질 수 있습니다.

인스턴싱의 중심은 복사본을 없애는 것이 아니라 공유할 부분을 정확하게 나누는 데 있습니다. 공통 데이터와 개별 상태를 분리하면 배경의 반복을 관리하는 방식도 달라집니다.

## 참고 자료

- [Mesh Drawing Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-drawing-pipeline-in-unreal-engine)
- [Instanced Static Mesh Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-static-mesh-component-in-unreal-engine)

[포스트 목록](../../README.md#포스트-목록) · [용어 찾아보기](../Glossary.md) · [이미지 출처](../Images/Sources.md)
