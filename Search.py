def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    # 初めの処理を判断するための変数
    i = 0
    while True:
        # 初期化処理
        if i == 0:
            # 探索対象の配列を設定
            search_array = sorted_array
            # 元々の探索対象である全ての要素を含んだ配列のインデックスを保持
            search_idx = [num for num in range(0,len(sorted_array))]

        # 最後の要素まで探し切った場合はループから抜け-1を返す
        if not search_array:
            break

        # 中間の値のインデックスを保持
        middle_idx = int(len(search_array)/2)

        # 中間の値と探したい値が一致した場合はそのインデックスを返す
        if search_array[middle_idx] == target_number:
            return search_idx[middle_idx]

        # 中間の値の方が探したい値よりも大きい場合は中間の値より小さい部分を探索対象にする
        # 元々の対象である全ての要素を含んだ配列のインデックスも絞る
        if search_array[middle_idx] > target_number:
            search_array = search_array[:middle_idx]
            search_idx = search_idx[:middle_idx]
        # 中間の値の方が探したい値よりも小さい場合は中間の値より大きい部分を探索対象にする
        # 元々の対象である全ての要素を含んだ配列のインデックスも絞る
        else:
            search_array = search_array[middle_idx+1:]
            search_idx = search_idx[middle_idx+1:]

        i+=1
        


    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()