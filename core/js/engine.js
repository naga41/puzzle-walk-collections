// core/js/engine.js

class PuzzleWalkEngine {
    constructor() {
        this.scenarioData = null;
        this.container = document.getElementById('main-container');
        this.bootScreen = document.getElementById('boot-screen');
        this.headerTitle = document.getElementById('header-title');
        this.init();
    }

    async init() {
        const urlParams = new URLSearchParams(window.location.search);
        
        // URLが勝手にエンコード（%3D等）されてしまった時のための安全策
        const rawSearch = decodeURIComponent(window.location.search);
        
        let contentId = urlParams.get('content');
        if (!contentId && rawSearch.includes('content=tokyo-rediscovery')) {
             contentId = 'tokyo-rediscovery';
        }
        contentId = contentId || 'tokyo-rediscovery'; 
        
        this.isDemoMode = urlParams.get('demo') === 'true' || rawSearch.includes('demo=true');

        try {
            const response = await fetch(`contents/${contentId}/scenario.json`);
            if (!response.ok) throw new Error('Scenario data not found');
            this.scenarioData = await response.json();
            
            this.applyTheme(this.scenarioData.theme);
            this.headerTitle.innerText = this.scenarioData.metadata.title;
            this.renderScenario(this.scenarioData.chapters);
            this.playPoeticPrologue(this.scenarioData.metadata.prologue, this.scenarioData.metadata.prologueImage);
            
        } catch (err) {
            console.error(err);
            this.container.innerHTML = `<div style="text-align:center; padding: 50px;">
                <p>……記憶を読み込めませんでした。</p>
                <a href="index.html" class="btn">ポータルに戻る</a>
            </div>`;
            this.bootScreen.style.display = 'none';
        }
    }

    applyTheme(theme) {
        if (!theme) return;
        const root = document.documentElement;
        for (const [key, value] of Object.entries(theme)) {
            root.style.setProperty(key, value);
        }
    }

    async playPoeticPrologue(prologueLines, prologueImage) {
        const logContainer = document.getElementById('boot-log');
        if (!prologueLines || prologueLines.length === 0) {
            this.bootScreen.style.display = 'none';
            return;
        }

        // Prologue Image support
        if (prologueImage) {
            this.bootScreen.style.backgroundImage = `linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('${prologueImage}')`;
            this.bootScreen.style.backgroundSize = 'cover';
            this.bootScreen.style.backgroundPosition = 'center';
        }

        // Tap guide
        const guide = document.createElement('div');
        guide.style.cssText = 'position:absolute; bottom:40px; left:0; width:100%; text-align:center; color:#f5f0e6; font-size:0.6rem; letter-spacing:4px; opacity:0; transition:opacity 1s; font-family:sans-serif; text-shadow: 0 0 10px rgba(0,0,0,1);';
        guide.innerText = 'TAP TO CONTINUE';
        this.bootScreen.appendChild(guide);
        setTimeout(() => guide.style.opacity = '0.4', 3000);

        const waitForNext = (waitTime) => {
            return new Promise(resolve => {
                let resolved = false;
                const done = () => {
                    if (resolved) return;
                    resolved = true;
                    this.bootScreen.removeEventListener('click', handler);
                    clearTimeout(timer);
                    resolve();
                };
                const handler = () => done();
                const timer = setTimeout(() => done(), waitTime);
                this.bootScreen.addEventListener('click', handler);
            });
        };

        const sleep = ms => new Promise(r => setTimeout(r, ms));

        for (let i = 0; i < prologueLines.length; i++) {
            const span = document.createElement('div');
            span.className = 'prologue-text';
            span.innerHTML = prologueLines[i];
            logContainer.innerHTML = '';
            logContainer.appendChild(span);
            
            await sleep(100);
            span.classList.add('show');
            
            // 文章の長さに応じた自動遷移時間（最低4秒、1文字100ms加算）
            const autoWaitTime = Math.max(4000, prologueLines[i].length * 100);
            await waitForNext(autoWaitTime);
            
            span.classList.remove('show');
            await sleep(1000); 
        }

        this.bootScreen.style.opacity = '0';
        guide.style.opacity = '0';
        setTimeout(() => this.bootScreen.style.display = 'none', 1500);
    }

    renderScenario(chapters) {
        this.container.innerHTML = '';
        
        chapters.forEach((ch, index) => {
            const section = document.createElement('section');
            section.className = `card ${index === 0 ? '' : 'locked'}`;
            section.id = `ch${ch.id}`;
            if (ch.type === 'briefing') {
                section.classList.add('briefing');
            }

            let html = `
                <div class="chapter-label">${ch.label}</div>
                <h2>${ch.title}</h2>
            `;

            if (ch.monologue) {
                html += `<div class="monologue">${ch.monologue}</div>`;
            }

            if (ch.imageUrl) {
                html += `<div class="prop-image-wrap">
                            <img src="${ch.imageUrl}" class="prop-image" alt="手記の画像">`;
                if (ch.imageCaption) {
                    html += `<div class="prop-caption">${ch.imageCaption}</div>`;
                }
                html += `</div>`;
            }

            if (ch.content) {
                html += `<div class="html-content">${ch.content.join('')}</div>`;
            }

            if (ch.postSolveHTML) {
                let displayHTML = ch.postSolveHTML;
                // 到着ボタンを自動挿入（challenge章）
                if (ch.type === 'challenge' && ch.nextChapterId) {
                    displayHTML += `<button class="btn btn-arrival" onclick="engine.handleArrival('${ch.nextChapterId}', '${ch.id}')">次なる観測地点に到着した</button>`;
                }
                // 結びボタンを自動挿入（final章）
                if (ch.type === 'final') {
                    displayHTML += `<button class="btn btn-arrival" onclick="engine.triggerFinalAha()">記憶の復元を完了し、結びを聞く</button>`;
                }
                html += `<div id="postsolve${ch.id}" class="postsolve-wrap" style="display:none; opacity:0; transition: opacity 1s ease; margin-top: 30px;">${displayHTML}</div>`;
            }

            // Input and Action Button
            if (ch.type === 'challenge' || ch.type === 'final') {
                html += `
                <div class="quest-card fade-in">
                    <div class="quest-label">ARCHIVE QUEST</div>
                    <div class="quest-instruction">${ch.instruction || 'この場所で『真実の一片』を特定せよ。'}</div>
                    <input type="text" id="ans${ch.id}" placeholder="キーワードを入力">
                    <button class="btn" onclick="engine.checkAnswer('${ch.id}', '${ch.answerKeyword}', ${ch.type === 'final'}, '${ch.nextChapterId}', '${ch.successMessage || '成功'}', '${ch.failureMessage || '失敗'}')">${ch.actionLabel}</button>
                </div>`;
                html += `<div id="feedback${ch.id}" class="feedback-msg"></div>`;
            } else if (ch.type === 'briefing') {
                // For briefing, button to unlock next
                if (this.isDemoMode) {
                    html += `<button class="btn" onclick="return false;" style="opacity:0.6; cursor:default; border-style:dashed; font-size: 0.8rem; line-height:1.8;">【プレビュー領域はここまで】<br><span style="font-size:0.7rem;">続きは実際の都市でお待ちしています</span></button>`;
                } else {
                    html += `<button class="btn" onclick="engine.unlockChapter('${ch.nextChapterId}')">${ch.actionLabel}</button>`;
                }
            }

            // Map and Hints
            if (ch.hint) {
                html += `
                    <div class="hint" onclick="document.getElementById('ht${ch.id}').style.display = document.getElementById('ht${ch.id}').style.display === 'block' ? 'none' : 'block'">[ 観測支援を求める ]</div>
                    <div id="ht${ch.id}" class="hint-text">${ch.hint}</div>
                `;
            }
            if (ch.mapLink) {
                html += `<div style="text-align: center;"><a href="${ch.mapLink.url}" class="btn btn-map" target="_blank">${ch.mapLink.label}</a></div>`;
            }

            section.innerHTML = html;
            this.container.appendChild(section);
        });
    }

    unlockChapter(chapterId, scroll = true) {
        if (this.isDemoMode) return;
        if (!chapterId) return;
        const target = document.getElementById(`ch${chapterId}`);
        if(target) {
            target.classList.remove('locked');
            if (scroll) {
                setTimeout(() => {
                    const yOffset = -80;
                    const y = target.getBoundingClientRect().top + window.pageYOffset + yOffset;
                    window.scrollTo({ top: y, behavior: 'smooth' });
                }, 400);
            }
        }
    }

    handleArrival(nextChapterId, currentChapterId) {
        const arrivalBtn = document.querySelector(`#postsolve${currentChapterId} .btn-arrival`);
        if (arrivalBtn) {
            arrivalBtn.disabled = true;
            arrivalBtn.innerText = "観測点に到達";
            arrivalBtn.style.opacity = "0.5";
        }
        this.unlockChapter(nextChapterId);
    }

    showFeedback(chapterId, msg, isSuccess) {
        const fb = document.getElementById(`feedback${chapterId}`);
        if (!fb) return;
        fb.innerText = msg;
        fb.style.color = isSuccess ? 'var(--text-main)' : 'var(--accent)';
        fb.style.opacity = '1';
        
        if (!isSuccess) {
            setTimeout(() => { fb.style.opacity = '0'; }, 3000);
        }
    }

    checkAnswer(chapterId, correctKeyword, isFinal, nextChapterId, successMsg, failMsg) {
        if (this.isDemoMode) return; // デモモード時は判定自体をブロック
        const inputElement = document.getElementById(`ans${chapterId}`);
        if (!inputElement) return;
        
        const val = inputElement.value;
        if (val.includes(correctKeyword)) {
            inputElement.disabled = true;
            this.showFeedback(chapterId, successMsg, true);
            
            const postSolveDiv = document.getElementById(`postsolve${chapterId}`);
            
            if (postSolveDiv) {
                postSolveDiv.style.display = 'block';
                void postSolveDiv.offsetWidth;
                postSolveDiv.style.opacity = '1';

                // 解けたあとの余韻を邪魔しないよう、入力フォーム等を非表示に
                const solveUI = document.querySelectorAll(`#ch${chapterId} .quest-card, #ch${chapterId} .hint, #ch${chapterId} .feedback-msg`);
                solveUI.forEach(el => el.style.display = 'none');

                // 解説・誘導セクションへスクロール
                setTimeout(() => {
                    const yOffset = -120;
                    const y = postSolveDiv.getBoundingClientRect().top + window.pageYOffset + yOffset;
                    window.scrollTo({ top: y, behavior: 'smooth' });
                }, 1000);
            }
        } else {
            this.showFeedback(chapterId, failMsg, false);
        }
    }

    triggerFinalAha() {
        // Trigger Aha Experience Mode (Slow ocean fade)
        document.body.classList.add('aha-mode');
        
        const finalReward = this.scenarioData.chapters.find(ch => ch.type === 'final')?.finalReward;
        
        setTimeout(() => {
            if (finalReward) {
                let html = `<div class="fade-in" style="text-align:center; padding-top: 40px;">
                    <h1 style="color:#bae6fd; font-size:1.8rem; letter-spacing: 4px; font-weight:300;">${finalReward.title}</h1>`;
                
                if (finalReward.imageUrl) {
                    html += `
                        <div class="delayed-show" style="margin: 40px -20px; overflow:hidden;">
                            <img src="${finalReward.imageUrl}" style="width:100%; border-radius:4px; opacity:0.85; filter: contrast(1.1) brightness(0.9); box-shadow: 0 10px 40px rgba(0,0,0,0.5);">
                        </div>
                    `;
                }

                html += `<div class="delayed-show" style="line-height:2.4; text-align:left; margin-top:30px; font-size: 1rem; font-weight: 300;">
                            ${finalReward.content.join('')}
                        </div>
                        <div class="clear-stamp" style="margin-top: 60px;">THE END</div>
                        <p class="fade-in" style="margin-top:20px; font-size:0.85rem; color:#7dd3fc; letter-spacing: 2px; animation-delay: 5s;">${finalReward.footer}</p>
                        <button class="btn fade-in" onclick="location.href='index.html'" style="border-color:#7dd3fc; color:#7dd3fc; margin:80px auto; width: 80%; animation-delay: 6s;">${finalReward.returnPortalLabel}</button>
                    </div>`;
                
                this.container.innerHTML = html;
            } else {
                 this.container.innerHTML = `<h1 class="fade-in" style="text-align:center">記憶の復元完了</h1>`;
            }
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }, 2000);
    }
}

// Global instance for inline onclick handlers
let engine;
window.addEventListener('DOMContentLoaded', () => {
    engine = new PuzzleWalkEngine();
});
