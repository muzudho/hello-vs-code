#
# python font_of_terminal.py
#
# ターミナルのフォントを桁揃えできるようにしたい
#
# 参考：
#
# 📖 [cascada-code](https://github.com/microsoft/cascadia-code)
#       - カスカディア・コードをインストールしてください
#           - 例えば otf/CascadiaMono-Regular.otf をダブルクリックして [インストール(I)]をクリック
#           - フォント名は `Cascadia Mono`
#
# 📖 [エディターで使用するフォントの種類とサイズの設定](https://www.javadrive.jp/vscode/setting/index5.html#google_vignette)
#       - [File] - [Preferences] - [Settings] から Editor の Font Family を `'Cascadia Mono', Consolas, monospace` に設定。これでエディターに表示されるフォントは等幅になる（ただし、罫線は半角のまま）
#
# 📖 [第２話：ターミナルを使いやすくしよう](https://baapuro.com/VScode/two/)
#       - [File] - [Preferences] - [Settings] から Terminal の Font Family を 'Cascadia Mono', monospace に設定。これでターミナルに表示されるフォントは等幅になる（ただし、罫線は半角のまま）
#
# 📖 [windows Terminalの問題「特定の絵文字が半角（サイズ1/4）」「罫線の縦線が削除」が解決した。異文字セレクタ付けただけ]
#       - 

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
Cascadia Code フォントの罫線とひらがなは、エディターではだいたい桁が揃い、ターミナルでは桁がずれる。
エディターでは、罫線の `─` や、半角記号の `-` の横幅がひらがなの半分より長いから。ターミナルでは等しい。
ターミナルが理想的だが、ターミナルに合わせるとエディターでずれてしまい本末転倒。
┌───────┐
│ずれる～│
└───────┘\
"""

        print(text_1)


        # 罫線には、太字もある
        text_2 = f"""\
┌───────┐
│ずれる～│
└───────┘\
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
Cascadia Code フォントの罫線とひらがなは、エディターではだいたい桁が揃い、ターミナルでは桁がずれる。
エディターでは、罫線の `─` や、半角記号の `-` の横幅がひらがなの半分より長いから。ターミナルでは等しい。
ターミナルが理想的だが、ターミナルに合わせるとエディターでずれてしまい本末転倒。
+-------+
|ずれる～|
+-------+\
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
