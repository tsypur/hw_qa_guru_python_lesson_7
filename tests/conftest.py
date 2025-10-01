import os
import zipfile
import pytest


@pytest.fixture(scope="session")
def create_archive():
    resources_dir = 'resources'
    os.makedirs(resources_dir, exist_ok=True)
    archive_path = os.path.join(resources_dir, 'folder_zip.zip')

    with zipfile.ZipFile(archive_path, 'w') as zipf:
        files_to_add = ['file_example_pdf.pdf', 'file_example_XLSX.xlsx', 'file_example_csv.csv']

        for file in files_to_add:
            source_file_path = os.path.join('tmp', file)
            zipf.write(source_file_path, file)

    return archive_path