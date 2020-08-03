"""
Script para buildar os materiais das disciplinas
"""
import os
import subprocess
import shutil


CURR_PATH = os.path.realpath(os.path.dirname(__file__))
SRC_PATH = os.path.join(os.path.dirname(CURR_PATH), "2020.2")

ASSETS_FOLDER_NAME = "materiais"
ASSETS_OUT_PATH = os.path.join(CURR_PATH, "assets")

EXCLUDE_FILES_EXP = "_gab"


def call_cmd(cmd):
    """Roda uma instrução."""
    error = subprocess.call(cmd, shell=True)
    if error:
        print(f"Build failed! Error code: {error}")
    else:
        print("Success!")

    return error


def build_adoc(basename, ext, src_path, out_path):
    """Builda documentação em .adoc em HTML."""
    print(f"Building {src_path}\\{basename}{ext}...")
    filepath = os.path.join(src_path, f"{basename}{ext}")
    cmd = ["asciidoctor", filepath, "-D", out_path]
    call_cmd(cmd)


def build_office(basename, ext, src_path, out_path):
    """Builda documentação do office em pdf."""
    print(f"Building {src_path}\\{basename}{ext}...")
    filepath = os.path.join(src_path, f"{basename}{ext}")
    destpath = os.path.join(out_path, f"{basename}.pdf")
    cmd = ["officetopdf", filepath, destpath]
    call_cmd(cmd)


BUILDERS = {
    ".docx": build_office,
    ".pptx": build_office,
    ".adoc": build_adoc
}


def build_all_files():
    """Builda os arquivos para todas as disciplinas."""
    for disc_name in os.listdir(SRC_PATH):
        disc_path = os.path.join(SRC_PATH, disc_name)
        if os.path.isdir(disc_path):
            build_disc_files(disc_name)


def build_disc_files(disc_name):
    """Build os arquivos de uma disciplina"""
    disc_path = os.path.join(SRC_PATH, disc_name)
    assets_path = os.path.join(disc_path, ASSETS_FOLDER_NAME)

    out_path = os.path.join(ASSETS_OUT_PATH, disc_name)
    if not os.path.isdir(out_path):
        os.mkdir(out_path)

    copy_img(assets_path, out_path)
    for filename in os.listdir(assets_path):
        basename, ext = os.path.splitext(filename)
        if ext in BUILDERS.keys() and EXCLUDE_FILES_EXP not in basename:
            BUILDERS[ext](basename, ext, assets_path, out_path)


def copy_img(assets_path, out_path):
    """Copia as imagens para o destino."""
    print("Copying images...")
    out_img_path = os.path.join(out_path, "img")
    img_path = os.path.join(assets_path, "img")

    if os.path.isdir(img_path):
        if os.path.isdir(out_img_path):
            shutil.rmtree(out_img_path)

        shutil.copytree(img_path, out_img_path)


def clear_assets_path():
    """Limpa a pasta de destino dos materiais."""
    for disc_dir in os.listdir(ASSETS_OUT_PATH):
        shutil.rmtree(os.path.join(ASSETS_OUT_PATH, disc_dir))


def clear_log_files(dir_path):
    """Limpa recursivamente arquivos de log em um diretório."""
    for entry_name in os.listdir(dir_path):
        entry_path = os.path.join(dir_path, entry_name)
        if os.path.isdir(entry_path):
            clear_log_files(entry_path)
        if entry_name == "debug.log":
            os.remove(entry_path)


def main():
    """Entrada do script."""
    clear_assets_path()
    build_all_files()
    clear_log_files(CURR_PATH)


if __name__ == "__main__":
    main()
