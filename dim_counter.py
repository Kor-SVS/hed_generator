# Source of this code: https://github.com/r9y9/nnsvs/pull/81

from nnmnkwii.io import hts


def dim_count(hed_file_path: str = "korean_question.hed"):
    binary_dict, continuous_dict = hts.load_question_set(hed_file_path)
    in_rest_idx = 0
    in_lf0_idx = 0

    for n in range(len(binary_dict)):
        if binary_dict[n][0] == "C-Silence":
            in_rest_idx = n
            print("in_rest_idx:", in_rest_idx)
            break

    for n in range(len(continuous_dict)):
        if continuous_dict[n][0] == "e1_absolute_pitch":  # the absolute pitch of the current note
            in_lf0_idx = n + len(binary_dict)
            print("in_lf0_idx:", in_lf0_idx)
            break

    count_dim = 0
    lines = ""
    with open(hed_file_path, "r", encoding="utf-8") as ft:
        lines = ft.readlines()

    for line in lines:
        if line.startswith("QS") or line.startswith("CQS"):
            count_dim += 1

    print("count_dim:", count_dim)

    return in_rest_idx, in_lf0_idx, count_dim


if __name__ == "__main__":
    dim_count()
