exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
user=int(input())
myd={}
for k,v in exam_marks.items():
    if v>=user:
        myd[k]=v
print(myd)