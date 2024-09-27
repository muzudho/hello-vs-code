#
# python font_of_terminal.py
#
# ターミナルのフォントを桁揃えできるようにしたい
#
# 参考：
#
# 📖 [プログラミングフォント2023年度版](https://qiita.com/chihayafuru/items/f48f088dbb231fd6d13b)
#       - 読むだけ
#
# 📖 [https://github.com/microsoft/cascadia-code/releases/tag/cascadia-next](https://github.com/microsoft/cascadia-code/releases/tag/cascadia-next)
#       - CascadiaNextJP.wght.ttf をダウンロードし、ファイルをダブルクリックして [インストール(I)] ボタンをクリックしてください
#               - otf がないので仕方なく ttf を選びました
#       - フォント名は 'Cascadia Next JP ExtraLight'
#       - 設定後、VSCode の再起動が必要かもしれません
#
# 📖 [エディターで使用するフォントの種類とサイズの設定](https://www.javadrive.jp/vscode/setting/index5.html#google_vignette)
#       - [File] - [Preferences] - [Settings] から Editor の Font Family を `'Cascadia Next JP ExtraLight', Consolas, monospace` に設定。これでエディターに表示されるフォントは等幅になる（ただし、罫線は半角のまま）
#
# 📖 [第２話：ターミナルを使いやすくしよう](https://baapuro.com/VScode/two/)
#       - [File] - [Preferences] - [Settings] から Terminal の Font Family を 'Cascadia Next JP ExtraLight', monospace に設定。これでターミナルに表示されるフォントは等幅になる（ただし、罫線は半角のまま）
#
# 📖 [windows Terminalの問題「特定の絵文字が半角（サイズ1/4）」「罫線の縦線が削除」が解決した。異文字セレクタ付けただけ]
#       - ［異文字セレクタ］の勉強にはなりますが、文字の桁揃えがずれるという問題は解決しません

import traceback


LOG_FILE_PATH = "logs/font_of_terminal.log"


########################################
# コマンドから実行時
########################################

if __name__ == '__main__':
    """コマンドから実行時"""

    try:
        # エディター上で見た目を合わせても、
        # ターミナルや、別のテキスト・エディターで見ると、ずれてしまう。
        # 罫線の `─` や、半角記号の `-` は、ひらがなの半分より横幅が長いから。
        text_1 = f"""\
ひらがなや、罫線、半角記号などにはフォントによって横幅が設定されており、方眼紙に収めたい日本語を考慮したフォントは 2024年現在 'Cascadia Next JP ExtraLight' ぐらいしか選択肢がありません。
しかもこの 'Cascadia Next JP ExtraLight' も、ターミナルでは罫線が半角文字の幅になってしまい、エディターとは表示がずれてしまいます。
例えば別のフォント、 `Cascadia Mono` フォントの罫線とひらがなは、エディターではだいたい桁が揃い、ターミナルでは桁がずれます。
エディターでは、罫線の `─` や、半角記号の `-` の横幅がひらがなの半分より長いからずれますが、逆にターミナルでは揃います。
ターミナルが理想的だが、ターミナルに合わせるとエディターでずれてしまい本末転倒。

┌────┐
│ずれる～│
└────┘\
"""

        print(text_1)


        # 罫線には、太字もある
        text_2 = f"""\
┌────┐
│ずれる～│
└────┘\
"""

        # 異字体セレクタを使って、罫線の太字の方を使う
        text_2 = text_2.replace('┌', f'┌{u'\uFE0E'}')
        text_2 = text_2.replace('─', f'─{u'\uFE0E'}')
        text_2 = text_2.replace('┐', f'┐{u'\uFE0E'}')
        text_2 = text_2.replace('│', f'│{u'\uFE0E'}')
        text_2 = text_2.replace('└', f'└{u'\uFE0E'}')
        text_2 = text_2.replace('┘', f'┘{u'\uFE0E'}')

        print(text_2)


        text_3 = f"""\
+--------+
|ずれる～|
+--------+\
"""

        print(text_3)

  
        # ファイルへログ出力
        with open(LOG_FILE_PATH, 'a', encoding='utf8') as f:
            f.write(f"""\
{text_1}

{text_2}

{text_3}""")


    except Exception as err:
        print(f"[unexpected error] {err=}  {type(err)=}")

        # スタックトレース表示
        print(traceback.format_exc())
