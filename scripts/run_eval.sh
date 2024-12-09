style=(
    # "sty"
    # "sty_atk_16_100_512_1_0_1_0_0"
    # "sty_atk_16_100_512_1_1_1_0_0"
    # "sty_atk_16_100_512_1_2_1_0_0"
    # "sty_atk_16_100_512_1_0_1_0_0_adain"
    # "sty_atk_16_100_512_1_1_1_0_0_adain"
    # "sty_atk_16_100_512_1_2_1_0_0_adain"
    # "sty_mifgsm_16_100_512_1_2_1_0_0"
    # "sty_nifgsm_16_100_512_1_2_1_0_0"
    "sty_vmifgsm_16_100_512_1_2_1_0_0"
)

# for sty in ${style[@]}; do
#     python util/copy_inputs.py \
#         --cnt data/cnt \
#         --sty data/${sty}
#
#     cd evaluation
#     python eval_artfid.py \
#         --sty ../data/${sty}_eval \
#         --cnt ../data/cnt_eval \
#         --tar ../output/${sty} >../output/${sty}_artfid.txt
#     python eval_histogan.py \
#         --sty ../data/${sty}_eval \
#         --tar ../output/${sty} >../output/${sty}_histo.txt
#     cd ..
#     echo ""
# done

# INFO: evaluation with orignial style
for sty in ${style[@]}; do
    python util/copy_inputs.py \
        --cnt data/cnt \
        --sty data/sty

    cd evaluation
    python eval_artfid.py \
        --sty ../data/sty_eval \
        --cnt ../data/cnt_eval \
        --tar ../output/${sty} >../output/eval_adv2clean/${sty}_artfid.txt
    python eval_histogan.py \
        --sty ../data/sty_eval \
        --tar ../output/${sty} >../output/eval_adv2clean/${sty}_histo.txt
    cd ..
    echo ""
done
