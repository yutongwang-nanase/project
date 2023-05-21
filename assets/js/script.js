let elements;
const { PI, sin, cos, random } = Math;
const TAU = 2 * PI;
const range = (n, m = 0) =>
  Array(n)
    .fill(m)
    .map((i, j) => i + j);
const map = (value, sMin, sMax, dMin, dMax) => {
  return dMin + ((value - sMin) / (sMax - sMin)) * (dMax - dMin);
};
const polar = (ang, r = 1, [x = 0, y = 0] = []) => [
  x + r * cos(ang),
  y + r * sin(ang)
];
const container = d3.select("#container");

const setStyle = (el, attrs) =>
  Object.entries(attrs).reduce((acc, [key, val]) => acc.style(key, val), el);
const setAttrs = (el, attrs) =>
  Object.entries(attrs).reduce((acc, [key, val]) => acc.attr(key, val), el);

const clipCords = range(6).map((i) => {
  const ang = map(i, 0, 6, 0, TAU);
  return polar(ang + PI / 2, 50);
});
const clipPathD = `M${[...clipCords, clipCords[0]]
  .map(([x, y]) => `L${x},${y}`)
  .join("")
  .slice(1)}`;

const svgRoot = container.append("svg");
setAttrs(svgRoot, { width: "0px", height: "0px" });
const defs = svgRoot.append("defs");
const clipPath = defs.append("clipPath");
setAttrs(clipPath, { id: "clipPath" });
const clipPathPath = clipPath.append("path");
setAttrs(clipPathPath, { d: clipPathD });

class Atom {
  constructor(parent, color) {
    this.element = parent.append("circle");
    setAttrs(this.element, { cx: 0, cy: 0, r: 4, fill: `${color}88` });

    this.seed1 = random() * TAU;
    this.seed2 = random() * TAU;
  }

  updatePosition(t) {
    const cx = 25 * sin(this.seed1 + t);
    const cy = 25 * sin(this.seed2 + t);
    setAttrs(this.element, { cx, cy });
  }
}

class Element {
  constructor(x, y, name, number, phase, color) {
    this.root = container.append("div");
    setStyle(this.root, {
      width: "5vw",
      height: "5vw",
      transform: `translate(${x}vw, ${y}vw)`,
      position: "absolute"
    });

    this.phase = phase;

    this.svg = this.root.append("svg");
    setAttrs(this.svg, { viewBox: "0 0 100 100", class: "svg" });
    this.group = this.svg.append("g");
    setAttrs(this.group, { transform: "translate(50,50)" });

    this.border = this.group.append("path");
    setAttrs(this.border, { d: clipPathD, fill: "none", stroke: `${color}88` });

    if (phase === "Solid") {
      this.solid = this.group.append("rect");
      setAttrs(this.solid, {
        x: -50,
        y: 18,
        width: 100,
        height: 60,
        fill: `${color}88`,
        style: "clip-path: url(#clipPath)"
      });
    }

    if (phase === "Liquid") {
      this.liquidPathA = this.group.append("path");
      setAttrs(this.liquidPathA, {
        d: "",
        fill: `${color}88`,
        style: "clip-path: url(#clipPath)"
      });
      this.liquidPathB = this.group.append("path");
      setAttrs(this.liquidPathB, {
        d: "",
        fill: `${color}44`,
        style: "clip-path: url(#clipPath)"
      });
    }

    if (phase === "Gas") {
      this.atoms = range(5).map(() => new Atom(this.group, color));
    }

    this.name = this.root.append("div").text(name);
    setAttrs(this.name, { class: "element-name" });
    setStyle(this.name, { color: `${color}88` });
    this.number = this.root.append("div").text(number);
    setAttrs(this.number, { class: "element-number" });
    setStyle(this.number, { color: `${color}88` });
  }

  update(t, path1, path2) {
    if (this.phase === "Liquid") {
      this.updateLiquid(path1, path2);
    }
    if (this.phase === "Gas") {
      this.updateAtoms(t);
    }
  }

  updateLiquid(path1, path2) {
    setAttrs(this.liquidPathA, { d: path1 });
    setAttrs(this.liquidPathB, { d: path2 });
  }

  updateAtoms(t) {
    this.atoms.forEach((atom) => {
      atom.updatePosition(t);
    });
  }
}

const categoryColors = {
  "diatomic nonmetal": "#3d7ea6",
  "noble gas": "#bc6ff1",
  "alkali metal": "#f05454",
  "alkaline earth metal": "#ffa36c",
  metalloid: "#64958f",
  "polyatomic nonmetal": "#8d93ab",
  "post-transition metal": "#c0e218",
  "transition metal": "#fcf876",
  lanthanide: "#949cdf",
  actinide: "#16697a"
};

const categoryDescriptions = {
  "diatomic nonmetal": "化学性质：二原子非金属指的是一些元素，它们在自然状态下以两个原子形式存在，如氧气（O2）、氮气（N2）和氯气（Cl2）。它们通常具有高电负性，形成共价键，并在化学反应中通常接受电子。\n\n在材料科学中的作用：二原子非金属在材料科学中具有广泛的应用。例如，氧气在燃烧和氧化反应中起重要作用，氮气在氨的合成中用作原料，氯气用于消毒和制备化学品等。",
  "noble gas": "化学性质：惰性气体是指位于周期表第18族的元素，包括氦（He）、氖（Ne）、氩（Ar）、氪（Kr）、氙（Xe）和氡（Rn）。它们具有非常稳定的电子结构，即满足八个外层电子或与氦类似的稳定结构。因此，它们很少与其他元素发生化学反应。\n\n在材料科学中的作用：惰性气体在材料科学中具有多种应用。例如，氦气用于气球充填和制冷，氩气常用于保护惰性气氛下的金属焊接和氧化物熔融，氪气用于激光技术和照明。",
  "alkali metal": "化学性质：碱金属是周期表第1族的元素，包括锂（Li）、钠（Na）、钾（K）、铷（Rb）、铯（Cs）和钫（Fr）。它们具有低电离能和高电导率，并且在与水反应时会释放出氢气并形成碱性溶液。\n\n在材料科学中的作用：碱金属在材料科学中有多种应用。例如，钠和钾常用于制备合金和催化剂，锂广泛用于电池技术，铷和铯用于光学器件和原子钟。",
  "alkaline earth metal": "化学性质：碱土金属是周期表第2族的元素，包括铍（Be）、镁（Mg）、钙（Ca）、锶（Sr）、钡（Ba）和镭（Ra）。它们具有较低的电离能和较高的金属反应性，与非金属反应形成离子化合物。与碱金属相比，碱土金属的反应性略低。\n\n在材料科学中的作用：碱土金属在材料科学中具有多种应用。例如，镁合金被广泛应用于航空航天、汽车制造和轻质结构材料。钙化合物用作建筑材料、牙科材料和蓄电池。钡和锶在电子器件和荧光材料中具有重要作用。",
  metalloid: "化学性质：类金属（也称为半金属）是一组元素，它们的性质介于金属和非金属之间。包括硼（B）、硅（Si）、锗（Ge）、砷（As）、锑（Sb）和碲（Te）。它们具有一些金属和非金属的特性，如可变的电导性、半导体性质和形成共价或离子化合物的能力。\n\n在材料科学中的作用：类金属在材料科学中有广泛的应用。硅是最常见的类金属，被广泛应用于半导体器件、太阳能电池和集成电路。硼用于制备高硬度材料，如硼化硅陶瓷。锑和碲用于制备热电材料和半导体。",
  "polyatomic nonmetal": "化学性质：多原子非金属是由多个原子组成的非金属元素。常见的多原子非金属包括磷（P）、硫（S）、硒（Se）和碘（I）。它们通常以分子形式存在，并且在化学反应中通常形成共价键。\n\n在材料科学中的作用：多原子非金属在材料科学中有多种应用。例如，硫被用于橡胶制品和染料的合成。磷化合物用作农业肥料和光子学器件。碘用于消毒剂、光敏材料和医药化学。",
  "post-transition metal": "化学性质：过渡后金属是指位于周期表中间区域的一组元素。它们包括铝（Al）、锌（Zn）、镓（Ga）、铟（In）、锡（Sn）、铅（Pb）和碲（Tl）。这些元素具有中等电离能和反应性，并且在化学反应中可以形成不同氧化态的离子。\n\n在材料科学中的作用：过渡后金属在材料科学中有多种应用。例如，铝是一种轻质且耐腐蚀的金属，广泛用于建筑、包装和航空航天工业。锌用于防腐蚀涂层和电池制造。铅在电子器件、弹丸和电池中有应用。",
  "transition metal": "化学性质：过渡金属是周期表中位于d区的一组元素。它们包括铁（Fe）、铜（Cu）、钴（Co）、镍（Ni）、铬（Cr）、钒（V）和铱（Ir）等。这些元素具有多个氧化态，形成复杂的配合物，并且在催化反应中起重要作用。\n\n在材料科学中的作用：过渡金属在材料科学中具有广泛的应用。例如，铁和钢是最常用的结构材料，铜被用于导电线和电子器件，钴用于合金和磁性材料，铬用于不锈钢制造，钒用于钢铁强化和催化剂。",
  lanthanide: "化学性质：镧系元素是指周期表中镧（La）到镧系最后一个元素镧（Lu）的一组元素。它们具有类似的电子结构，具有高度相似的化学性质。镧系元素常形成+3价离子，并在化学反应中形成稳定的配合物。\n\n在材料科学中的作用：镧系元素在材料科学中具有多种应用。它们被广泛用于制备催化剂、磁性材料、发光材料和陶瓷。镧系元素也是稀土磁体和高温超导材料的重要组成部分。",
  actinide: "化学性质：锕系元素是指周期表中锕（Ac）到锕系最后一个元素锕（Lr）的一组元素。它们是放射性元素，具有高密度和较高的电子数目。锕系元素的化学性质因其电子结构的特殊性而独特，包括多种氧化态和复杂的配位化学。\n\n在材料科学中的作用：锕系元素在材料科学中有一些应用。由于其放射性性质，锕系元素被用于核燃料和核能产业。一些锕系元素的同位素也用于放射治疗和医学诊断。此外，锕系元素的化合物在催化剂、发光材料和核工程中也具有重要作用。"
};

const categoryButtons = container.append("div");
setStyle(categoryButtons, {
  display: "flex",
  justifyContent: "center",
  marginBottom: "1rem"
});

Object.entries(categoryDescriptions).forEach(([category, description]) => {
  let categoryChinese;
  switch (category) {
    case "diatomic nonmetal":
      categoryChinese = "二元非金属";
      break;
    case "noble gas":
      categoryChinese = "惰性气体";
      break;
    case "alkali metal":
      categoryChinese = "碱金属";
      break;
    case "alkaline earth metal":
      categoryChinese = "碱土金属";
      break;
    case "metalloid":
      categoryChinese = "准金属";
      break;
    case "polyatomic nonmetal":
      categoryChinese = "多元非金属";
      break;
    case "post-transition metal":
      categoryChinese = "过渡金属后金属";
      break;
    case "transition metal":
      categoryChinese = "过渡金属";
      break;
    case "lanthanide":
      categoryChinese = "镧系元素";
      break;
    case "actinide":
      categoryChinese = "锕系元素";
      break;
    default:
      categoryChinese = category;
  }

  const button = categoryButtons.append("button").text(categoryChinese);
  setStyle(button, {
    background: `${categoryColors[category]}40`,
    color: "#fff",
    border: "none",
    borderRadius: "0.5rem",
    padding: "0.5rem 1rem",
    margin: "0 0.5rem",
    cursor: "pointer"
  });

  button.on("click", () => {
    const popup = container.append("div");
    setStyle(popup, {
      position: "absolute",
      top: "50%",
      left: "50%",
      transform: "translate(-50%, -50%)",
      padding: "1rem",
      background: "#fff",
      border: "1px solid #ccc",
      borderRadius: "0.5rem",
      boxShadow: "0 0.5rem 1rem rgba(0, 0, 0, 0.2)",
      zIndex: 9
    });

    const message = popup.append("p").html(`这是${categoryChinese}（${description.replace(/\n/g, "<br>")}）`);
    setStyle(message, { marginBottom: "0.5rem" });

    const closeButton = popup.append("button").text("关闭");
    setStyle(closeButton, {
      display: "block",
      margin: "1rem auto 0",
      padding: "0.5rem 1rem",
      background: "#ccc",
      border: "none",
      borderRadius: "0.5rem",
      cursor: "pointer"
    });

    closeButton.on("click", () => {
      popup.remove();
    });
  });
});


function createElements(data) {
  elements = data.map((element, index) => {
    const category = element.category;
    const name = element.symbol;
    const number = element.number;
    const phase = element.phase;
    const ix = element.xpos;
    const iy = element.ypos;
    const x = ix * 4.8 + ((iy + 1) % 2) * 2.5 - 2;
    const y = iy * 4.5 - 4;
    const color = categoryColors[category] || "#93abd3";

    return new Element(x, y, name, number, phase, color);
  });
}

let step = 0;

function animate() {
  step = (step + 1) % 100;
  const t = map(step, 0, 100, 0, TAU);

  const curve1 = range(10)
    .map((i) => {
      const ang = map(i, 0, 10, 0, TAU);
      const x = map(i, 0, 10, -50, 50);
      const y = 10 + 4 * sin(ang + t);
      return `L${x},${y}`;
    })
    .join("");

  const curve2 = range(10)
    .map((i) => {
      const ang = map(i, 0, 10, 0, TAU);
      const x = map(i, 0, 10, -50, 50);
      const y = 10 + 6 * sin(ang + t + PI);
      return `L${x},${y}`;
    })
    .join("");

  const path1 = `M50,10L50,50L-50,50L-50,10${curve1}`;
  const path2 = `M50,10L50,50L-50,50L-50,10${curve2}`;

  elements.forEach((element) => {
    element.update(t, path1, path2);
  });

  requestAnimationFrame(animate);
}

fetch("https://assets.codepen.io/3685267/periodic-table-data.json")
  .then((response) => response.json())
  .then((data) => {
    createElements(data.elements);
    animate();
  });




