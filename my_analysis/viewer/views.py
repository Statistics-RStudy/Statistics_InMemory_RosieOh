import nbformat
from django.shortcuts import render

def notebook_results_view(request):
    # Notebook 파일 경로
    notebook_path = os.path.join(settings.BASE_DIR, 'notebooks', 'ch01.ipynb')
    
    # Notebook 파일 로드
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)
    
    # 특정 셀 출력 결과 추출
    results = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code' and 'outputs' in cell:
            for output in cell['outputs']:
                if 'text' in output:  # 텍스트 결과 추출
                    results.append(output['text'])
    
    return render(request, 'notebook_results.html', {'results': results})
