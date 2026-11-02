# MajorMap Fonts

상업적으로 쓸 수 있는 한글 무료 글꼴 12종을 CSS 한 줄로 불러오는 저장소입니다. [jsDelivr](https://www.jsdelivr.com/) 글로벌 CDN으로 서비스합니다.

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/hoony-majormap/majormap-fonts@v1.0.0/css/suit.css">
```

```css
body { font-family: "SUIT", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif; }
```

## 글꼴 목록

`css/` 뒤의 파일 이름만 바꾸면 됩니다.

| 글꼴 | CSS 파일 | `font-family` | 굵기 | 웹 파일 크기 | 라이선스 |
|---|---|---|---|---|---|
| Noto Sans KR | `noto-sans-kr.css` | `Noto Sans KR` | 100–900 | 글자 단위 분할 | OFL 1.1 |
| Gothic A1 | `gothic-a1.css` | `Gothic A1` | 300, 400, 500, 700 | 글자 단위 분할 | OFL 1.1 |
| IBM Plex Sans KR | `ibm-plex-sans-kr.css` | `IBM Plex Sans KR` | 300, 400, 500, 700 | 글자 단위 분할 | OFL 1.1 |
| Spoqa Han Sans Neo | `spoqa-han-sans-neo.css` | `Spoqa Han Sans Neo` | 100, 300, 400, 500, 700 | 굵기당 약 180KB | OFL 1.1 |
| SUIT | `suit.css` | `SUIT` | 100–900 | 전체 약 620KB | OFL 1.1 |
| Wanted Sans | `wanted-sans.css` | `Wanted Sans` | 400–1000 | 전체 약 1.3MB | OFL 1.1 |
| Paperlogy | `paperlogy.css` | `Paperlogy` | 100–900 | 굵기당 약 440KB | OFL 1.1 |
| S-Core Dream | `s-core-dream.css` | `S-Core Dream` | 100–900 | 굵기당 약 740KB | 에스코어 자체 라이선스 |
| LINE Seed Sans KR | `line-seed-sans-kr.css` | `LINE Seed Sans KR` | 100, 400, 700 | 굵기당 약 460KB | OFL 1.1 |
| NanumSquare Neo | `nanum-square-neo.css` | `NanumSquare Neo` | 300, 400, 700, 800, 900 | 굵기당 약 380KB | OFL 1.1 |
| Freesentation | `freesentation.css` | `Freesentation` | 100–900 | 굵기당 약 480KB | OFL 1.1 |
| A2Z | `a2z.css` | `A2Z` | 100–900 | 굵기당 약 150KB | OFL 1.1 |

브라우저는 페이지에서 실제로 쓰는 굵기의 파일만 받습니다.

SUIT와 Spoqa Han Sans Neo의 웹 파일은 제작사가 자주 쓰는 글자만 추린 버전입니다. 드물게 쓰는 한글은 다음 순서의 글꼴로 표시되므로 `font-family`에 대체 글꼴을 꼭 함께 적어 주세요.

## 한국어 외 언어

대표 글자를 뽑아 글꼴에 들어 있는지 확인한 결과입니다. 해당 글꼴이 없는 언어는 대체 글꼴로 표시됩니다.

| 언어 | 쓸 수 있는 글꼴 |
|---|---|
| 영어, 인도네시아어 | 12종 모두 |
| 베트남어 | Gothic A1, Noto Sans KR |
| 몽골어(키릴 문자) | Gothic A1 |
| 중국어 간체 | 없음. 별도 글꼴이 필요합니다 |

## 라이선스

모든 글꼴은 상업적으로 쓸 수 있습니다. 전문은 [`licenses/`](licenses/)에 있습니다. 이 저장소는 글꼴의 저작권을 갖지 않으며, 각 글꼴의 권리는 제작사에 있습니다.

- **OFL 1.1 글꼴 11종**: 웹사이트, 앱, 인쇄물, 영상, 로고에 쓸 수 있고 재배포도 됩니다. 글꼴 파일만 따로 판매하는 것은 금지입니다.
- **S-Core Dream**: 상업적 사용과 재배포가 가능합니다. 다만 파일 수정과 판매가 금지되어 있어 woff2로 변환하지 않고 원본 OTF를 그대로 제공합니다.
- **S-Core Dream, NanumSquare Neo**: 이 글꼴을 쓴 인쇄물과 광고물 이미지가 제작사 홍보에 활용될 수 있습니다. 원하지 않으면 제작사에 요청하면 됩니다.

## 파일을 수정하지 않습니다

IBM Plex Sans KR, Spoqa Han Sans Neo, SUIT 등은 OFL의 예약 글꼴 이름(Reserved Font Name)이 선언되어 있어, 수정본에 같은 이름을 쓰면 라이선스에 어긋날 수 있습니다. 그래서 글꼴을 직접 분할하거나 변환하지 않습니다.

- `fonts/`의 파일은 공식 배포본과 바이트 단위로 같습니다. 해시는 [`SHA256SUMS`](SHA256SUMS)에 있습니다. A2Z만 URL을 위해 한글 파일 이름을 영문으로 바꿨습니다.
- Noto Sans KR, Gothic A1, IBM Plex Sans KR은 파일을 이 저장소에 두지 않고 [Fontsource](https://fontsource.org/) npm 패키지에서 불러옵니다.

## 출처

| 글꼴 | 공식 배포처 | 버전 |
|---|---|---|
| Noto Sans KR | [@fontsource-variable/noto-sans-kr](https://www.npmjs.com/package/@fontsource-variable/noto-sans-kr) (원본: [google/fonts](https://github.com/google/fonts/tree/main/ofl/notosanskr)) | 5.3.1 |
| Gothic A1 | [@fontsource/gothic-a1](https://www.npmjs.com/package/@fontsource/gothic-a1) (원본: [google/fonts](https://github.com/google/fonts/tree/main/ofl/gothica1)) | 5.3.0 |
| IBM Plex Sans KR | [@fontsource/ibm-plex-sans-kr](https://www.npmjs.com/package/@fontsource/ibm-plex-sans-kr) (원본: [google/fonts](https://github.com/google/fonts/tree/main/ofl/ibmplexsanskr)) | 5.3.0 |
| Spoqa Han Sans Neo | [spoqa/spoqa-han-sans](https://github.com/spoqa/spoqa-han-sans) | v3.3.0 |
| SUIT | [sun-typeface/SUIT](https://github.com/sun-typeface/SUIT) | v2.0.5 |
| Wanted Sans | [wanteddev/wanted-sans](https://github.com/wanteddev/wanted-sans) | v1.0.3 |
| Paperlogy | [Freesentation/Paperlogy](https://github.com/Freesentation/Paperlogy) | 1.001 |
| S-Core Dream | [에스코어](https://s-core.co.kr/who-we-are/font/) | 1.000 |
| LINE Seed Sans KR | [seed.line.me](https://seed.line.me/index_kr.html) | 2023.09.06 |
| NanumSquare Neo | [네이버](https://campaign.naver.com/nanumsquare_neo/) | 1.000 |
| Freesentation | [Freesentation/Freesentation](https://github.com/Freesentation/Freesentation) | 웹 파일 1.006 |
| A2Z | [Freesentation/A2Z](https://github.com/Freesentation/A2Z) | 1.001 |

새로 빌드하려면 공식 패키지를 내려받아 압축을 푼 뒤 `python3 -I scripts/build.py --dl <패키지 폴더> --notices <안내문 폴더>`를 실행합니다.
