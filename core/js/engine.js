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
        const contentId = urlParams.get('content') || 'tokyo-rediscovery'; // default fallback for now

        try {
            const response = await fetch(`contents/${contentId}/scenario.json`);
            if (!response.ok) throw new Error('Scenario data not found');
            this.scenarioData = await response.json();
            
            this.applyTheme(this.scenarioData.theme);
            this.headerTitle.innerText = this.scenarioData.metadata.title;
            this.renderScenario(this.scenarioData.chapters);
            this.runBootSequence(this.scenarioData.metadata.bootLogs);
            
        } catch (err) {
            console.error(err);
            this.container.innerHTML = `<div style="text-align:center; padding: 50px;">
                <p>エラーが発生しました: コンテンツを読み込めません。</p>
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

    runBootSequence(logs) {
        const logContainer = document.getElementById('boot-log');
        if (!logs || logs.length === 0) {
            this.bootScreen.style.display = 'none';
            return;
        }

        logs.forEach((text, i) => {
            setTimeout(() => {
                const div = document.createElement('div');
                div.className = 'typing-text';
                div.innerText = text;
                logContainer.appendChild(div);
            }, i * 800);
        });
        setTimeout(() => {
            this.bootScreen.style.opacity = '0';
            setTimeout(() => this.bootScreen.style.display = 'none', 1000);
        }, logs.length * 900);
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

            if (ch.content) {
                html += `<div class="html-content">${ch.content.join('')}</div>`;
            }

            // Input and Action Button
            if (ch.type === 'challenge' || ch.type === 'final') {
                html += `<input type="text" id="ans${ch.id}" placeholder="${ch.type === 'final' ? 'ENTER FINAL KEY...' : 'ENTER DECRYPT KEY...'}">`;
                html += `<button class="btn" onclick="engine.checkAnswer('${ch.id}', '${ch.answerKeyword}', ${ch.type === 'final'}, '${ch.nextChapterId}')">${ch.actionLabel || '復元を実行'}</button>`;
                if (ch.successMessage) {
                    html += `<div id="success${ch.id}" class="success-indicator">${ch.successMessage}</div>`;
                }
            } else if (ch.type === 'briefing') {
                // For briefing, button to unlock next
                html += `<button class="btn" onclick="engine.unlockChapter('${ch.nextChapterId}')">${ch.actionLabel || '開始する'}</button>`;
            }

            // Map and Hints
            if (ch.mapLink) {
                html += `<a href="${ch.mapLink.url}" class="btn btn-map" target="_blank">${ch.mapLink.label}</a>`;
            }
            if (ch.hint) {
                html += `
                    <div class="hint" onclick="document.getElementById('ht${ch.id}').style.display = document.getElementById('ht${ch.id}').style.display === 'block' ? 'none' : 'block'">[ 観測支援を要請 ]</div>
                    <div id="ht${ch.id}" class="hint-text">${ch.hint}</div>
                `;
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
            target.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }

    checkAnswer(chapterId, correctKeyword, isFinal, nextChapterId) {
        const inputElement = document.getElementById(`ans${chapterId}`);
        if (!inputElement) return;
        
        const val = inputElement.value;
        if (val.includes(correctKeyword)) {
            if (isFinal) {
                this.triggerFinalAha();
            } else {
                const successDiv = document.getElementById(`success${chapterId}`);
                if (successDiv) successDiv.style.display = 'block';
                setTimeout(() => this.unlockChapter(nextChapterId), 800);
            }
        } else {
            alert("! ACCESS DENIED: システムが適合しません。");
        }
    }

    triggerFinalAha() {
        // Trigger Aha Experience Mode
        document.body.classList.add('aha-mode');
        
        const finalReward = this.scenarioData.chapters.find(ch => ch.type === 'final')?.finalReward;
        
        setTimeout(() => {
            if (finalReward) {
                this.container.innerHTML = `
                    <div style="animation: fadeIn 3s; text-align:center; padding-top: 20px;">
                        <h1 style="color:#7dd3fc; font-size:1.8rem; letter-spacing: 4px; text-shadow: 0 0 15px var(--accent-glow);">${finalReward.title}</h1>
                        <div style="font-family:'Noto Serif JP'; line-height:2.4; text-align:left; margin-top:30px; font-size: 1rem;">
                            ${finalReward.content.join('')}
                        </div>
                        <p style="margin-top:60px; font-size:0.75rem; color:#38bdf8; letter-spacing: 2px;">${finalReward.footer}</p>
                        <button class="btn btn-map" onclick="location.href='index.html'" style="border-color:#7dd3fc; color:#7dd3fc; margin-bottom:80px;">${finalReward.returnPortalLabel || 'ポータルに戻る'}</button>
                    </div>
                `;
            } else {
                 this.container.innerHTML = `<h1 style="text-align:center">MISSION COMPLETE</h1>`;
            }
            window.scrollTo(0, 0);
        }, 1800);
    }
}

// Global instance for inline onclick handlers
let engine;
window.addEventListener('DOMContentLoaded', () => {
    engine = new PuzzleWalkEngine();
});
