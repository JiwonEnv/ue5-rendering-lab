# 중심 질문에 따른 편집 기록

내용을 추가하는 방식에서 벗어나, 각 챕터의 질문·설명·그림·실험이 같은 원리를 향하도록 다시 편집했습니다.

| 챕터 | PDF 시작 쪽 | 중심 질문 |
|---|---:|---|
| [CH01](Chapters/CH01_RenderingPipeline.md) | 4 | 같은 장면인데 왜 진단 화면마다 보이는 것이 다를까? |
| [CH02](Chapters/CH02_ForwardDeferred.md) | 10 | 왜 렌더러를 바꾸면 같은 에셋의 표현과 비용 조건이 달라질까? |
| [CH03](Chapters/CH03_GBuffer.md) | 12 | 벽이 번들거릴 때 왜 최종 색보다 Roughness 화면을 먼저 볼까? |
| [CH04](Chapters/CH04_DBufferDecals.md) | 14 | 데칼은 왜 벽 그림처럼 빛에 반응하고, 옆 소품에도 묻을까? |
| [CH05](Chapters/CH05_DepthEarlyZ.md) | 16 | 앞에 벽이 있으면 뒤의 비싼 재질 계산도 하지 않을까? |
| [CH06](Chapters/CH06_Overdraw.md) | 18 | 삼각형을 줄인 풀 카드가 왜 더 느릴 수 있을까? |
| [CH07](Chapters/CH07_PBR.md) | 20 | 조명을 바꿔도 금속과 페인트가 재료답게 보이려면 무엇을 입력해야 할까? |
| [CH08](Chapters/CH08_BRDF.md) | 22 | 같은 밝기의 재질인데 왜 하이라이트의 폭과 모양이 다를까? |
| [CH09](Chapters/CH09_Fresnel.md) | 24 | 물이나 유리는 왜 비스듬히 볼 때 반사가 강해질까? |
| [CH10](Chapters/CH10_ShadersWPO.md) | 26 | 재질에서 풀을 흔들면 왜 형상과 그림자가 함께 달라질까? |
| [CH11](Chapters/CH11_Substrate.md) | 28 | 페인트 위 투명 코팅은 왜 두 재질의 색을 섞는 것만으로 충분하지 않을까? |
| [CH12](Chapters/CH12_TranslucencyRefraction.md) | 30 | 유리판을 겹치면 왜 불투명 벽과 다른 오류가 생길까? |
| [CH13](Chapters/CH13_SubsurfaceScattering.md) | 32 | 왁스는 왜 두께와 역광에 따라 색과 밝기가 달라질까? |
| [CH14](Chapters/CH14_DrawCalls.md) | 34 | 소품 하나인데 왜 여러 번 그리는 명령이 생길까? |
| [CH15](Chapters/CH15_Instancing.md) | 36 | 같은 기둥 수백 개를 왜 개별 Actor 대신 인스턴스로 관리할까? |
| [CH16](Chapters/CH16_LOD.md) | 38 | 먼 난간의 나사는 왜 생략해도 되지만 윤곽은 남겨야 할까? |
| [CH17](Chapters/CH17_Nanite.md) | 40 | Nanite는 원본의 수많은 삼각형을 매번 모두 그릴까? |
| [CH18](Chapters/CH18_Culling.md) | 42 | 건물을 한 덩어리로 합치면 왜 벽 뒤 부분까지 처리할 수 있을까? |
| [CH19](Chapters/CH19_Mipmaps.md) | 44 | 먼 바닥의 잔무늬는 왜 고해상도 원본만 쓰면 더 흔들릴까? |
| [CH20](Chapters/CH20_TextureStreaming.md) | 46 | 텍스처 원본은 선명한데 게임에서는 왜 잠시 흐리게 보일까? |
| [CH21](Chapters/CH21_Lumen.md) | 48 | 직접 빛이 닿지 않는 흰 벽은 왜 주변 벽의 색을 띨까? |
| [CH22](Chapters/CH22_VirtualShadowMaps.md) | 50 | 바람 부는 풀밭은 왜 카메라가 멈춰도 그림자 작업이 생길까? |
| [CH23](Chapters/CH23_TAA.md) | 52 | 철망의 깜빡임을 줄였는데 왜 움직일 때 잔상이 생길까? |
| [CH24](Chapters/CH24_TSR.md) | 54 | 낮은 내부 해상도로 그려도 어떻게 높은 출력 해상도를 만들까? |
| [CH25](Chapters/CH25_CPUGPUBottlenecks.md) | 56 | 폴리곤과 해상도를 줄였는데 왜 FPS가 그대로일까? |
| [CH26](Chapters/CH26_GPUProfiling.md) | 58 | 무거운 GPU 패스를 찾은 다음 어떻게 수정 효과를 증명할까? |

## 범위 조정

- CH01은 14쪽에서 6쪽으로 편집했습니다. 좌표·래스터화·표면과 조명·Bloom의 인과 흐름을 남기고 상세 캡처는 별도 기록으로 보존했습니다.
- CH10은 정점 변형에 초점을 맞추고 순열·컴파일·쿠킹은 심화로 옮겼습니다.
- CH11은 단일 혼합과 물질 적층, CH13은 내부 산란 경로, CH17은 화면 오차와 세부 선택을 설명하는 도식으로 교체했습니다.
- CH21의 반사 모드 비교를 간접광 현상으로, CH23의 정지 AA 비교를 히스토리 대응 과정으로 교체했습니다.
- GBuffer의 재질 진단과 해상도별 비용 실험을 분리했습니다. 본문은 입력과 조명 결과의 구분에 집중합니다.
- 모든 실습에 예상 결과와 이유를 적고, 실제 제작의 선택과 예외를 뒤에 배치했습니다.
- 이전 외부 그림의 원본과 출처는 삭제하지 않고 참고 자료로 보관합니다. 본문 삽입 수를 품질 목표로 삼지 않습니다.

기존 PDF와 DOCX를 같은 이름으로 갱신했습니다. CH02–26의 실제 특화 예제 제작과 성능 측정은 별도 작업입니다.
