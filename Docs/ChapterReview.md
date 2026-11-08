# 블로그 포스트 형식 편집 기록

문서를 강의 자료에서 독립된 블로그 포스트 모음으로 편집했습니다. 개념의 정의와 전체 역할은 본문에 유지하고, 주제별 도입·소제목·서술형 제작 사례·자연스러운 맺음으로 연결했습니다.

| 포스트 | PDF 시작 쪽 | 제목 |
|---|---:|---|
| [01](Chapters/CH01_RenderingPipeline.md) | 3 | 렌더링 파이프라인 장면이 이미지가 되기까지 |
| [02](Chapters/CH02_ForwardDeferred.md) | 8 | Forward와 Deferred 조명 계산의 차이 |
| [03](Chapters/CH03_GBuffer.md) | 10 | GBuffer 최종 색 뒤에 있는 표면 정보 |
| [04](Chapters/CH04_DBufferDecals.md) | 12 | DBuffer 데칼은 벽의 무엇을 바꾸는가 |
| [05](Chapters/CH05_DepthEarlyZ.md) | 14 | Depth와 Early Z 가려진 표면의 계산은 언제 멈출까 |
| [06](Chapters/CH06_Overdraw.md) | 16 | Overdraw 삼각형이 적은 풀이 더 느릴 수 있는 이유 |
| [07](Chapters/CH07_PBR.md) | 18 | PBR 조명이 바뀌어도 재료답게 보이는 표면 |
| [08](Chapters/CH08_BRDF.md) | 20 | BRDF 하이라이트의 모양은 어디에서 오는가 |
| [09](Chapters/CH09_Fresnel.md) | 22 | Fresnel 물과 유리의 반사가 각도에 따라 달라지는 이유 |
| [10](Chapters/CH10_ShadersWPO.md) | 24 | 셰이더와 머티리얼 그래프는 어떻게 화면 계산이 될까 |
| [11](Chapters/CH11_Substrate.md) | 26 | Substrate 재료를 섞는 것과 층을 쌓는 것의 차이 |
| [12](Chapters/CH12_TranslucencyRefraction.md) | 28 | Translucency 유리가 불투명 벽보다 까다로운 이유 |
| [13](Chapters/CH13_SubsurfaceScattering.md) | 30 | SSS 왁스와 돌의 내부에서 일어나는 빛의 변화 |
| [14](Chapters/CH14_DrawCalls.md) | 32 | Draw Call 소품 하나가 여러 그리기 작업이 되는 이유 |
| [15](Chapters/CH15_Instancing.md) | 34 | Instancing 반복되는 배치에서 무엇을 공유할까 |
| [16](Chapters/CH16_LOD.md) | 36 | LOD 멀리서도 남겨야 하는 디테일은 무엇일까 |
| [17](Chapters/CH17_Nanite.md) | 38 | Nanite 원본 디테일과 화면의 삼각형 수가 다른 이유 |
| [18](Chapters/CH18_Culling.md) | 40 | Culling 보이지 않는 배경을 언제 제외할까 |
| [19](Chapters/CH19_Mipmaps.md) | 42 | Mipmap 먼 텍스처는 왜 덜 세밀해야 안정적일까 |
| [20](Chapters/CH20_TextureStreaming.md) | 44 | Texture Streaming 선명한 원본이 잠시 흐리게 보이는 이유 |
| [21](Chapters/CH21_Lumen.md) | 46 | Lumen 표면 사이를 이동하는 빛을 계산하는 방법 |
| [22](Chapters/CH22_VirtualShadowMaps.md) | 48 | Virtual Shadow Maps 선명한 그림자와 캐시의 관계 |
| [23](Chapters/CH23_TAA.md) | 50 | TAA 과거 프레임이 경계를 안정시키고 잔상을 만드는 이유 |
| [24](Chapters/CH24_TSR.md) | 52 | TSR 내부 해상도와 출력 해상도 사이의 재구성 |
| [25](Chapters/CH25_CPUGPUBottlenecks.md) | 54 | CPU와 GPU 병목 가벼워진 에셋이 FPS를 올리지 못할 때 |
| [26](Chapters/CH26_GPUProfiling.md) | 56 | GPU Profiler 프레임의 비용을 읽는 법 |

## 편집 범위

- 학습 목표, 예제 목표, 실습 절차, 예상 결과, 결과 해석 과제와 종합 과제를 원고에서 제거했습니다.
- 무엇인가·역할·입력과 출력 같은 반복 항목명을 주제에 맞는 소제목과 연결된 문단으로 바꿨습니다.
- 메뉴 조작과 설정 변경 지시는 제작 상황을 설명하는 사례로 다시 썼습니다.
- 기존 비교 캡처는 현상을 보여 주는 이미지로 유지하고, 새로운 실측이나 구현으로 표시하지 않습니다.
- 기존 언리얼 레벨과 도구, 과거 촬영 기록은 원고와 별도로 보존했습니다.
