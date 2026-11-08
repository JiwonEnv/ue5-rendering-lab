# CH01 렌더링 파이프라인

## 중심 질문

같은 장면인데 왜 진단 화면마다 보이는 것이 다를까?

## 먼저 알아둘 답

최종 화면은 한 번에 그린 사진이 아니라, 형태·표면·빛·합성의 결과를 이어 만든 이미지입니다.

## 왜 알아야 할까

화면이 이상할 때 메시, 재질, 조명, 후처리 중 어디를 먼저 조사할지 정하기 위해 배웁니다.

### 예제 학습 목표

Bloom을 바꾸는 실험으로 최종 번짐과 기본 표면 입력을 구분합니다.

**구현 상태 — 실제 엔진 씬과 캡처 제공**

레벨 `/Game/RenderingLab/Chapters/Part01_RenderingBasics/CH01_RenderingPipeline/Maps/L_CH01_RenderingPipeline`

## 왜 이런 결과가 생길까

CPU는 장면 상태를 바탕으로 그릴 작업을 준비하고 GPU는 그 명령에 따라 계산합니다. 먼저 메시의 정점 위치를 카메라 화면에 대응시키고, 삼각형이 덮는 위치를 찾습니다. 그 위치의 표면 정보에 빛과 그림자를 반영하고, 유리 같은 표면과 화면 효과를 합쳐 최종 색을 만듭니다.

## 제작 중에는 이렇게 나타납니다

따라서 최종 색이 밝다는 사실만으로 Base Color가 밝다고 판단할 수 없습니다. 조명이나 발광, Bloom이 밝게 보이게 했을 수도 있습니다. 진단 화면은 이 중 특정 정보만 꺼내 보여 주므로 서로 다르게 보이는 것이 정상입니다.

## 모델에서 화면까지

지오메트리는 형태와 위치를 정하는 기하 정보입니다. 메시의 삼각형 꼭짓점이 정점입니다. GPU의 정점 셰이더는 모델 내부 위치에 배치와 카메라 변환을 적용해 화면 위치를 구합니다. UV는 텍스처 위치를, 법선은 표면 방향을 나타냅니다.

![외부 참고 그림 · 모델의 로컬 공간부터 월드·카메라·클립·화면 공간까지 이어지는 좌표 변환입니다.](../Images/External/coordinates-print.png)

외부 참고 그림 · 모델의 로컬 공간부터 월드·카메라·클립·화면 공간까지 이어지는 좌표 변환입니다.

읽을 곳  1→2에서는 큐브를 장면에 배치하고, 2→3에서는 카메라를 기준으로 장면을 해석합니다. 4→5에서는 투영한 결과가 화면 영역에 대응합니다. UE와 OpenGL의 축·깊이 규약은 같지 않지만 좌표 기준을 바꾸는 목적은 같습니다.

[© Joey de Vries · LearnOpenGL · @JoeyDeVriez · 출처 37](https://learnopengl.com/Getting-started/Coordinate-Systems)

원본 전체와 비율 유지

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

래스터화는 화면의 삼각형이 어느 샘플 위치를 덮는지 찾는 과정입니다. 보간은 꼭짓점의 알려진 값으로 내부 위치의 UV 같은 중간값을 구하는 것입니다. 무늬의 세밀함과 실루엣의 세밀함을 구분할 수 있는 이유입니다.

![외부 비교 그림 · 삼각형과 화면 격자, 그리고 포함 판정을 표시한 결과를 나란히 배치했습니다.](../Images/External/raster-print.png)

외부 비교 그림 · 삼각형과 화면 격자, 그리고 포함 판정을 표시한 결과를 나란히 배치했습니다.

읽을 곳  왼쪽의 매끈한 삼각형 경계와 오른쪽의 격자에 맞춘 계단형 경계를 비교합니다. 이 그림은 래스터화와 앨리어싱의 관계를 설명하며 TAA 또는 TSR의 전후 결과가 아닙니다.

[© Joey de Vries · LearnOpenGL · @JoeyDeVriez · 출처 38](https://learnopengl.com/Advanced-OpenGL/Anti-Aliasing)

원본 전체와 비율 유지

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 준비와 실행

스레드는 명령을 이어 실행하는 흐름입니다. 게임 스레드는 상태를 갱신하고 렌더 스레드는 CPU에서 그릴 명령을 준비합니다. RHI는 Render Hardware Interface로 명령을 그래픽 API에 연결하는 계층입니다. GPU는 제출된 작업을 실행합니다. 버퍼는 작업 데이터를 보관하는 메모리이며, 패스는 계산을 나눠 수행하는 단위입니다.

표면과 깊이를 준비하고 빛·그림자를 반영한 뒤 반투명과 후처리를 합쳐 최종 색을 만듭니다. 실제 실행은 분기와 병렬 작업을 포함합니다.

![표면색 진단](../Images/CH01/02_BaseColor.png)

![조명 기여 진단](../Images/CH01/10_LightingOnly.png)

직접 제작·실제 엔진의 같은 카메라 캡처. Base Color와 Lighting Only는 서로 다른 진단이며 두 화면을 더하는 단순 분해식은 아닙니다.

## 실습 절차

CH01 쇼윈도에서 같은 카메라를 유지합니다. Lit와 Base Color를 먼저 비교한 뒤 Bloom만 끄고 Lit와 Base Color를 다시 봅니다. 노출과 재질 값은 그대로 둡니다.

## 예상 결과와 이유

Bloom을 끄면 밝은 바 주변의 번짐이 줄어들지만, 기본 표면색은 같은 상태로 남을 것입니다. 이는 화면 뒤쪽 단계의 변화가 앞쪽 표면 입력을 바꾸지 않는다는 예상입니다.

## 결과를 어떻게 해석할까

번짐과 표면색이 함께 바뀌면 Bloom 외의 설정이나 노출이 달라졌는지 먼저 확인합니다. 진단 화면이 달라진 이유를 찾는 것이 이번 실습의 목적이며, 이 비교만으로 성능 향상까지 판단하지 않습니다.

## 실제 제작에서의 선택

입력 표면색부터 이상하면 재질을, 표면색은 정상인데 최종 밝기만 이상하면 조명·노출·후처리를 다음 조사 대상으로 고릅니다.

## 이해한 뒤 확인할 조건

본문의 순서는 대표적인 의존 관계입니다. 실제 GPU 실행에는 그림자 등 별도 작업이 있으며 일부 작업은 겹쳐 진행됩니다. Nanite의 세부 지오메트리 경로는 CH17에서 다룹니다.

![Bloom 적용](../Images/CH01/01_Lit.png)

![Bloom 해제](../Images/CH01/08_BloomOff.png)

직접 제작·같은 카메라의 실제 엔진 비교. 밝은 바 주변의 번짐을 확인합니다. 캡처 중 시간은 일반 성능 측정값이 아닙니다.

[상세 캡처와 제작 기록](../Reference/CH01_CaptureAtlas.md) · [촬영 조건](../Images/CH01/CaptureManifest.json)

## 공식 자료와 확장

- [Rendering Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-settings-in-the-unreal-engine-project-settings)
- [Render Dependency Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-dependency-graph-in-unreal-engine)
- [Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
