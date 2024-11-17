import os
from django.shortcuts import render
from django.conf import settings
import nbformat

def list_notebooks_view(request):
    """Jupyter Notebook 파일 목록을 가져오는 뷰"""
    notebooks_dir = os.path.join(settings.BASE_DIR, 'notebooks')
    notebook_files = [f for f in os.listdir(notebooks_dir) if f.endswith('.ipynb')]
    return render(request, 'list_notebooks.html', {'notebook_files': notebook_files})

def notebook_results_view(request, notebook_name):
    """선택한 Jupyter Notebook의 결과를 보여주는 뷰"""
    notebook_path = os.path.join(settings.BASE_DIR, 'notebooks', notebook_name)
    
    if not os.path.exists(notebook_path):
        return render(request, 'error.html', {'message': 'Notebook 파일이 존재하지 않습니다.'})

    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)
    
    # 특정 셀 출력 결과 추출
    results = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code' and 'outputs' in cell:
            for output in cell['outputs']:
                if 'text' in output:  # 텍스트 결과 추출
                    results.append(output['text'])
    
    return render(request, 'notebook_results.html', {'results': results, 'notebook_name': notebook_name})
