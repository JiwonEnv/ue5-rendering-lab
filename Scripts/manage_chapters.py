"""Maintain the stable chapter registry and its README index."""
import argparse
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / 'Docs/chapters.json'


def update_readme(chapters):
    rows = []
    for chapter in chapters:
        status = {'starter': '기본 레벨 준비', 'implemented': '예제 구현',
                  'verified': '실습 검증 완료'}.get(chapter['status'], chapter['status'])
        rows.append(f"| {chapter['id']} | [{chapter['title']}]({chapter['notes']}) | {status} |")
    text = '''# UE5 Rendering Lab

게임 배경 아티스트를 위한 언리얼 엔진 5 렌더링 원리와 최적화 실습 프로젝트입니다.

## 현재 구성

UE 5.8.4의 콘텐츠 전용 프로젝트입니다. 시작 레벨과 챕터별 기본 실습 레벨을 제공합니다.
각 기본 레벨에는 공통 비교 무대, 조명, 고정 노출, 카메라와 비교용 구가 있습니다.
챕터별 특화 기능을 구현하는 절차는 각 실습 문서에 정리되어 있습니다.
`기본 레벨 준비` 상태의 챕터는 해당 기능의 완성 예제가 될 때까지 추가 제작이 필요합니다.

## 시작하기

1. UE 5.8.4와 Git LFS를 준비합니다.
2. 저장소를 복제한 뒤 `git lfs pull`로 바이너리 에셋을 받습니다.
3. `RenderingLab.uproject`를 엽니다. 첫 실행은 셰이더와 거리장 준비에 시간이 걸릴 수 있습니다.
4. 시작 레벨 `Content/RenderingLab/Maps/L_RenderingLab`을 확인합니다.
5. 아래 실습 문서에서 레벨 경로를 확인하고 해당 챕터 맵을 엽니다.

에디터 시점을 비교 구도로 맞추려면 Outliner에서 `ComparisonCamera`를 선택하고
카메라를 Pilot합니다. Play에서도 자동 활성화 카메라로 비교 무대를 볼 수 있습니다.

Windows DX12 SM6, Deferred, Lumen, Virtual Shadow Maps, TSR,
Substrate Blendable을 시작 설정으로 사용합니다. 대상 기기에서 기능 지원을 확인하세요.
Forward 전환이나 Adaptive GBuffer 실험은 프로젝트 설정 변경과 재시작이 필요할 수 있습니다.

## 학습 순서

<!-- Generated from Docs/chapters.json by Scripts/manage_chapters.py -->
| ID | 주제와 실습 절차 | 제작 상태 |
| --- | --- | --- |
''' + '\n'.join(rows) + '''

## 구조와 확장

- [폴더 구조와 에셋 규칙](Docs/FolderStructure.md)
- [새 챕터 추가 방법](Docs/AddingChapters.md)
- [커밋 규칙](CONTRIBUTING.md)
- [한국어 학습 가이드 PDF](Docs/Guide/UE5_Rendering_Guide_KO.pdf)

챕터 ID와 에셋 경로는 유지하고 `Docs/chapters.json` 배열에서 학습 순서를 관리합니다.
새 챕터는 새 ID를 부여한 뒤 원하는 학습 순서에 배치할 수 있습니다.
공유 에셋은 `Content/RenderingLab/Common`에서 관리합니다.

## 기본 레벨 생성

에디터를 닫은 뒤 PowerShell에서 실행합니다.

```powershell
.\\Scripts\\BuildLab.ps1
```

생성 도구는 누락된 레벨과 공용 머티리얼을 만듭니다. 기존 에셋은 보존합니다.
검수 로그는 `Saved/Logs/LabBuild.log`에 생성되며 Git에 포함하지 않습니다.
생성 단계의 NullRHI 실행은 에셋 저장과 로드 검증용입니다.
렌더링 품질과 성능은 실제 GPU로 에디터 또는 빌드를 실행해 별도로 측정합니다.

## 자료 출처

기본 무대는 Unreal Engine에 포함된 BasicShapes를 참조하며 외부 에셋을 포함하지 않습니다.
프로젝트를 열려면 Epic Games의 Unreal Engine 설치가 필요합니다.
각 주제의 참고 링크는 학습 가이드의 출처 목록에서 확인할 수 있습니다.
'''
    (ROOT / 'README.md').write_text(text, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--slug')
    parser.add_argument('--title')
    parser.add_argument('--part', default='Part06_Extensions')
    parser.add_argument('--after')
    args = parser.parse_args()
    chapters = json.loads(REGISTRY.read_text(encoding='utf-8'))
    if not isinstance(chapters, list) or not chapters:
        parser.error('The chapter registry must be a nonempty array')
    ids = [chapter['id'] for chapter in chapters]
    paths = [chapter['map'] for chapter in chapters]
    if len(ids) != len(set(ids)) or len(paths) != len(set(paths)):
        parser.error('Duplicate chapter IDs or map paths in registry')
    if args.slug or args.title:
        if not args.slug or not args.title:
            parser.error('--slug and --title must be supplied together')
        for value in (args.slug, args.part):
            if not re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', value):
                parser.error('Slug and part must use letters, digits and underscores')
        if any(chapter['slug'].casefold() == args.slug.casefold() for chapter in chapters):
            parser.error('A chapter with that slug already exists')
        if args.after and args.after not in ids:
            parser.error('--after must name an existing chapter ID')
        number = max(int(chapter['id'][2:]) for chapter in chapters) + 1
        chapter_id = f'CH{number:02d}'
        folder = f'{chapter_id}_{args.slug}'
        map_path = f'/Game/RenderingLab/Chapters/{args.part}/{folder}/Maps/L_{folder}'
        content = ROOT / Path(map_path.replace('/Game/', 'Content/')).parent.parent
        notes = f'Docs/Chapters/{folder}.md'
        if content.exists() or (ROOT / notes).exists():
            parser.error('Destination already exists. Inspect existing content before adding it.')
        for sub in ('Maps', 'Materials', 'Meshes', 'Textures', 'Blueprints'):
            path = content / sub
            path.mkdir(parents=True)
            (path / '.gitkeep').touch()
        headings = ['학습 목표', '원리', '제작 절차', '검증 방법', '결과와 참고 자료']
        body = [f'# {chapter_id} {args.title}', '', '**구현 상태 — 기본 실습 레벨 준비**', '',
                f'레벨 경로 `{map_path}`', '']
        for heading in headings:
            body.extend([f'## {heading}', '', '작성 예정', ''])
        (ROOT / notes).write_text('\n'.join(body), encoding='utf-8')
        chapter = {
            'id': chapter_id, 'slug': args.slug, 'title': args.title,
            'part': args.part, 'folder': folder, 'status': 'starter',
            'map': map_path, 'notes': notes,
        }
        index = ids.index(args.after) + 1 if args.after else len(chapters)
        chapters.insert(index, chapter)
        temporary = REGISTRY.with_suffix('.json.tmp')
        temporary.write_text(json.dumps(chapters, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        temporary.replace(REGISTRY)
        print(f'Added {chapter_id}: {args.title}')
    elif args.after:
        parser.error('--after requires a new chapter')
    update_readme(chapters)
    print(f'Updated README index for {len(chapters)} chapters')


if __name__ == '__main__':
    main()
