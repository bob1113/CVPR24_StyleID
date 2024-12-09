style=(
    "sty"
    "sty_atk_16_100_512_1_0_1_0_0"
    # "sty_atk_16_100_512_1_1_1_0_0"
    # "sty_atk_16_100_512_1_2_1_0_0"
    # "sty_atk_16_100_512_1_0_1_0_0_adain"
    # "sty_atk_16_100_512_1_1_1_0_0_adain"
    # "sty_atk_16_100_512_1_2_1_0_0_adain"
)

for gamma in 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
    for sty in ${style[@]}; do
        python util/copy_inputs.py \
            --cnt data/cnt \
            --sty data/${sty}

        cd evaluation
        python eval_artfid.py \
            --sty ../data/${sty}_eval \
            --cnt ../data/cnt_eval \
            --tar ../output/gamma_ablation/${gamma}${sty} >../output/gamma_ablation/${gamma}${sty}_artfid.txt
        python eval_histogan.py \
            --sty ../data/${sty}_eval \
            --tar ../output/gamma_ablation/${gamma}${sty} >../output/gamma_ablation/${gamma}${sty}_histo.txt
        cd ..
        echo ""
    done
done
