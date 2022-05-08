def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    # pivotの値が最小値である時、無限ループになる場合があるため対処として1つずらす
    if pivot == min(array):
        pivot = array[1]

    #分割後のそれぞれの2つのグループを保持するリスト
    left = []
    right = []

    # 左、右それぞれから検索するためのインデックス
    min_idx = 0
    high_idx = len(array) - 1

    while True:
        # 隣り合う2つの値を入れ替えた場合は検索を終了し分割に進む
        if min_idx > high_idx:
            break

        # 一つ値を挟んで2つの値を入れ替えた場合は真ん中の値によって
        # 分割方法が異なるためpivotを元に分割位置を調整
        elif min_idx == high_idx:
            if array[min_idx] < pivot:
                min_idx+=1
            break

        # 先頭から検索しpivot以上の値が見つかったかつ末尾から検索しpivot未満の値が見つかった場合は
        # それらを入れ替えた上で検索のために両者とも1つ進める
        elif (array[min_idx] >= pivot) and (array[high_idx] < pivot): 
            array[min_idx],array[high_idx] = array[high_idx],array[min_idx]
            min_idx+=1
            high_idx-=1

        # 先頭から検索してpivot未満の値だった場合は1つ進める
        elif array[min_idx] < pivot:
            min_idx+=1

        # 末尾から検索してpivot以上(今回は重複がないためpivotより大きな値)だった場合は1つ進める
        elif array[high_idx] >= pivot:
            high_idx-=1

    # pivot未満とpivot以上のグループに分割
    left.extend(array[:min_idx])
    right.extend(array[min_idx:])

    # 分割したそれぞれに対して同様の処理を実行
    left = sort(left)
    right = sort(right)
    
    # 分割した2つの結果を合わせて返す
    return left + right


    # ここまで記述

if __name__ == '__main__':
    main()
