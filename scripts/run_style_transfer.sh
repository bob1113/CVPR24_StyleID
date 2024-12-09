if [ -d "precomputed_feats" ]; then
    rm -r precomputed_feats # clear cached features
fi

style=(
    # "sty"
    # "sty_atk_16_100_512_1_0_1_0_0"
    # "sty_atk_16_100_512_1_1_1_0_0"
    # "sty_atk_16_100_512_1_2_1_0_0"
    # "sty_mifgsm_16_100_512_1_2_1_0_0"
    # "sty_nifgsm_16_100_512_1_2_1_0_0"
    "sty_vmifgsm_16_100_512_1_2_1_0_0"
    # "sty_vnifgsm_16_100_512_1_2_1_0_0"
    # "sty_vmifgsm_16_100_512_1_2_1_0_0"
    # "sty_atk_16_100_512_1_0_1_0_0_adain"
    # "sty_atk_16_100_512_1_1_1_0_0_adain"
    # "sty_atk_16_100_512_1_2_1_0_0_adain"
)

for sty in ${style[@]}; do
    python run_styleid.py \
        --cnt data/cnt \
        --sty data/${sty} \
        --output_path "output/${sty}" \
        --gamma 0.75 \
        --T 1.5
done

# for gamma in 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
#     for sty in ${style[@]}; do
#         python run_styleid.py \
#             --cnt data/cnt \
#             --sty data/${sty} \
#             --output_path "output/gamma_ablation/${gamma}${sty}" \
#             --gamma ${gamma} \
#             --T 1.5
#     done
# done
