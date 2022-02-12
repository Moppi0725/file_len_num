print('行番号を振りたいファイルを指定してください: ',end = '')
open_file_name = input() # 読み込むファイル名を取得
file = open(open_file_name) # ファイルを開く
data = file.read() # ファイルのデータを読み込む
file.close() # ファイルを閉じる
program_data  = data.splitlines() #ファイルを行で分割
file_name = open_file_name.split('.') #拡張子とファイル名を分ける
output_file = open('num-{}.txt'.format(file_name[0]),'w') # 保存ファイルを開く
line_num = 1
print('===出力ファイルの内容===')
for i in program_data:
    print('{:>3}  {}'.format(line_num,i))
    text = '{:>3}  {}\n'.format(line_num,i)
    output_file.write(text)
    line_num += 1
output_file.close()
print('===以上のように行番号をつけたファイルを出力しました。===')
