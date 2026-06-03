import os
import json

base_path = '/home/ubuntu/Workspace/GitHub/pages/template/base_template.html'
out_path = '/home/ubuntu/Workspace/GitHub/pages/daily/daily_2026-06-03_3.html'
json_path = '/home/ubuntu/Workspace/GitHub/pages/daily.json'

with open(base_path, 'r', encoding='utf-8') as f:
    template = f.read()

# Replace title
template = template.replace('<title>Page Title - Termux Theme</title>', '<title>일일 투자 인사이트 (2026-06-03) - Daily Insight</title>')
template = template.replace('Termux <span class="gradient-text">Setup</span>', 'Daily <span class="gradient-text">Insight</span>')

content = """
            <div class="space-y-12 py-8">
                <!-- Header -->
                <div class="text-center py-10">
                    <h2 class="text-3xl md:text-5xl font-extrabold text-slate-900 dark:text-white mb-6">
                        글로벌 시장 동향 및 <span class="gradient-text">투자 인사이트</span>
                    </h2>
                    <p class="text-lg text-slate-600 dark:text-slate-400">
                        2026년 6월 3일 기준 한미 주요 증시 및 매크로 지표 심층 분석
                    </p>
                </div>

                <!-- 1. 한눈에 보기 -->
                <section class="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-slate-200 dark:border-gray-700 p-8 reveal">
                    <h3 class="text-2xl font-bold mb-6 flex items-center gap-2">
                        <span class="text-2xl">📊</span> 한눈에 보기
                    </h3>
                    <div class="bg-slate-50 dark:bg-gray-900 rounded-xl p-6 mb-8 border border-slate-100 dark:border-gray-700">
                        <ul class="space-y-3 text-slate-700 dark:text-slate-300 font-medium">
                            <li class="flex items-start gap-3">
                                <span class="text-blue-500 mt-1"><i class="fa-solid fa-check-circle"></i></span>
                                <span><strong>한국 증시:</strong> KOSPI 사상 최초 8,900선 장중 돌파 및 8,801.49(+0.15%) 마감. 개인의 기록적 순매수(6.3조)가 외국인 대규모 매도 물량(6.5조)을 방어.</span>
                            </li>
                            <li class="flex items-start gap-3">
                                <span class="text-blue-500 mt-1"><i class="fa-solid fa-check-circle"></i></span>
                                <span><strong>미국 증시:</strong> AI 인프라 기대감 확대로 S&P500 7,600선 최초 돌파 및 9거래일 연속 상승. M7 내 종목 장세 심화 (엔비디아/MSFT 강세 vs 알파벳 약세).</span>
                            </li>
                            <li class="flex items-start gap-3">
                                <span class="text-blue-500 mt-1"><i class="fa-solid fa-check-circle"></i></span>
                                <span><strong>매크로 지표:</strong> 중동발 리스크로 WTI 94달러 돌파, 고물가 우려에 따른 미국 3.75% 고금리 장기화로 원·달러 환율 1,520원대 고공행진 지속.</span>
                            </li>
                        </ul>
                    </div>
                    
                    <div class="overflow-x-auto rounded-lg border border-slate-200 dark:border-gray-700">
                        <table class="w-full text-left text-sm whitespace-nowrap">
                            <thead class="uppercase tracking-wider border-b-2 dark:border-gray-600 bg-slate-50 dark:bg-gray-900 text-slate-600 dark:text-slate-400">
                                <tr>
                                    <th class="px-6 py-4 font-bold">지수/지표</th>
                                    <th class="px-6 py-4 font-bold">현재가</th>
                                    <th class="px-6 py-4 font-bold">전일 대비</th>
                                    <th class="px-6 py-4 font-bold">핵심 동향</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-200 dark:divide-gray-700 bg-white dark:bg-gray-800">
                                <tr class="hover:bg-slate-50 dark:hover:bg-gray-700 transition-colors">
                                    <td class="px-6 py-4 font-semibold text-slate-900 dark:text-white">🇰🇷 KOSPI</td>
                                    <td class="px-6 py-4">8,801.49</td>
                                    <td class="px-6 py-4 text-red-500 font-medium">▲ 0.15%</td>
                                    <td class="px-6 py-4 text-slate-600 dark:text-slate-400">종가 기준 3거래일 연속 사상 최고치</td>
                                </tr>
                                <tr class="hover:bg-slate-50 dark:hover:bg-gray-700 transition-colors">
                                    <td class="px-6 py-4 font-semibold text-slate-900 dark:text-white">🇰🇷 KOSDAQ</td>
                                    <td class="px-6 py-4">1,026.03</td>
                                    <td class="px-6 py-4 text-blue-500 font-medium">▼ 2.29%</td>
                                    <td class="px-6 py-4 text-slate-600 dark:text-slate-400">상승 452종목 vs 하락 1226종목 (투심 악화)</td>
                                </tr>
                                <tr class="hover:bg-slate-50 dark:hover:bg-gray-700 transition-colors">
                                    <td class="px-6 py-4 font-semibold text-slate-900 dark:text-white">🇺🇸 S&P 500</td>
                                    <td class="px-6 py-4">7,609.78</td>
                                    <td class="px-6 py-4 text-red-500 font-medium">▲ 0.01%</td>
                                    <td class="px-6 py-4 text-slate-600 dark:text-slate-400">사상 최초 7,600선 돌파, 9거래일 상승</td>
                                </tr>
                                <tr class="hover:bg-slate-50 dark:hover:bg-gray-700 transition-colors">
                                    <td class="px-6 py-4 font-semibold text-slate-900 dark:text-white">🌍 USD/KRW</td>
                                    <td class="px-6 py-4">1,520.00</td>
                                    <td class="px-6 py-4 text-red-500 font-medium">▲ 급등</td>
                                    <td class="px-6 py-4 text-slate-600 dark:text-slate-400">강달러 장기화 및 안전자산 선호 심리 반영</td>
                                </tr>
                                <tr class="hover:bg-slate-50 dark:hover:bg-gray-700 transition-colors">
                                    <td class="px-6 py-4 font-semibold text-slate-900 dark:text-white">🛢️ WTI 원유</td>
                                    <td class="px-6 py-4">$94.00+</td>
                                    <td class="px-6 py-4 text-red-500 font-medium">▲ 상승</td>
                                    <td class="px-6 py-4 text-slate-600 dark:text-slate-400">중동 지정학적 위기 고조</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <!-- 2. 한국 시장 심층 분석 -->
                <section class="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-slate-200 dark:border-gray-700 p-8 reveal">
                    <h3 class="text-2xl font-bold mb-6 flex items-center gap-2">
                        <span class="text-2xl">🇰🇷</span> 한국 시장 심층 분석
                    </h3>
                    <div class="space-y-5 text-slate-700 dark:text-slate-300 leading-relaxed text-justify">
                        <p>
                            2026년 6월 초반 국내 증시는 극단적인 수급 공방전과 시장 양극화 양상을 동시에 보여주고 있습니다. KOSPI 지수는 전일 대비 +0.15% 상승한 8,801.49 포인트로 마감하며 장중 사상 최초로 8,900선을 터치하는 등 기념비적인 기록을 세웠습니다. 지수 자체는 3거래일 연속 종가 기준 사상 최고치를 경신했지만, 그 이면을 들여다보면 시장 체력에 대한 깊은 의문이 제기됩니다. 
                        </p>
                        <p>
                            수급 측면에서 가장 눈에 띄는 부분은 외국인 투자자의 전례 없는 엑소더스입니다. 코스피 시장에서 외국인은 무려 6조 5,941억 원에 달하는 기록적인 순매도를 쏟아냈으며, 이는 18거래일 연속 순매도 행진의 연장선입니다. 이러한 거센 매도 폭풍에도 불구하고 지수가 상승 마감할 수 있었던 이유는 개인 투자자들이 6조 3,489억 원이라는 막대한 자금으로 방어선을 구축했기 때문입니다. 기관 역시 2,409억 원을 순매수하며 힘을 보탰습니다. 
                        </p>
                        <p>
                            대형주 위주의 코스피가 근근이 상승을 지켜낸 반면, KOSDAQ 시장은 -2.29% 급락한 1,026.03 포인트로 마감하며 투심 악화를 여실히 보여주었습니다. 하락 종목 수(1,226개)가 상승 종목 수(452개)를 압도적으로 상회하여 투자자들의 체감 지수는 꽁꽁 얼어붙었습니다. 코스닥 시장 수급은 코스피와는 반대로 외국인이 3,106억 원, 기관이 1,285억 원을 순매수한 반면, 개인이 4,090억 원을 순매도하며 극명한 온도차를 나타냈습니다.
                        </p>
                        <p>
                            이러한 시장 분리의 근본적인 원인은 국내외 복합 위기 요인에 있습니다. 3.1%까지 뛰어오른 국내 소비자물가 지표는 금리 인하에 대한 기대를 무너뜨렸으며, 1,520원에 육박하는 고환율과 중동 지정학적 리스크가 맞물려 외국인들의 한국 증시 이탈을 부추기고 있습니다. 대형 수출주에 대한 저가 매수세와 밸류업 모멘텀이 코스피를 지지하고 있지만, 자금 조달에 취약한 중소형주가 다수인 코스닥은 거시경제 악화의 충격을 온몸으로 받고 있는 상황입니다.
                        </p>
                    </div>
                </section>

                <!-- 3. 미국 시장 심층 분석 -->
                <section class="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-slate-200 dark:border-gray-700 p-8 reveal">
                    <h3 class="text-2xl font-bold mb-6 flex items-center gap-2">
                        <span class="text-2xl">🇺🇸</span> 미국 시장 심층 분석
                    </h3>
                    <div class="space-y-5 text-slate-700 dark:text-slate-300 leading-relaxed text-justify">
                        <p>
                            글로벌 증시의 나침반 역할을 하는 뉴욕 증시는 AI가 만들어낸 '신대륙'을 발견한 듯한 강력한 랠리를 펼치고 있습니다. S&P 500 지수는 사상 처음으로 7,600선을 상향 돌파(7,609.78)하며 9거래일 연속 상승이라는 눈부신 기록을 세웠습니다. 나스닥 종합지수 또한 동반 사상 최고치를 경신하며, 중동 긴장과 고물가라는 거대한 매크로 악재조차 거침없이 무너뜨리는 AI 하드웨어와 인프라의 막강한 모멘텀을 증명했습니다. 
                        </p>
                        <p>
                            이번 상승장의 핵심 동력은 단연 매그니피센트 7(M7)과 AI 밸류체인 기업들입니다. 엔비디아(Nvidia)의 차세대 AI 반도체 수요에 대한 강한 자신감이 퍼지면서 마벨 테크놀로지(Marvell Technology)와 같은 관련주들이 큰 폭의 상승세를 보였습니다. 이와 함께 마이크로소프트(MSFT)는 'Microsoft Build 2026' 개발자 컨퍼런스를 개최하며 고도화된 AI 생태계를 선보여 랠리의 선봉장 역할을 확고히 했습니다.
                        </p>
                        <p>
                            그러나 M7 내부에서도 희비는 뚜렷하게 갈리고 있습니다. 막대한 AI 인프라 투자 자금을 조달하기 위해 800억 달러 규모의 자금 조달(주식 매각) 계획을 발표한 알파벳(Google)은 당일 약 -4% 가까이 급락하며 시장에 충격을 주었습니다. 이는 AI 기술 경쟁에서 우위를 점하기 위한 빅테크 기업들의 극단적인 자본 확충 경쟁이 주가 변동성으로 이어질 수 있음을 보여주는 대표적 사례입니다.
                        </p>
                        <p>
                            월가의 다수 전문가들은 현재의 상승장이 소수의 거대 기술주에 의해 견인되는 '브레드스 패러독스(Breadth Paradox, 시장 폭의 역설)' 현상을 겪고 있다고 분석합니다. 소수 종목의 폭발적 성장이 시장 전체의 지수를 끌어올리고 있지만, 다수 종목들의 약세가 가려져 있다는 것입니다. 고금리 환경 속에서 이러한 쏠림 현상이 심화됨에 따라, 향후 실적 이벤트 등에 의해 언제든 큰 폭의 기술적 조정을 맞이할 수 있다는 우려도 공존하고 있습니다.
                        </p>
                    </div>
                </section>

                <!-- 4. 매크로 & 글로벌 이슈 -->
                <section class="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-slate-200 dark:border-gray-700 p-8 reveal">
                    <h3 class="text-2xl font-bold mb-6 flex items-center gap-2">
                        <span class="text-2xl">🌍</span> 매크로 & 글로벌 이슈
                    </h3>
                    <div class="space-y-5 text-slate-700 dark:text-slate-300 leading-relaxed text-justify">
                        <p>
                            글로벌 매크로 환경은 주식시장의 강세와는 대조적으로 매우 불안정한 줄타기를 이어가고 있습니다. 미 연방준비제도(Fed)는 기준금리를 3.75% 수준에서 단단히 묶어두고 있습니다. 쉽게 잡히지 않는 '스티키(Sticky)'한 인플레이션과 지정학적 불안정성으로 인해 시장이 연초 기대했던 금리 인하 사이클은 사실상 뒤로 밀린 상태입니다. 한국은행 또한 이러한 연준의 기조 및 국내 물가 상황에 보폭을 맞추어 금리를 동결하며 긴축의 끈을 놓지 못하고 있습니다.
                        </p>
                        <p>
                            외환시장에서는 강달러의 거센 파도가 신흥국 통화를 덮치고 있습니다. 원·달러 환율은 심리적 저항선이었던 1,500원대를 훌쩍 넘어 1,520원선까지 치솟으며 극심한 변동성을 보이고 있습니다. 이는 미국 경제의 독보적인 강세, 금리 인하 지연 전망, 그리고 중동 리스크 장기화에 따른 글로벌 자금의 안전자산(달러) 쏠림 현상이 복합적으로 맞물린 결과입니다. 글로벌 금융위기 수준에 육박한 환율은 외국인 자금의 한국 증시 이탈을 가속화시키는 직접적인 요인입니다.
                        </p>
                        <p>
                            에너지 시장의 긴장감도 최고조에 달해 있습니다. 이란과의 종전 협상이 돌파구를 찾지 못한 채 교착 상태에 빠지면서 WTI(서부텍사스산원유)는 배럴당 94달러를 상회했고, 브렌트유 역시 96~97달러를 넘나들며 인플레이션 압력을 키우고 있습니다. 원유 수입 의존도가 절대적인 한국 경제의 특성상, 장기화되는 고유가는 무역수지 악화와 국내 물가 폭등을 야기하여 증시와 실물경제 전반에 치명적인 부담을 안겨주고 있습니다.
                        </p>
                    </div>
                </section>

                <!-- 5. 투자 시사점 & 전략 -->
                <section class="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-slate-200 dark:border-gray-700 p-8 reveal">
                    <h3 class="text-2xl font-bold mb-6 flex items-center gap-2">
                        <span class="text-2xl">💡</span> 투자 시사점 및 전략
                    </h3>
                    <div class="space-y-5 text-slate-700 dark:text-slate-300 leading-relaxed text-justify">
                        <p>
                            현재 글로벌 금융시장은 '미국 중심의 AI 테크주 환호'와 '고금리·고환율의 매크로 공포'가 극단적으로 공존하는 기형적인 국면입니다. 향후 1주일간 투자자들은 시장의 방향성을 뒤흔들 수 있는 양극단의 변수들을 세밀하게 모니터링해야 합니다. 단기적으로 포트폴리오의 수익률을 방어하기 위해서는 실적이 명확하게 뒷받침되는 <strong>미국 AI 주도주 및 하드웨어 인프라 핵심 기업</strong>에 비중을 두는 전략이 가장 합리적입니다. 다만, 쏠림 현상에 따른 밸류에이션 부담을 고려하여 추격 매수보다는 펀더멘털 기반의 분할 매수 접근이 필수적입니다.
                        </p>
                        <p>
                            국내 시장 투자에 있어서는 <strong>철저한 보수적 대응과 선제적인 리스크 관리</strong>를 권고합니다. 환율 1,520원대 돌파와 유가 94달러 안착이라는 악성 매크로 환경은 단기간 내 해소되기 어려우며, 외국인의 기조적인 순매도를 고착화할 가능성이 매우 높습니다. 따라서 무리한 지수 베팅은 자제하고, 고환율의 수혜를 구조적으로 누릴 수 있는 방산, 조선, 자동차 등 수출 주도형 가치주 섹터로 포트폴리오를 압축해야 합니다. 반대로 자금 조달 비용(금리) 상승에 취약한 중소형 성장주와 내수 소비재의 비중은 축소할 것을 권장합니다.
                        </p>
                        <p>
                            단기적으로 가장 예의주시해야 할 리스크 요인은 두 가지입니다. 첫째, <strong>알파벳의 유상증자 이슈가 촉발할 수 있는 빅테크 기업 전반의 연쇄적인 자금 조달 우려</strong>입니다. 이는 무한 경쟁에 돌입한 AI 인프라 투자의 부작용으로 작용하여 시장의 투심을 급격히 냉각시킬 수 있습니다. 둘째, <strong>중동 분쟁의 돌발적인 확전 가능성</strong>입니다. 유가가 100달러를 돌파하게 될 경우 시장은 금리 인하 기대 완전 소멸이라는 최악의 시나리오를 강제로 반영하게 될 것입니다. 맹목적인 상승 기대감을 경계하고, 변동성에 대비한 일정 수준의 현금 비중 확보가 그 어느 때보다 중요한 시점입니다.
                        </p>
                    </div>
                </section>
            </div>
"""

start_marker = '<!-- 여기에 새로운 콘텐츠를 추가하세요 -->'
end_marker = '</div>'
# We want to replace everything from the start marker to the </div> just before </main>
# Looking at the template, the structure is:
#             <!-- 여기에 새로운 콘텐츠를 추가하세요 -->
#             <div class="text-center py-20">
#                 ...
#             </div>
#             
#         </div>

# We can find <!-- 여기에 새로운 콘텐츠를 추가하세요 -->
# and replace the block up to the next </div>
import re
new_html = re.sub(
    r'<!-- 여기에 새로운 콘텐츠를 추가하세요 -->.*?</div>',
    content,
    template,
    flags=re.DOTALL
)

os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

# Now handle daily.json
if os.path.exists(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
else:
    data = []

new_entry = {
    "category": "시장동향",
    "date": "2026-06-03",
    "filename": "daily/daily_2026-06-03_3.html"
}
data.append(new_entry)

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Generated files successfully.")
