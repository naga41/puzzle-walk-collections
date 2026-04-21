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
        const contentId = urlParams.get('content') || 'tokyo-rediscovery'; 
        this.isDemoMode = urlParams.get('demo') === 'true';

        try {
            const response = await fetch(`contents/${contentId}/scenario.json`);
            if (!response.ok) throw new Error('Scenario data not found');
            this.scenarioData = await response.json();
            
            this.applyTheme(this.scenarioData.theme);
            this.headerTitle.innerText = this.scenarioData.metadata.title;
            this.renderScenario(this.scenarioData.chapters);
            this.playPoeticPrologue(this.scenarioData.metadata.prologue);
            
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

    async playPoeticPrologue(prologueLines) {
        const logContainer = document.getElementById('boot-log');
        if (!prologueLines || prologueLines.length === 0) {
            this.bootScreen.style.display = 'none';
            return;
        }

        // Sleep helper
        const sleep = ms => new Promise(r => setTimeout(r, ms));

        for (let i = 0; i < prologueLines.length; i++) {
            const span = document.createElement('div');
            span.className = 'prologue-text';
            span.innerHTML = prologueLines[i];
            logContainer.innerHTML = ''; // クリアして中央へ
            logContainer.appendChild(span);
            
            // フェードイン
            await sleep(100);
            span.classList.add('show');
            
            // 待機 (文章の長さに応じて)
            const waitTime = Math.max(2500, prologueLines[i].length * 100);
            await sleep(waitTime);
            
            // フェードアウト
            span.classList.remove('show');
            await sleep(1500); // 完全に消えるのを待つ
        }

        // 全て終わったら画面遷移
        this.bootScreen.style.opacity = '0';
        setTimeout(() => this.bootScreen.style.display = 'none', 2000);
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

            // Input and Action Button
            if (ch.type === 'challenge' || ch.type === 'final') {
                html += `<input type="text" id="ans${ch.id}" placeholder="キーワードを入力">`;
                html += `<button class="btn" onclick="engine.checkAnswer('${ch.id}', '${ch.answerKeyword}', ${ch.type === 'final'}, '${ch.nextChapterId}', '${ch.successMessage || '成功'}', '${ch.failureMessage || '失敗'}')">${ch.actionLabel}</button>`;
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

    unlockChapter(chapterId) {
        if (!chapterId) return;
        const target = document.getElementById(`ch${chapterId}`);
        if(target) {
            target.classList.remove('locked');
            setTimeout(() => {
                target.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }, 300);
        }
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
        const inputElement = document.getElementById(`ans${chapterId}`);
        if (!inputElement) return;
        
        const val = inputElement.value;
        if (val.includes(correctKeyword)) {
            inputElement.disabled = true;
            this.showFeedback(chapterId, successMsg, true);
            if (isFinal) {
                setTimeout(() => this.triggerFinalAha(), 1500);
            } else {
                setTimeout(() => this.unlockChapter(nextChapterId), 1500);
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
