# 이미지 출처와 편집 기록

현재 본문은 중심 질문에 맞는 그림을 선별해 사용합니다. 아래에는 사용 중인 자료와 이전 판에서 보관한 자료의 원본 기록을 모두 남깁니다.

CH01의 원본 12장은 이 프로젝트에서 직접 촬영했습니다. 외부 사례는 이 프로젝트의 실행 결과나 성능 보장으로 사용하지 않습니다.

## 직접 제작한 엔진 캡처와 도식

`CH01/CaptureManifest.json`에 촬영 조건과 원본 해시가 있습니다. `Concepts/explain-foundations.png`는 CPU·GPU 역할을 설명하는 자체 개념도입니다.

## 현재 본문에서 쓰는 그림

- CH01 실제 CH01 캡처, coordinates와 raster 외부 설명도
- CH02 직접 제작 개념도 `Focused/focus-02.png`
- CH03 외부 자료 `gbuffer-print.png`
- CH04 외부 자료 `decal-print.png`
- CH05 외부 자료 `depth-print.png`
- CH06 외부 자료 `overdraw-print.png`
- CH07 외부 자료 `pbr-print.png`
- CH08 외부 자료 `brdf-print.png`
- CH09 외부 자료 `fresnel-print.png`
- CH10 직접 제작 개념도 `Focused/focus-10.png`
- CH11 직접 제작 개념도 `Focused/focus-11.png`
- CH12 직접 제작 개념도 `Focused/focus-12.png`
- CH13 직접 제작 개념도 `Focused/focus-13.png`
- CH14 직접 제작 개념도 `Focused/focus-14.png`
- CH15 외부 자료 `instance-data-print.png`
- CH16 외부 자료 `lod-print.png`
- CH17 직접 제작 개념도 `Focused/focus-17.png`
- CH18 직접 제작 개념도 `Focused/focus-18.png`
- CH19 외부 자료 `mipmap-print.png`
- CH20 외부 자료 `streaming-stats-print.png`
- CH21 Cornell box 외부 렌더, Public domain, 원본 전체·비율·색상 유지
- CH22 외부 자료 `vsm-cache-print.png`
- CH23 직접 제작 개념도 `Focused/focus-23.png`
- CH24 외부 자료 `tsr-output-print.png`
- CH25 외부 자료 `cpu-frames-print.png`
- CH26 외부 자료 `gpu-events-print.png`

## 보관한 외부 그림과 원본 기록

보관한 외부 그림 28개에 원본 출처·저자·편집 기록을 붙였습니다. 각 그림의 이용 조건은 저장소 전체의 라이선스와 구별합니다.

### coordinates · 출처 37

외부 참고 그림 · 모델의 로컬 공간부터 월드·카메라·클립·화면 공간까지 이어지는 좌표 변환입니다.

읽을 곳  1→2에서는 큐브를 장면에 배치하고, 2→3에서는 카메라를 기준으로 장면을 해석합니다. 4→5에서는 투영한 결과가 화면 영역에 대응합니다. UE와 OpenGL의 축·깊이 규약은 같지 않지만 좌표 기준을 바꾸는 목적은 같습니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문](https://learnopengl.com/Getting-started/Coordinate-Systems)
- 문서 삽입 파일 `External/coordinates-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 흰색으로 표시했습니다.

### projection · 출처 37

외부 비교 이미지 · 같은 형상의 투영 방식 비교입니다. 왼쪽 Perspective(원근), 오른쪽 Orthographic(직교)입니다.

읽을 곳  왼쪽은 뒤로 갈수록 크기와 간격이 작아 보입니다. 오른쪽은 깊이에 따른 크기 변화가 없어 평행한 방향을 읽기 쉽습니다. 투영 방식의 비교이며 UE의 캡처가 아닙니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문](https://learnopengl.com/Getting-started/Coordinate-Systems)
- 문서 삽입 파일 `External/projection-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 흰색으로 표시했습니다.

### raster · 출처 38

외부 비교 그림 · 삼각형과 화면 격자, 그리고 포함 판정을 표시한 결과를 나란히 배치했습니다.

읽을 곳  왼쪽의 매끈한 삼각형 경계와 오른쪽의 격자에 맞춘 계단형 경계를 비교합니다. 이 그림은 래스터화와 앨리어싱의 관계를 설명하며 TAA 또는 TSR의 전후 결과가 아닙니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문](https://learnopengl.com/Advanced-OpenGL/Anti-Aliasing)
- 문서 삽입 파일 `External/raster-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 2점을 나란히 배치하고 상단 표제만 추가했습니다.

### deferred · 출처 39

외부 참고 그림 · Geometry Pass에서 얻은 여러 표면 버퍼를 Lighting Pass에서 사용합니다.

읽을 곳  가운데 버퍼의 위치·법선·색 정보가 오른쪽의 조명 결과에 어떻게 모이는지 봅니다. OpenGL 학습용 구현이므로 UE의 실제 GBuffer 배치와 동일하다고 해석하지 않습니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문](https://learnopengl.com/Advanced-Lighting/Deferred-Shading)
- 문서 삽입 파일 `External/deferred-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 흰색으로 표시했습니다.

### gbuffer · 출처 39

외부 시각화 이미지 · 같은 장면의 위치·법선·Albedo·Specular를 분리해 표시한 GBuffer 예시입니다.

읽을 곳  왼쪽 위는 위치에 따라, 오른쪽 위는 표면 방향에 따라 색이 달라집니다. 아래쪽은 재질의 색과 반사 입력입니다. 진단용 색을 최종 외관이나 UE 채널 구성으로 읽지 않습니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문](https://learnopengl.com/Advanced-Lighting/Deferred-Shading)
- 문서 삽입 파일 `External/gbuffer-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 흰색으로 표시했습니다.

### pbr · 출처 40

외부 렌더 이미지 · 금속성과 거칠기를 달리한 구들을 두 시점에서 비교합니다.

읽을 곳  오른쪽 배열의 가로 방향에서 거칠기가 변할 때 작은 반사점이 넓어지는 모습을 봅니다. 세로 방향의 금속성 변화도 함께 비교합니다. UE와 광원·톤매핑이 같은 비교 자료는 아닙니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문](https://learnopengl.com/PBR/Lighting)
- 문서 삽입 파일 `External/pbr-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 흰색으로 표시했습니다.

### brdf · 출처 41

외부 개념도 · 미세한 표면 방향의 차이가 반사광의 퍼짐에 영향을 주는 모습입니다.

읽을 곳  거친 표면에서는 여러 방향으로, 매끈한 표면에서는 더 모인 방향으로 반사하는 차이를 봅니다. 확대된 개념도이며 실제 메시의 모든 미세 면을 직접 만드는 뜻은 아닙니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문](https://learnopengl.com/PBR/Theory)
- 문서 삽입 파일 `External/brdf-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 흰색으로 표시했습니다.

### fresnel · 출처 41

외부 시각화 이미지 · 구의 중심과 실루엣 부근에서 Fresnel 반사 계수가 달라지는 예입니다.

읽을 곳  중심보다 테두리가 밝습니다. 곡면의 테두리에서 시선이 표면에 더 비스듬하게 닿기 때문입니다. 물체의 완성 렌더가 아닌 반사 계수의 시각화입니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문](https://learnopengl.com/PBR/Theory)
- 문서 삽입 파일 `External/fresnel-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 흰색으로 표시했습니다.

### translucency · 출처 41

외부 개념도 · 입사한 빛이 표면에서 반사되거나 내부로 들어가 산란·흡수될 수 있습니다.

읽을 곳  표면에서 되돌아가는 경로와 내부로 들어가는 경로를 구분합니다. 이 개념만으로 UE 반투명 구현이 물질 내부의 모든 광선을 추적한다고 해석하지 않습니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문](https://learnopengl.com/PBR/Theory)
- 문서 삽입 파일 `External/translucency-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 흰색으로 표시했습니다.

### lod · 출처 42

외부 비교 그림 · 비슷한 실루엣을 더 적은 변으로 근사한 세 가지 LOD입니다.

읽을 곳  오른쪽으로 갈수록 위쪽 윤곽이 각지게 바뀝니다. 원본의 LOD 1·2·3 표기는 해당 그림의 번호이며 UE에서 흔히 시작하는 LOD0 번호와 구별합니다.

- 저자 Sirotk · Wikimedia Commons
- [원문](https://commons.wikimedia.org/wiki/File:LOD_Example.png)
- 문서 삽입 파일 `External/lod-print.png`
- [이용 조건 CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 흰색으로 표시했습니다.

### nanite · 출처 45

Epic 공식 비교 이미지 · Nanite Clusters 시각화에서 Preserve Area를 끈 상태와 켠 상태입니다.

읽을 곳  왼쪽의 검게 비어 보이는 잎 사이 공간과 오른쪽의 더 조밀한 수관을 비교합니다. 삼각형을 줄일 때 소실되는 잎 면적을 보존하는 사례입니다. 색은 재질색이 아닌 클러스터 구분이며 UE 5.5 문서의 예시로, 이 프로젝트의 UE 5.8 실측이나 성능 비교가 아닙니다.

- 저자 © Epic Games · UE 5.5 공식 문서
- [원문](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.5)
- 문서 삽입 파일 `External/nanite-print.png`
- 원저작권은 Epic Games에 귀속됩니다. 별도의 공개 라이선스를 부여하지 않습니다.
- 편집 원본 2점을 나란히 배치하고 상단 표제만 추가했습니다.

### mipmap · 출처 43

외부 실제 렌더 비교 · 왼쪽 No MipMapping, 오른쪽 With MipMapping입니다.

읽을 곳  수평선에 가까운 먼 바닥에서 왼쪽의 물결무늬와 오른쪽의 안정된 패턴을 비교합니다. 원본은 Blender 렌더이며 필터링도 관여할 수 있으므로 UE에서 밉만 바꾼 통제 실험으로 해석하지 않습니다.

- 저자 BillyBob CornCob · Wikimedia Commons
- [원문](https://commons.wikimedia.org/wiki/File:Mipmap_Aliasing_Comparison.png)
- 문서 삽입 파일 `External/mipmap-print.png`
- [이용 조건 CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 흰색으로 표시했습니다.

### decal · 출처 46

공식 비교 이미지 · 같은 돌벽에 데칼을 적용하기 전과 후입니다. UE 5.5 문서의 사례입니다.

읽을 곳  반복되는 벽돌 위에 생긴 손상과 표면 변화가 어디까지 이어지는지 봅니다. 데칼 수나 성능의 통제 실험은 아니므로 투영 면적·겹침의 비용은 실습에서 따로 측정합니다.

- 저자 © Epic Games · 공식 문서
- [원문](https://dev.epicgames.com/documentation/en-us/unreal-engine/decal-materials-in-unreal-engine?application_version=5.5)
- 문서 삽입 파일 `External/decal-print.png`
- 원저작권과 원문 출처 표시는 유지합니다
- 편집 원본 전체 유지 · 투명 배경은 흰색으로 표시

### depth · 출처 47

외부 비교 이미지 · 왼쪽은 깊이 비교를 항상 통과, 오른쪽은 앞쪽 깊이를 선택한 OpenGL 예시입니다.

읽을 곳  왼쪽에서 바닥이 큐브를 잘못 덮는 부분과 오른쪽의 올바른 가림을 비교합니다. 깊이 검사의 필요성을 보여 주며, Early Z로 몇 ms를 절약했는지 입증하는 이미지는 아닙니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문](https://learnopengl.com/Advanced-OpenGL/Depth-testing)
- 문서 삽입 파일 `External/depth-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 동일 범위의 원본을 나란히 배치 · 표제 추가

### overdraw · 출처 48

외부 진단 화면 · Android Developers가 소개한 Unreal Editor의 Quad Overdraw 시각화입니다.

읽을 곳  겹친 영역의 진단색과 아래 범례를 같이 봅니다. 작은 화면 묶음에서의 처리 비효율을 찾는 화면이며 실제 GPU 시간은 아닙니다. 원본은 이전 에디터 UI로 UE 5.8의 메뉴 배치는 다를 수 있습니다.

- 저자 Android Developers · Google
- [원문](https://developer.android.com/games/optimize/materials)
- 문서 삽입 파일 `External/overdraw-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체 유지 · 투명 배경은 흰색으로 표시

### shader-stats · 출처 48

외부 에디터 화면 · 대상 플랫폼별 셰이더 통계 표를 발췌했습니다.

읽을 곳  픽셀·정점 셰이더와 텍스처 관련 항목을 나누어 읽습니다. 그림의 플랫폼·명령 수는 외부 사례이며 이 프로젝트의 측정값이 아닙니다. WPO 비용은 정점 수·그림자 패스·모션 정보와 함께 별도로 확인합니다.

- 저자 Android Developers · Google
- [원문](https://developer.android.com/games/optimize/materials)
- 문서 삽입 파일 `External/shader-stats-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 일부 발췌·확대 · 색상 유지 · 표제 추가

### substrate-coat · 출처 49

Epic 공식 비교 · 코팅 아래 체크 패턴이 흐려지는 사례입니다. UE 5.4 문서의 그림입니다.

읽을 곳  오른쪽의 패턴이 더 흐립니다. 원문은 코팅 거칠기와 두께를 함께 높인 비교이므로 한 변수의 효과로 읽지 않습니다. 단순화·저장 형식의 현재 지원 조건과 비용은 UE 5.8 프로젝트에서 확인합니다.

- 저자 © Epic Games · 공식 문서
- [원문](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.4)
- 문서 삽입 파일 `External/substrate-coat-print.png`
- 원저작권과 원문 출처 표시는 유지합니다
- 편집 원본 전체 유지 · 투명 배경은 흰색으로 표시

### sss-model · 출처 50

Epic 공식 비교 · 레거시 Subsurface 모델에서 Opacity를 0·0.35·0.65·1로 바꾼 사례입니다.

읽을 곳  같은 역광에서 몸통과 얇은 부분의 색·빛 번짐이 어떻게 달라지는지 봅니다. 이 입력의 의미를 일반 투명도나 다른 SSS 모델에 그대로 적용하지 않습니다. UE 5.5 문서의 예시입니다.

- 저자 © Epic Games · 공식 문서
- [원문](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-subsurface-scattering-in-unreal-engine-materials?application_version=5.5)
- 문서 삽입 파일 `External/sss-model-print.png`
- 원저작권과 원문 출처 표시는 유지합니다
- 편집 원본 전체 유지 · 투명 배경은 흰색으로 표시

### draw-pipeline · 출처 51

Epic 공식 도식 · 메시 정보에서 그리기 명령과 그래픽 API 호출로 이어지는 준비 과정입니다.

읽을 곳  위쪽의 메시 표현에서 아래쪽의 제출 명령까지 단계가 나뉩니다. C++ 이름을 암기할 필요는 없습니다. 같은 메시도 섹션과 패스에 따라 작업이 달라지므로 Actor 수와 호출 수를 구분합니다. UE 5.5 문서의 개념도입니다.

- 저자 © Epic Games · 공식 문서
- [원문](https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-drawing-pipeline-in-unreal-engine?application_version=5.5)
- 문서 삽입 파일 `External/draw-pipeline-print.png`
- 원저작권과 원문 출처 표시는 유지합니다
- 편집 원본 전체 유지 · 투명 배경은 흰색으로 표시

### instance-data · 출처 52

외부 렌더 이미지 · 공통 사각형을 인스턴싱하면서 배치별 위치와 크기를 달리한 예입니다.

읽을 곳  같은 기본 형상을 공유해도 복사본마다 변환 정보가 다릅니다. OpenGL 학습 예시이며 UE ISM의 호출 수나 속도를 측정한 자료는 아닙니다. 외관을 유지하며 제출 비용이 줄었는지는 목표 장면에서 검증합니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문](https://learnopengl.com/Advanced-OpenGL/Instancing)
- 문서 삽입 파일 `External/instance-data-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체 유지 · 투명 배경은 흰색으로 표시

### culling · 출처 53

Epic 공식 단계별 그림 · 시야 밖 제외와 앞 물체에 가려진 후보의 제외를 보여 줍니다.

읽을 곳  오른쪽의 점선으로 남은 물체와 앞쪽의 흰 물체를 비교합니다. 왼쪽은 전체 배치이며, 오른쪽은 시야·가림 판정을 적용한 상태입니다. 최종 화면에서 빠져도 그림자용 작업까지 모두 사라진다고 해석하지 않습니다.

- 저자 © Epic Games · 공식 문서
- [원문](https://dev.epicgames.com/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-in-unreal-engine)
- 문서 삽입 파일 `External/culling-print.png`
- 원저작권과 원문 출처 표시는 유지합니다
- 편집 동일 범위의 원본을 나란히 배치 · 표제 추가

### streaming-stats · 출처 54

Epic 공식 통계 화면 · stat streaming의 Memory Counters를 발췌하고 항목과 수치 사이의 여백을 줄였습니다.

읽을 곳  Memory Counters의 Pool·Required·Visible 등 서로 다른 항목을 구분합니다. 화면의 숫자는 원문 예시이며 권장 예산이 아닙니다. UE 5.5 자료이므로 항목 배치는 현재 빌드에서 확인합니다.

- 저자 © Epic Games · 공식 문서
- [원문](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-streaming-metrics-in-unreal-engine?application_version=5.5)
- 문서 삽입 파일 `External/streaming-stats-print.png`
- 원저작권과 원문 출처 표시는 유지합니다
- 편집 원본 통계 표 발췌 · 가운데 여백만 축소 · 값과 항목 유지

### lumen-reflection · 출처 55

Epic 공식 반사 비교 · 왼쪽 Surface Cache, 오른쪽 Hit Lighting입니다. 동일한 바닥 반사 영역을 발췌했습니다.

읽을 곳  오른쪽 바닥에 추가된 밝은 반사선과 조명 반응을 봅니다. 반사 조명 평가 방식의 차이이며 모든 Lumen 문제의 해결책은 아닙니다. 원문 UE 5.5 예시를 현재 기능 지원·GPU 시간과 구분합니다.

- 저자 © Epic Games · 공식 문서
- [원문](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-technical-details-in-unreal-engine?application_version=5.5)
- 문서 삽입 파일 `External/lumen-reflection-print.png`
- 원저작권과 원문 출처 표시는 유지합니다
- 편집 원본 일부 발췌·확대 · 색상 유지 · 표제 추가

### vsm-cache · 출처 56

Epic 공식 진단 비교 · 왼쪽은 캐시 페이지, 오른쪽은 무효화를 유발하는 Bounds도 표시한 화면입니다.

읽을 곳  이 시각화에서 초록은 재사용, 빨강은 새로 필요하거나 무효화된 페이지입니다. 오른쪽 경계가 어떤 영역에 영향을 주는지 봅니다. UE 5.4 문서의 표시 예이며 비용 측정은 진단 모드를 끈 뒤 수행합니다.

- 저자 © Epic Games · 공식 문서
- [원문](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-shadow-maps-in-unreal-engine?application_version=5.4)
- 문서 삽입 파일 `External/vsm-cache-print.png`
- 원저작권과 원문 출처 표시는 유지합니다
- 편집 동일 범위의 원본을 나란히 배치 · 표제 추가

### taa-edges · 출처 57

Epic 공식 AA 전후 비교 · 같은 난간 부위를 확대해 정지된 가장자리의 차이를 보여 줍니다.

읽을 곳  왼쪽 AA 미적용과 오른쪽 AA 적용의 계단형 경계를 비교합니다. 원문은 일반 AA 비교이며 이 그림만으로 TAA의 잔상·시간적 안정성이나 다른 AA보다의 우위를 판단할 수 없습니다. 이동 검증은 아래 절차로 수행합니다.

- 저자 © Epic Games · 공식 문서
- [원문](https://dev.epicgames.com/documentation/en-us/unreal-engine/anti-aliasing-and-upscaling-in-unreal-engine?application_version=5.5)
- 문서 삽입 파일 `External/taa-edges-print.png`
- 원저작권과 원문 출처 표시는 유지합니다
- 편집 원본 일부 발췌·확대 · 색상 유지 · 표제 추가

### tsr-output · 출처 58

Epic 공식 TSR 비교 · 왼쪽 네이티브 4K, 오른쪽 1080p에서 4K로 재구성한 결과의 같은 구역을 발췌했습니다.

읽을 곳  출력 크기가 같아도 들어온 정보량은 다릅니다. 글자·창틀 같은 세부를 비교하되 정지된 한 장이 이동 품질을 보장하지는 않습니다. UE 5.5 원문 장면의 성능 수치를 이 프로젝트의 예상 이득으로 사용하지 않습니다.

- 저자 © Epic Games · 공식 문서
- [원문](https://dev.epicgames.com/documentation/en-us/unreal-engine/temporal-super-resolution-in-unreal-engine?application_version=5.5)
- 문서 삽입 파일 `External/tsr-output-print.png`
- 원저작권과 원문 출처 표시는 유지합니다
- 편집 원본 일부 발췌·확대 · 색상 유지 · 표제 추가

### cpu-frames · 출처 59

외부 실측 화면 · John Farrow가 기록한 Unreal Insights의 프레임 시간 그래프입니다.

읽을 곳  긴 막대가 나타난 구간을 고른 뒤 CPU·GPU 시간축을 열어 원인을 찾습니다. 그래프 자체로 CPU 병목이라고 판정하지 않습니다. 저자의 2024년 프로젝트 예시이며 이 저장소의 측정 결과가 아닙니다.

- 저자 © John Farrow · Unrealcode.net
- [원문](https://www.unrealcode.net/Optimization_Part3/)
- 문서 삽입 파일 `External/cpu-frames-print.png`
- 원저작권과 원문 출처 표시는 유지합니다
- 편집 원본 전체 유지 · 투명 배경은 흰색으로 표시

### gpu-events · 출처 60

외부 실제 도구 화면 · GPU Insights 시간축의 이벤트 계층을 발췌·확대했습니다.

읽을 곳  큰 Frame 구간 안에 작은 작업 구간이 포함됩니다. 로그에서 Inclusive는 하위 작업을 포함한 시간, Exclusive는 자체 시간입니다. 부모·자식 시간을 모두 더하지 않습니다. UE 5.6 예시이므로 실제 UI와 기록 항목은 현재 빌드에서 확인합니다.

- 저자 Tom Looman 문서 수록 · Unreal Engine 도구 화면
- [원문](https://tomlooman.com/unreal-engine-5-6-performance-highlights/)
- 문서 삽입 파일 `External/gpu-events-print.png`
- 원저작권과 원문 출처 표시는 유지합니다
- 편집 원본 일부 발췌·확대 · 색상 유지 · 표제 추가

## 원본 다운로드 기록

[원본 URL과 SHA256 기록](External/SourceManifest.json)에 보관한 원본별 출처가 있습니다.

## 이전 간접광 참고 이미지

Trevorgoodchild의 Cornell box 이미지는 `Concepts/cornellbox.png`에 보관되어 있습니다. 현재 Lumen 본문은 간접광의 색 전달을 설명하기 위해 이 그림을 다시 사용합니다. Lumen 실행 결과로 표시하지 않습니다.
[Cornell box 원본과 Public domain 표기](https://commons.wikimedia.org/wiki/File:Cornellbox_pathtracing_irradiancecaching.png)

확인일 2026-11-08. 저작권과 출처 표시는 각 원본에 따릅니다.
