# 이미지 출처와 편집 기록

본문에서 외부 참고 그림과 직접 제작한 도식, 실제 엔진 캡처를 구분합니다. 외부 이미지는 실제 파일로 문서에 삽입되어 있습니다.

## 직접 제작한 도식과 엔진 캡처

`Concepts/explain-*.png`는 직접 제작한 설명도입니다. 실제 엔진 실행 화면이나 실측 그래프가 아닙니다.
`CH01`의 12개 원본은 이 프로젝트의 UE 5.8.4 장면을 직접 촬영했습니다. 조건과 파일 해시는 `CH01/CaptureManifest.json`에 있습니다.

## 기존 외부 간접광 사례

- 제목 Cornellbox pathtracing irradiancecaching
- 저자 Trevorgoodchild · Public domain
- [원본과 이용 조건](https://commons.wikimedia.org/wiki/File:Cornellbox_pathtracing_irradiancecaching.png)
- 파일 `Concepts/cornellbox.png`
- 원본의 색상·비율·전체 구도를 유지해 CH21 설명도에 축소 배치했습니다. Lumen 캡처가 아닌 일반 간접광 사례입니다.

## 이번 보완에서 삽입한 외부 자료

원본 이미지 14점을 12개 그림으로 배치했습니다. 모든 그림에 원본 링크와 관찰 지점을 붙였습니다.

### coordinates · 출처 37

외부 참고 그림 · 모델의 로컬 공간부터 월드·카메라·클립·화면 공간까지 이어지는 좌표 변환입니다.

읽을 곳  1→2에서는 큐브를 장면에 배치하고, 2→3에서는 카메라를 기준으로 장면을 해석합니다. 4→5에서는 투영한 결과가 화면 영역에 대응합니다. UE와 OpenGL의 축·깊이 규약은 같지 않지만 좌표 기준을 바꾸는 목적은 같습니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문 출처](https://learnopengl.com/Getting-started/Coordinate-Systems)
- 문서 삽입 파일 `External/coordinates-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 인쇄를 위해 흰색으로 표시했습니다.

### projection · 출처 37

외부 비교 이미지 · 같은 형상의 투영 방식 비교입니다. 왼쪽 Perspective(원근), 오른쪽 Orthographic(직교)입니다.

읽을 곳  왼쪽은 뒤로 갈수록 크기와 간격이 작아 보입니다. 오른쪽은 깊이에 따른 크기 변화가 없어 평행한 방향을 읽기 쉽습니다. 투영 방식의 비교이며 UE의 캡처가 아닙니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문 출처](https://learnopengl.com/Getting-started/Coordinate-Systems)
- 문서 삽입 파일 `External/projection-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 인쇄를 위해 흰색으로 표시했습니다.

### raster · 출처 38

외부 비교 그림 · 삼각형과 화면 격자, 그리고 포함 판정을 표시한 결과를 나란히 배치했습니다.

읽을 곳  왼쪽의 매끈한 삼각형 경계와 오른쪽의 격자에 맞춘 계단형 경계를 비교합니다. 이 그림은 래스터화와 앨리어싱의 관계를 설명하며 TAA 또는 TSR의 전후 결과가 아닙니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문 출처](https://learnopengl.com/Advanced-OpenGL/Anti-Aliasing)
- 문서 삽입 파일 `External/raster-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 인쇄를 위해 흰색으로 표시했습니다.

원본 2점을 나란히 배치하고 상단에 표제를 추가했습니다.

### deferred · 출처 39

외부 참고 그림 · Geometry Pass에서 얻은 여러 표면 버퍼를 Lighting Pass에서 사용합니다.

읽을 곳  가운데 버퍼의 위치·법선·색 정보가 오른쪽의 조명 결과에 어떻게 모이는지 봅니다. OpenGL 학습용 구현이므로 UE의 실제 GBuffer 배치와 동일하다고 해석하지 않습니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문 출처](https://learnopengl.com/Advanced-Lighting/Deferred-Shading)
- 문서 삽입 파일 `External/deferred-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 인쇄를 위해 흰색으로 표시했습니다.

### gbuffer · 출처 39

외부 시각화 이미지 · 같은 장면의 위치·법선·Albedo·Specular를 분리해 표시한 GBuffer 예시입니다.

읽을 곳  왼쪽 위는 위치에 따라, 오른쪽 위는 표면 방향에 따라 색이 달라집니다. 아래쪽은 재질의 색과 반사 입력입니다. 진단용 색을 최종 외관이나 UE 채널 구성으로 읽지 않습니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문 출처](https://learnopengl.com/Advanced-Lighting/Deferred-Shading)
- 문서 삽입 파일 `External/gbuffer-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 인쇄를 위해 흰색으로 표시했습니다.

### pbr · 출처 40

외부 렌더 이미지 · 금속성과 거칠기를 달리한 구들을 두 시점에서 비교합니다.

읽을 곳  오른쪽 배열의 가로 방향에서 거칠기가 변할 때 작은 반사점이 넓어지는 모습을 봅니다. 세로 방향의 금속성 변화도 함께 비교합니다. UE와 광원·톤매핑이 같은 비교 자료는 아닙니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문 출처](https://learnopengl.com/PBR/Lighting)
- 문서 삽입 파일 `External/pbr-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 인쇄를 위해 흰색으로 표시했습니다.

### brdf · 출처 41

외부 개념도 · 미세한 표면 방향의 차이가 반사광의 퍼짐에 영향을 주는 모습입니다.

읽을 곳  거친 표면에서는 여러 방향으로, 매끈한 표면에서는 더 모인 방향으로 반사하는 차이를 봅니다. 확대된 개념도이며 실제 메시의 모든 미세 면을 직접 만드는 뜻은 아닙니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문 출처](https://learnopengl.com/PBR/Theory)
- 문서 삽입 파일 `External/brdf-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 인쇄를 위해 흰색으로 표시했습니다.

### fresnel · 출처 41

외부 시각화 이미지 · 구의 중심과 실루엣 부근에서 Fresnel 반사 계수가 달라지는 예입니다.

읽을 곳  중심보다 테두리가 밝습니다. 곡면의 테두리에서 시선이 표면에 더 비스듬하게 닿기 때문입니다. 물체의 완성 렌더가 아닌 반사 계수의 시각화입니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문 출처](https://learnopengl.com/PBR/Theory)
- 문서 삽입 파일 `External/fresnel-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 인쇄를 위해 흰색으로 표시했습니다.

### translucency · 출처 41

외부 개념도 · 입사한 빛이 표면에서 반사되거나 내부로 들어가 산란·흡수될 수 있습니다.

읽을 곳  표면에서 되돌아가는 경로와 내부로 들어가는 경로를 구분합니다. 이 개념만으로 UE 반투명 구현이 물질 내부의 모든 광선을 추적한다고 해석하지 않습니다.

- 저자 © Joey de Vries · LearnOpenGL · @JoeyDeVriez
- [원문 출처](https://learnopengl.com/PBR/Theory)
- 문서 삽입 파일 `External/translucency-print.png`
- [이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 인쇄를 위해 흰색으로 표시했습니다.

### lod · 출처 42

외부 비교 그림 · 비슷한 실루엣을 더 적은 변으로 근사한 세 가지 LOD입니다.

읽을 곳  오른쪽으로 갈수록 위쪽 윤곽이 각지게 바뀝니다. 원본의 LOD 1·2·3 표기는 해당 그림의 번호이며 UE에서 흔히 시작하는 LOD0 번호와 구별합니다.

- 저자 Sirotk · Wikimedia Commons
- [원문 출처](https://commons.wikimedia.org/wiki/File:LOD_Example.png)
- 문서 삽입 파일 `External/lod-print.png`
- [이용 조건 CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 인쇄를 위해 흰색으로 표시했습니다.

### nanite · 출처 45

Epic 공식 비교 이미지 · Nanite Clusters 시각화에서 Preserve Area를 끈 상태와 켠 상태입니다.

읽을 곳  왼쪽의 검게 비어 보이는 잎 사이 공간과 오른쪽의 더 조밀한 수관을 비교합니다. 삼각형을 줄일 때 소실되는 잎 면적을 보존하는 사례입니다. 색은 재질색이 아닌 클러스터 구분이며 UE 5.5 문서의 예시로, 이 프로젝트의 UE 5.8 실측이나 성능 비교가 아닙니다.

- 저자 © Epic Games · UE 5.5 공식 문서
- [원문 출처](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.5)
- 문서 삽입 파일 `External/nanite-print.png`
- © Epic Games. 원저작권을 유지한 공식 문서 참고 이미지이며 별도의 공개 라이선스를 부여하지 않습니다.
- 편집 원본 전체·색상·비율 유지. 투명 배경은 인쇄를 위해 흰색으로 표시했습니다.

원본 2점을 나란히 배치하고 상단에 표제를 추가했습니다.

### mipmap · 출처 43

외부 실제 렌더 비교 · 왼쪽 No MipMapping, 오른쪽 With MipMapping입니다.

읽을 곳  수평선에 가까운 먼 바닥에서 왼쪽의 물결무늬와 오른쪽의 안정된 패턴을 비교합니다. 원본은 Blender 렌더이며 필터링도 관여할 수 있으므로 UE에서 밉만 바꾼 통제 실험으로 해석하지 않습니다.

- 저자 BillyBob CornCob · Wikimedia Commons
- [원문 출처](https://commons.wikimedia.org/wiki/File:Mipmap_Aliasing_Comparison.png)
- 문서 삽입 파일 `External/mipmap-print.png`
- [이용 조건 CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)
- 편집 원본 전체·색상·비율 유지. 투명 배경은 인쇄를 위해 흰색으로 표시했습니다.

## 원본 URL

- [coordinates](https://learnopengl.com/img/getting-started/coordinate_systems.png)
- [projection](https://learnopengl.com/img/getting-started/perspective_orthographic.png)
- [raster-outline](https://learnopengl.com/img/advanced/anti_aliasing_rasterization.png)
- [raster](https://learnopengl.com/img/advanced/anti_aliasing_rasterization_filled.png)
- [deferred](https://learnopengl.com/img/advanced-lighting/deferred_overview.png)
- [gbuffer](https://learnopengl.com/img/advanced-lighting/deferred_g_buffer.png)
- [pbr](https://learnopengl.com/img/pbr/lighting_result.png)
- [brdf](https://learnopengl.com/img/pbr/microfacets_light_rays.png)
- [fresnel](https://learnopengl.com/img/pbr/fresnel.png)
- [translucency](https://learnopengl.com/img/pbr/surface_reaction.png)
- [lod](https://upload.wikimedia.org/wikipedia/commons/2/26/LOD_Example.png)
- [mipmap](https://upload.wikimedia.org/wikipedia/commons/5/59/Mipmap_Aliasing_Comparison.png)
- [nanite-off](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/62955159-0c76-4b0a-a468-1e3c489adf3b/nanite-preservearea-disabled-clustervis.png)
- [nanite-on](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ed92757-cb3a-4e94-822d-f69162156991/nanite-preservearea-enabled-clustervis.png)

확인일 2026-11-08. 외부 이미지의 이용 조건은 각 이미지에 적용되며 저장소 전체의 라이선스와 구별합니다.
