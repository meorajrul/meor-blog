// Preflight the authored interaction and data consistency without a browser.
// This does not validate visual layout or browser rendering.
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert');
const rootPath=path.resolve(__dirname,'..');
const fragment=fs.readFileSync(path.join(rootPath,'to_human/quadrant-fragment.html'),'utf8');
const agencies=JSON.parse(fs.readFileSync(path.join(rootPath,'data/agencies.json'),'utf8'));
class Element {
  constructor(){this.children=[];this.dataset={};this.attrs={};this.events={};this.textContent='';}
  append(...es){this.children.push(...es);}
  replaceChildren(...es){this.children=[...es];}
  setAttribute(k,v){this.attrs[k]=v;}
  addEventListener(k,v){this.events[k]=v;}
}
const cells=Object.fromEntries(['met-transfer','met-retain','below-transfer','below-retain'].map(k=>[k,new Element()]));
const detail=new Element(),unknown=new Element(),root=new Element();
root.querySelector=s=>s==='[data-detail]'?detail:s==='[data-unknown]'?unknown:cells[s.match(/data-cell="([^"]+)"/)[1]];
let state;
const window={openai:{widgetState:{modelContent:{selectedAgency:'insken'}},setWidgetState:s=>{state=s;return Promise.resolve();}},addEventListener:()=>{}};
const document={getElementById:id=>{assert.equal(id,'msme-quadrant-261019');return root;},createElement:()=>new Element()};
const script=fragment.match(/<script>([\s\S]*?)<\/script>/)[1];
new vm.Script(script).runInNewContext({window,document});
assert.equal(Object.values(cells).flatMap(c=>c.children).length,11);
assert.equal(unknown.children.length,2);
for(const agency of agencies){
  const host=agency.performance_score===null?unknown:cells[(agency.performance_score>=70?'met':'below')+'-'+agency.institution_case];
  const button=host.children.find(b=>b.dataset.id===agency.id);
  assert(button,agency.id+' must appear in its supported quadrant or unknown group');
  assert.equal(button.textContent,agency.name);
  assert(button.attrs['aria-label'].includes(agency.performance_score===null?'unscored':String(agency.performance_score)));
  button.events.click();
  assert.equal(state.modelContent.selectedAgency,agency.id);
  assert.equal(button.attrs['aria-pressed'],'true');
  assert(detail.children[0].textContent.includes(agency.name));
  assert(detail.children[0].textContent.includes(agency.performance_score===null?'Unknown':agency.performance_score.toFixed(1)+'/100'));
}
assert.equal(cells['below-transfer'].children.length,0);
console.log(JSON.stringify({javascript_syntax:'passed',agency_placement:13,selection_interactions:13,unknowns_not_zero:2,browser_visual_layout:'not verified; local file URL blocked'},null,2));
