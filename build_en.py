# -*- coding: utf-8 -*-
"""ENページ生成：JAページをコピーし、表示文言を英語に置換する

合格条件：misses が 0 件のときだけ en/index.html を書き出す（1件でもあれば中断して exit 1）。
JA（index.html）の文言を変えたら、対応する置換ペアを必ず同時に更新すること。
"""
import os, sys
h = open('index.html', encoding='utf-8').read()
misses = []
def rep(old, new, cnt=1):
    global h
    if old not in h:
        misses.append(old[:60]); return
    h = h.replace(old, new, cnt)

# --- 共通文言（title / og:title / twitter:title は同一文、og/twitter description も同一文） ---
JA_TITLE = '東京の広告・ビューティー撮影フォトグラファー｜Katsutomo Izawa（K\'s Creative Works）'
EN_TITLE = 'Tokyo Beauty &amp; Fashion Advertising Photographer | Katsutomo Izawa'
JA_OG_DESC = '東京を拠点に、ビューティー＆ファッションの広告撮影・ブランドイメージ撮影・人物撮影を行うフォトグラファー。写真をもとにしたAI動画生成にも対応。'
EN_OG_DESC = 'Tokyo-based photographer specialising in beauty and fashion advertising, brand imagery and portraits, plus AI film production from stills.'
JA_IMG_ALT = 'Katsutomo Izawa — 東京のビューティー＆ファッション広告撮影フォトグラファー'
EN_IMG_ALT = 'Katsutomo Izawa — Tokyo beauty &amp; fashion advertising photographer'

# --- 基本構造 ---
rep('<html lang="ja">', '<html lang="en">')
rep('src="images/', 'src="../images/', cnt=-1)
rep('data-full="images/', 'data-full="../images/', cnt=-1)
rep('href="images/', 'href="../images/', cnt=-1)
rep('<title>' + JA_TITLE + '</title>',
    '<title>' + EN_TITLE + '</title>')
rep('<meta name="description" content="東京を拠点に、ビューティー＆ファッションの広告撮影・ブランドイメージ撮影・人物撮影を行うフォトグラファー Katsutomo Izawa（K\'s Creative Works）。2013年から活動。写真をもとにしたAI動画生成にも対応。撮影のご相談はお問い合わせフォームから。">',
    '<meta name="description" content="Katsutomo Izawa (Katsu) is a Tokyo-based photographer specialising in beauty and fashion advertising, brand imagery and portraits, plus AI film production from stills. Enquire via the contact form.">')
rep('<meta property="og:title" content="' + JA_TITLE + '">',
    '<meta property="og:title" content="' + EN_TITLE + '">')
rep('<meta property="og:description" content="' + JA_OG_DESC + '">',
    '<meta property="og:description" content="' + EN_OG_DESC + '">')
rep('<meta property="og:url" content="https://ksphotoswork.com/">',
    '<meta property="og:url" content="https://ksphotoswork.com/en/">')
rep('<meta property="og:image:alt" content="' + JA_IMG_ALT + '">',
    '<meta property="og:image:alt" content="' + EN_IMG_ALT + '">')
rep('<meta property="og:locale" content="ja_JP">',
    '<meta property="og:locale" content="en_US">')
rep('<meta property="og:locale:alternate" content="en_US">',
    '<meta property="og:locale:alternate" content="ja_JP">')
rep('<meta name="twitter:title" content="' + JA_TITLE + '">',
    '<meta name="twitter:title" content="' + EN_TITLE + '">')
rep('<meta name="twitter:description" content="' + JA_OG_DESC + '">',
    '<meta name="twitter:description" content="' + EN_OG_DESC + '">')
rep('<meta name="twitter:image:alt" content="' + JA_IMG_ALT + '">',
    '<meta name="twitter:image:alt" content="' + EN_IMG_ALT + '">')
rep('<link rel="canonical" href="https://ksphotoswork.com/">',
    '<link rel="canonical" href="https://ksphotoswork.com/en/">')

# --- JSON-LD（"name": "..." 等の文脈付きで置換し、本文・alt 側のペアと競合させない） ---
rep('"description": "東京を拠点にビューティー＆ファッションの広告撮影を行うフォトグラファー、Katsutomo Izawa（Katsu／K\'s Creative Works）。広告撮影、ブランドイメージ撮影、人物撮影、AI動画生成。"',
    '"description": "Katsutomo Izawa (Katsu) of K\'s Creative Works is a Tokyo-based photographer specialising in beauty and fashion advertising photography, brand imagery, portraits and AI film production."')
rep('"knowsAbout": ["広告撮影", "ビューティー撮影", "ファッション撮影", "ポートレート撮影", "商品撮影", "AI動画生成", "Advertising Photography", "Beauty Photography", "Fashion Photography"]',
    '"knowsAbout": ["Advertising Photography", "Beauty Photography", "Fashion Photography", "Portrait Photography", "Product Photography", "AI Film Production"]')
rep('"name": "撮影メニュー"', '"name": "Services"')
rep('"name": "ビューティー＆ファッション広告撮影"', '"name": "Beauty & Fashion Advertising Photography"')
rep('"name": "ブランド・商品イメージ撮影"', '"name": "Brand & Product Imagery"')
rep('"name": "人物・プロフィール撮影"', '"name": "Portraits & Profiles"')
rep('"name": "ディレクション・編集まで一貫対応"', '"name": "Direction & Editing, End to End"')
rep('"name": "AI動画生成"', '"name": "AI Film Production"')
rep('"name": "ビューティー広告撮影"', '"name": "Beauty advertising photography"')
rep('"name": "名取裕子さん 広告撮影"', '"name": "Yuko Natori — advertising shoot"')
rep('"name": "モノクロのロングヘア女性ポートレート"', '"name": "Monochrome portrait of a woman with long hair"')
rep('"description": "テスト撮影のポートレート作品"', '"description": "A portrait work from a test shoot"')
rep('"inLanguage": "ja"', '"inLanguage": "en"')

# --- ヘッダー・言語切替・モバイルメニュー ---
rep('<span class="lang-switch"><span class="lang-cur">JP</span><span class="sep">|</span><a href="/en/" hreflang="en">EN</a></span>',
    '<span class="lang-switch"><a href="/" hreflang="ja">JP</a><span class="sep">|</span><span class="lang-cur">EN</span></span>')
rep('<div class="mm-lang"><span class="lang-cur">JP</span><span class="sep">|</span><a href="/en/" hreflang="en">EN</a></div>',
    '<div class="mm-lang"><a href="/" hreflang="ja">JP</a><span class="sep">|</span><span class="lang-cur">EN</span></div>')
rep('<button class="menu-btn" id="menuBtn" aria-label="メニューを開く"',
    '<button class="menu-btn" id="menuBtn" aria-label="Open menu"')

# --- ヒーロー ---
rep('<p>東京を拠点に、ビューティー＆ファッションの広告撮影を専門とするフォトグラファー。ブランドと商品のイメージ撮影、人物撮影から、撮影・編集・ディレクションの一貫対応、写真をもとにしたAI動画生成まで。</p>',
    '<p>A Tokyo-based photographer specialising in beauty and fashion advertising. From brand and product imagery to portraits, with direction, shooting and editing handled end to end — including AI film production based on still photography.</p>')
rep('<a class="cta" href="#contact">撮影のご相談はこちら</a>',
    '<a class="cta" href="#contact">Enquire about a shoot</a>')

# --- ギャラリー見出し・alt ---
rep('<h2>主な実績</h2>', '<h2>Selected Works</h2>')
rep('<div class="more-label">その他の実績</div>', '<div class="more-label">MORE CREDITS</div>')
ALTS = [
 ('ビューティー広告撮影、青い水面を背景にした後ろ姿のポートレート', 'Beauty advertising photography — back-view portrait against blue water'),
 ('ロメロ・ブリット 来日記念イベント撮影', 'Romero Britto — Japan visit commemorative event'),
 ('体組成計のプロダクト広告撮影、白背景のスタジオカット', 'Product advertising shoot for a body composition monitor, studio cut on white'),
 ('奥菜恵さん オフィシャルファンサイト「奥菜\'s room」撮影', 'Megumi Okina — official fan site &quot;Okina\'s room&quot; shoot'),
 ('ビューティーポートレート、白背景のスタジオ撮影。黒のストラップレスドレスと赤いリップ', 'Beauty portrait in studio on white — black strapless dress and red lips'),
 ('目を閉じたビューティークローズアップ', 'Beauty close-up with eyes closed'),
 ('黒髪のビューティーポートレート', 'Beauty portrait with black hair'),
 ('レザーコートのファッションエディトリアル撮影', 'Fashion editorial shoot in a leather coat'),
 ('白シャツとスツールのスタジオポートレート', 'Studio portrait with a white shirt and stool'),
 ('モノクロの滝ロケーションポートレート', 'Monochrome location portrait at a waterfall'),
 ('モノクロのロングヘア女性ポートレート（テスト撮影）', 'Monochrome portrait of a woman with long hair (test shoot)'),
 ('モノクロのロングドレス全身ポートレート', 'Monochrome full-length portrait in a long dress'),
 ('名取裕子さん 広告撮影', 'Yuko Natori — advertising shoot'),
 ('トレンチコートのファッションポートレート', 'Fashion portrait in a trench coat'),
 ('黒いラッフルドレスのファッションポートレート', 'Fashion portrait in a black ruffled dress'),
 ('パーティーをテーマにしたファッションエディトリアル撮影', 'Party-themed fashion editorial shoot'),
 ('武藤敬司さん Rakuten Fashion Week Tokyo', 'Keiji Mutoh — Rakuten Fashion Week Tokyo'),
 ('南こうせつさん LIVE', 'Kosetsu Minami — live performance'),
 ('ジャズライブ撮影', 'Jazz live photography'),
 ('ライブステージ撮影', 'Live stage photography'),
 ('夜のイルミネーションを背景にしたポートレート', 'Portrait against night illuminations'),
 ('淡いピンクのニットを着たポートレートのクローズアップ', 'Close-up portrait in a pale pink knit'),
 ('ボブヘアのクローズアップポートレート', 'Close-up portrait with a bob hairstyle'),
 ('男性デュオのポートレート', 'Male duo portrait'),
 ('笑顔のメンズ全身ポートレート', "Smiling full-length men's portrait"),
 ('白いキャップとTシャツのメンズファッションポートレート', "Men's fashion portrait in a white cap and T-shirt"),
 ('六角精児さん 撮影', 'Seiji Rokkaku — portrait shoot'),
]
for ja, en in ALTS:
    rep('alt="' + ja + '"', 'alt="' + en + '"', cnt=99)

# --- AIフィルム（現行 en/index.html の公開済み EN 文言をそのまま再現） ---
rep('<!-- AI FILM section : #works の直後（</section> の後、#services の前）に挿入する -->',
    '<!-- AI FILM section (EN) : insert right after the #works closing </section>, before <section id="services"> in en/index.html -->')
rep('<h2>AIフィルム<span class="h2-note">AI生成サンプル</span></h2>',
    '<h2>AI Film<span class="h2-note">AI-GENERATED SAMPLES</span></h2>')
rep('<p class="aifilm-lead">このコーナーの動画は、すべてAIで生成したサンプルです。写真（実写）とは分けて掲載しています。登場するブランド・商品・モデルは架空のもので、実在の商品ではありません。実際のご依頼では、実物の商品をモデルが着用した撮影を行い、その写真をもとに動画を制作します。</p>',
    '<p class="aifilm-lead">Every film in this corner is an AI-generated sample, presented separately from the photography (real shoots). The brands, products and models shown are fictional and do not exist. For actual commissions, the real product is photographed worn by a model, and the film is then produced from those photographs.</p>')
rep('alt="AI生成ビューティー広告サンプル FUYUKAMERIA の最終カット（笑顔のモデルと赤いボトル、カメリア）"',
    'alt="Final frame of the AI-generated beauty commercial sample FUYUKAMERIA — a smiling model with a red bottle and a camellia"')
rep('alt="AI生成ファッションフィルム VELMARA の最終カット（濡れた夜の街を歩き去るモデル）"',
    'alt="Final frame of the AI-generated fashion film VELMARA — a model walking away on a wet night street"')
rep('alt="AI生成リップスティックフィルム GRENAT の最終カット（深紅の世界に赤と白のリップスティック2本）"',
    'alt="Final frame of the AI-generated lipstick film GRENAT — two lipsticks, red and white, in a deep red world"')
rep('aria-label="Instagramの投稿を読み込んで再生する"', 'aria-label="Load and play the Instagram post"', cnt=-1)
rep('<h3 class="aifilm-title">FUYUKAMERIA ― MAISON ÉCLAT</h3>',
    '<h3 class="aifilm-title">FUYUKAMERIA — MAISON ÉCLAT</h3>')
rep('<h3 class="aifilm-title">GRENAT ― ROUGE GRENAT</h3>',
    '<h3 class="aifilm-title">GRENAT — ROUGE GRENAT</h3>')
rep('<p class="aifilm-desc">架空のビューティーブランドを想定した広告動画サンプル（30秒）。企画・商品デザイン・プロンプト設計・編集までを制作。</p>',
    '<p class="aifilm-desc">A 30-second commercial film sample created for a fictional beauty maison: concept, product design, prompt design and editing.</p>')
rep('<p class="aifilm-desc">架空のシューズ＆バッグブランド『VELMARA』のAI生成ファッションフィルム（62秒）。夜の街とホテルのロビーを舞台に、企画・スタイリング・プロンプト設計・編集までを制作。</p>',
    '<p class="aifilm-desc">An AI-generated fashion film (62s) for VELMARA, a fictional maison of shoes and bags — a night piece set on wet streets and in a hotel lobby. Concept, styling, prompt design and edit produced in-studio.</p>')
rep('<p class="aifilm-desc">架空のリップスティックブランド『GRENAT』のAI生成フィルム（10秒）。深紅とゴールドの世界で、商品デザイン・静止画設計・生成・編集までを制作。</p>',
    '<p class="aifilm-desc">An AI-generated lipstick film (10s) for GRENAT, a fictional lipstick brand — set in a world of deep red and gold. Product design, still design, generation and editing produced in-studio.</p>')
rep('>Instagramで見る<span aria-hidden="true"> →</span></a>', '>View on Instagram<span aria-hidden="true"> →</span></a>', cnt=-1)

# --- サービス ---
rep('<h2>対応メニュー</h2>', '<h2>Services</h2>')
rep('<h3>ビューティー＆ファッション広告撮影</h3>\n        <p>コスメ、ジュエリー、ファッションブランドの広告ビジュアル撮影。商品の質感とモデルの表情を両立させる撮影設計を行います。</p>',
    '<h3>Beauty &amp; Fashion Advertising Photography</h3>\n        <p>Advertising visuals for cosmetics, jewellery and fashion brands — shoot design that holds both the texture of the product and the expression of the model.</p>')
rep('<h3>ブランド・商品イメージ撮影</h3>\n        <p>ブランドの世界観に沿ったイメージカット、商品撮影、イベント・プレビューの記録撮影。</p>',
    '<h3>Brand &amp; Product Imagery</h3>\n        <p>Image cuts in line with the brand world, product photography, and coverage of events and previews.</p>')
rep('<h3>人物・プロフィール撮影</h3>\n        <p>アーティスト、経営者、専門職の方のプロフィール撮影。用途に合わせた印象設計から対応します。</p>',
    '<h3>Portraits &amp; Profiles</h3>\n        <p>Profile photography for artists, executives and professionals, with the impression designed around the intended use.</p>')
rep('<h3>ディレクション・編集まで一貫対応</h3>\n        <p>撮影だけでなく、編集とディレクションまで一貫して対応。納品形態に合わせた最終仕上げまで行います。</p>',
    '<h3>Direction &amp; Editing, End to End</h3>\n        <p>Not only the shoot — direction and editing are handled consistently through to the final finish for each delivery format.</p>')
rep('<h3>AI動画生成</h3>\n        <p>撮影した写真をもとにした動画化、AI生成によるCM制作。実在のモデルが着用した商品撮影と、その動画化にも対応します。</p>',
    '<h3>AI Film Production</h3>\n        <p>Films built from photographed stills, and AI-generated commercial films. Real products can be photographed worn by a model and then made into video.</p>')
rep('<h3>まずはご相談ください</h3>\n        <p>企画段階からのご相談も歓迎です。撮影内容、スケジュール、ご予算に応じて最適な形をご提案します。</p>',
    '<h3>Start with a Conversation</h3>\n        <p>Enquiries are welcome from the planning stage. The best format is proposed around the content, schedule and budget of the shoot.</p>')

# --- プロフィール ---
rep('<h2>プロフィール</h2>', '<h2>Profile</h2>')
rep('<p>フォトグラファーの Katsutomo Izawa です。2013年よりプロフェッショナルとして活動し、東京を拠点に K\'s Creative Works として、ビューティー＆ファッション分野の広告撮影を中心に活動しています。</p>',
    '<p>I am Katsutomo Izawa, a photographer working professionally since 2013. Based in Tokyo as K\'s Creative Works, my work centres on advertising photography in beauty and fashion.</p>')
rep('<p>現場では、限られた時間と条件の中で「何を残すか」の判断を積み重ねることを大切にしています。クライアントの意図を汲み、被写体の魅力を最も伝わる形で切り取る撮影を心がけています。</p>',
    '<p>On set, I value the accumulation of judgement — deciding what to keep within limited time and conditions. The aim is always to understand the client\'s intent and capture the subject in the form that communicates their appeal most strongly.</p>')
print('part1 misses:', len(misses))
for m in misses: print('MISS:', m)

# --- お問い合わせ ---
rep('<h2>お問い合わせ</h2>', '<h2>Contact</h2>')
rep('<p>撮影のご相談は、下記フォーム、メール、または Instagram の DM からお気軽にどうぞ。</p>',
    '<p>For shoot enquiries, please use the form below, email, or Instagram DM.</p>')
rep('「<span class="req-mark">※必須</span>」のついた項目は、必ずご入力ください。',
    'Fields marked <span class="req-mark">* Required</span> must be completed.')
rep('<p>入力内容に不備があります。次の項目をご確認ください。</p>',
    '<p>Some fields need your attention. Please check the following items.</p>')
rep('<label for="cf-name">お名前<span class="req-mark">※必須</span></label>',
    '<label for="cf-name">Your name<span class="req-mark">* Required</span></label>')
rep('<p class="support" id="cf-name-support">例：山田 花子</p>',
    '<p class="support" id="cf-name-support">e.g. Jane Smith</p>')
rep('<label for="cf-company">会社名・ブランド名<span class="opt-mark">※任意</span></label>',
    '<label for="cf-company">Company / brand name<span class="opt-mark">Optional</span></label>')
rep('<p class="support" id="cf-company-support">個人でご相談の方は、空欄のままでかまいません。</p>',
    '<p class="support" id="cf-company-support">If you are enquiring as an individual, you may leave this blank.</p>')
rep('<label for="cf-email">メールアドレス<span class="req-mark">※必須</span></label>',
    '<label for="cf-email">Email address<span class="req-mark">* Required</span></label>')
rep('<p class="support" id="cf-email-support">返信先のアドレスをご入力ください。例：name@example.com</p>',
    '<p class="support" id="cf-email-support">Please enter the address where you would like the reply sent. e.g. name@example.com</p>')
rep('<label for="cf-type">お問い合わせ種別<span class="req-mark">※必須</span></label>',
    '<label for="cf-type">Enquiry type<span class="req-mark">* Required</span></label>')
rep('<p class="support" id="cf-type-support">ご相談の内容に最も近いものを選んでください。</p>',
    '<p class="support" id="cf-type-support">Please choose the option closest to your enquiry.</p>')
rep('<option value="" selected>選択してください</option>',
    '<option value="" selected>Please select</option>')
rep('<option value="撮影のご依頼">撮影のご依頼</option>',
    '<option value="撮影のご依頼">Commission a shoot</option>')
rep('<option value="AI動画生成">AI動画生成</option>',
    '<option value="AI動画生成">AI film production</option>')
rep('<option value="その他">その他</option>',
    '<option value="その他">Other</option>')
rep('<label for="cf-message">お問い合わせ内容<span class="req-mark">※必須</span></label>',
    '<label for="cf-message">Your enquiry<span class="req-mark">* Required</span></label>')
rep('<p class="support" id="cf-message-support">撮影の内容、ご希望の時期・場所、ご予算感など、分かる範囲でご記入ください。</p>',
    '<p class="support" id="cf-message-support">Please include whatever you can — the nature of the shoot, preferred timing and location, and your budget range.</p>')
rep('<button type="submit" class="submit-btn">入力内容を確認する</button>',
    '<button type="submit" class="submit-btn">Review your enquiry</button>')
rep('<p class="mail-note">ボタンを押すと確認画面が表示されます。内容をご確認のうえ、送信を確定してください。メールソフトは開きません。</p>',
    '<p class="mail-note">Pressing the button shows a confirmation screen. Please check the details and confirm to send. No mail app will open.</p>')
rep('<h3>入力内容の確認</h3>', '<h3>Review your enquiry</h3>')
rep('<p class="confirm-lead">以下の内容で送信します。よろしければ「この内容で送信する」を押してください。</p>',
    '<p class="confirm-lead">Your enquiry will be sent with the following details. If everything looks right, press "Send with these details".</p>')
rep('<div class="confirm-row"><dt>お名前</dt>', '<div class="confirm-row"><dt>Your name</dt>')
rep('<div class="confirm-row"><dt>会社名・ブランド名</dt>', '<div class="confirm-row"><dt>Company / brand</dt>')
rep('<div class="confirm-row"><dt>メールアドレス</dt>', '<div class="confirm-row"><dt>Email address</dt>')
rep('<div class="confirm-row"><dt>お問い合わせ種別</dt>', '<div class="confirm-row"><dt>Enquiry type</dt>')
rep('<div class="confirm-row"><dt>お問い合わせ内容</dt>', '<div class="confirm-row"><dt>Your enquiry</dt>')
rep('<button type="button" class="btn-ghost" id="backBtn">修正する</button>',
    '<button type="button" class="btn-ghost" id="backBtn">Go back and edit</button>')
rep('<button type="button" class="submit-btn" id="sendBtn">この内容で送信する</button>',
    '<button type="button" class="submit-btn" id="sendBtn">Send with these details</button>')
rep('<h3>送信が完了しました</h3>', '<h3>Your enquiry has been sent</h3>')
rep('<p>お問い合わせを受け付けました。入力いただいたメールアドレス宛に、折り返しご連絡いたします。</p>',
    '<p>Thank you — your enquiry has been received. A reply will be sent to the email address you provided.</p>')
rep('<p>フォームからうまく送れない場合は、メールまたは Instagram からもご連絡いただけます。</p>',
    '<p>If the form does not work for you, you can also get in touch by email or Instagram.</p>')
rep('>Instagramで相談する</a>', '>Enquire on Instagram</a>')

# --- フォームJSの文言 ---
rep("return v.trim() ? '' : '＊お名前が入力されていません。お名前を入力してください。';",
    "return v.trim() ? '' : '* Your name has not been entered. Please enter your name.';")
rep("if(!v) return '＊メールアドレスが入力されていません。返信を受け取れるメールアドレスを入力してください。';",
    "if(!v) return '* Your email address has not been entered. Please enter an address where you can receive a reply.';")
rep("if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) return '＊メールアドレスの形式が正しくありません。「@」とドメインを含む完全なアドレスを入力してください（例：name@example.com）。';",
    "if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) return '* The email address does not look complete. Please enter a full address including \"@\" and a domain (e.g. name@example.com).';")
rep("validate:function(v){ return v ? '' : '＊お問い合わせ種別が選択されていません。一覧から最も近いものを選択してください。'; }",
    "validate:function(v){ return v ? '' : '* No enquiry type has been selected. Please choose the closest option from the list.'; }")
rep("validate:function(v){ return v.trim() ? '' : '＊お問い合わせ内容が入力されていません。ご相談の概要を入力してください。'; }",
    "validate:function(v){ return v.trim() ? '' : '* Your enquiry has not been entered. Please briefly describe what you would like to discuss.'; }")
rep("document.getElementById('cv-company').textContent = value('cf-company') || '（未入力）';",
    "document.getElementById('cv-company').textContent = value('cf-company') || '(not provided)';")
rep("document.getElementById('cv-type').textContent = value('cf-type');",
    "document.getElementById('cv-type').textContent = document.getElementById('cf-type').selectedOptions[0].textContent;")
rep("'会社名・ブランド名': value('cf-company') || '（未入力）',",
    "'会社名・ブランド名': value('cf-company') || '(not provided)',")
rep("'送信元ページ': '日本語版',", "'送信元ページ': 'English',")
rep("sendBtn.textContent = '送信中…';", "sendBtn.textContent = 'Sending…';")
rep("sendBtn.textContent = 'この内容で送信する';", "sendBtn.textContent = 'Send with these details';")
rep("sendError.textContent = '送信できませんでした。通信環境をご確認のうえ、もう一度お試しください。うまくいかない場合は、下記のメールアドレスまたは Instagram からご連絡ください。';",
    "sendError.textContent = 'The enquiry could not be sent. Please check your connection and try again. If it still does not work, please use the email address or Instagram link below.';")

# --- ライトボックス ---
rep('aria-label="写真ビューア"', 'aria-label="Photo viewer"')
rep('aria-label="閉じる"', 'aria-label="Close"')
rep('aria-label="前の写真"', 'aria-label="Previous photo"')
rep('aria-label="次の写真"', 'aria-label="Next photo"')
rep("lbHint.textContent = coarse ? '左右にスワイプ／下のボタンで前後の写真へ' : '← → キー／左右のボタンで前後の写真へ';",
    "lbHint.textContent = coarse ? 'Swipe, or use the buttons below, to move between photos' : 'Use the arrow keys or the side buttons to move between photos';")

# --- モバイルメニューJS・AIフィルムのファサードJS ---
rep("btn.setAttribute('aria-expanded','false'); btn.setAttribute('aria-label','メニューを開く'); }",
    "btn.setAttribute('aria-expanded','false'); btn.setAttribute('aria-label','Open menu'); }")
rep("btn.setAttribute('aria-label',open?'メニューを閉じる':'メニューを開く');",
    "btn.setAttribute('aria-label',open?'Close menu':'Open menu');")
rep("iframe.title = 'Instagramに投稿されたAI生成動画 ' + t;",
    "iframe.title = 'AI-generated film ' + t + ' posted on Instagram';")

# NOTE (2026-11-14): Cloudflare Web Analytics beacon is embedded in index.html just before </body>;
# it is carried over to en/index.html automatically by this script. Do not remove it from index.html.
print('part2 misses:', len(misses))
for m in misses: print('MISS:', m)
if misses:
    print('ABORT: misses があるため en/index.html は書き出しません。置換ペアを index.html の現行文字列に合わせてください。')
    sys.exit(1)
os.makedirs('en', exist_ok=True)
open('en/index.html', 'w', encoding='utf-8').write(h)
print('EN page written', len(h))
