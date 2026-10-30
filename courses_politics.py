# Politics Courses (11-20) for The Paper Crane Academy
faculty = "Faculty of Politics, The Paper Crane Academy"

politics_courses = [
  {
    "id": "pol-political-philosophy",
    "title": "Classical & Modern Political Philosophy: Foundations of the State",
    "category": "Politics",
    "subcategory": "Political philosophy",
    "level": "Pre-university",
    "duration": "7 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "An inquiry into the foundational questions of political authority: Why should citizens obey the state? What is justice? Students examine the classical Greek polis (Plato and Aristotle), the emergence of the modern social contract (Hobbes, Locke, Rousseau), and contemporary theories of distributive justice (Rawls and Nozick).",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Compare Plato's philosopher-king in The Republic with Aristotle's constitutional polity in The Politics.",
      "Analyze the state of nature and social contract theories of Thomas Hobbes, John Locke, and Jean-Jacques Rousseau.",
      "Evaluate John Rawls's 'Original Position' and the Difference Principle versus Robert Nozick's entitlement theory.",
      "Synthesize concepts of negative versus positive liberty formulated by Isaiah Berlin."
    ],
    "modules": [
      {
        "title": "Module 1: The Social Contract Tradition: Hobbes, Locke, and Rousseau",
        "lessons": [
          {
            "id": "pol-phil-l1",
            "title": "The State of Nature and the Sovereign Leviathan",
            "body": """### The Justification of Sovereign Authority

The social contract tradition seeks to answer a radical question: How can free individuals be legitimately subjected to political coercion? To investigate this, contract theorists imagine a pre-political hypothetical condition: **the State of Nature**.

#### 1. Thomas Hobbes: The Leviathan (1651)
Writing amidst the carnage of the English Civil War, Hobbes posited a radically materialist view of human psychology. In the absence of a common power to keep all in awe, human beings exist in a state of perpetual war of every man against every man (*bellum omnium contra omnes*):
- Driven by competition for resources, fear (*diffidence*), and the pursuit of glory.
- In this state, there is no industry, no navigation, no culture, and:
  > *"The life of man, solitary, poor, nasty, brutish, and short."*
- To escape this intolerable anarchy, rational self-interest drives individuals to surrender their natural liberty through a covenant to an absolute sovereign—the **Leviathan**—who guarantees physical security.

#### 2. John Locke: The Second Treatise of Civil Government (1689)
Locke envisioned a fundamentally different state of nature governed by the **Law of Nature**, which dictates that no one ought to harm another in their life, health, liberty, or possessions.
- However, the state of nature suffers from severe 'inconveniences': the lack of an established known law, an indifferent judge, and execution power.
- Individuals form civil society for the mutual preservation of their **Property** (life, liberty, and estate).
- Because sovereignty remains conditional upon protecting natural rights, Locke formulates the revolutionary **Right of Revolution**: when a government systematically breaches trust, citizens are absolved from obedience.

#### 3. Jean-Jacques Rousseau: The Social Contract (1762)
Rousseau famously proclaimed:
> *"Man is born free, and everywhere he is in chains."*
- Rousseau rejects both Hobbesian absolutism and Lockean property protection. He proposes that individuals alienate themselves totally to the whole community, creating a collective moral body directed by the **General Will** (*volonté générale*), which aims exclusively at the common good rather than private factional interests.""",
            "readings": [
              {"label": "Thomas Hobbes, Leviathan, Chapters XIII & XIV (1651)", "url": "https://www.gutenberg.org/ebooks/3207"},
              {"label": "John Locke, Second Treatise of Government (1689)", "url": "https://www.gutenberg.org/ebooks/7370"},
              {"label": "Stanford Encyclopedia of Philosophy, Social Contract Theory", "url": "https://plato.stanford.edu/entries/contractarianism/"}
            ],
            "quiz": [
              {
                "q": "Why does John Locke argue that individuals leave the state of nature to form a commonwealth?",
                "options": [
                  "To surrender all individual freedoms to an absolute monarch.",
                  "Because the state of nature lacks established laws, impartial judges, and an executive power to protect private property and natural rights.",
                  "Because human nature is inherently incapable of rational cooperation.",
                  "To conquer neighboring sovereign nations."
                ],
                "answer": 1,
                "why": "Locke emphasizes that although the state of nature is not a state of constant war, the lack of an impartial arbiter creates insecurity, prompting individuals to institute government to preserve their life, liberty, and estate."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "pol-comparative-systems",
    "title": "Comparative Political Systems: Democracies, Authoritarianisms & Hybrid Regimes",
    "category": "Politics",
    "subcategory": "Democracy and governance",
    "level": "Undergraduate",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "A comparative analysis of political regime types and state structures. Students examine democratic institutions across presidential, parliamentary, and semi-presidential systems, analyze the survival strategies of non-democratic regimes (military juntas, single-party states, personalist dictatorships), and investigate competitive authoritarianism.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Categorize regime types using Robert Dahl's Polyarchy framework (contestation and inclusiveness).",
      "Compare the institutional dynamics of presidentialism versus parliamentarism (Juan Linz's perils of presidentialism).",
      "Analyze the mechanics of 'Competitive Authoritarianism' formulated by Levitsky and Way.",
      "Evaluate coalition bargaining dynamics and government stability in multi-party systems."
    ],
    "modules": [
      {
        "title": "Module 1: The Democratic Continuum and Executive Architectures",
        "lessons": [
          {
            "id": "pol-sys-l1",
            "title": "Parliamentarism vs Presidentialism: Juan Linz and Institutional Perils",
            "body": """### Comparative Executive Architectures

In comparative politics, the institutional relationship between the executive and the legislature forms the primary axis of democratic classification.

#### 1. The Parliamentary System
In parliamentary democracies (e.g., the United Kingdom, Germany, India, Japan):
- The executive is fused with and drawn directly from the legislative assembly.
- The Prime Minister or Chancellor is not directly elected by the public, but holds office by maintaining the **confidence** of a parliamentary majority.
- If the majority fractures, a government falls via a **motion of no confidence**, triggering either a new coalition negotiation or snap elections.
- Divided government is constitutionally impossible: the executive by definition commands a working legislative majority.

#### 2. The Presidential System
In presidential regimes (e.g., the United States, Brazil, Mexico):
- The President is elected independently of the legislature for a fixed calendar term.
- Both the executive and legislative branches possess independent **dual democratic legitimacy**—both can claim a direct mandate from the people.
- The President cannot dissolve the legislature, and the legislature cannot remove the President except through extraordinary quasi-criminal impeachment thresholds.

#### Juan Linz's 'Perils of Presidentialism'
In a landmark 1990 essay in the *Journal of Democracy*, political scientist Juan Linz observed that historically, presidential democracies outside the United States suffered far higher rates of democratic breakdown and military coups. Linz identified three systemic perils:
1. **Rigidity:** Fixed presidential terms make it impossible to swiftly replace an incompetent or deeply unpopular leader during an acute national crisis.
2. **Zero-Sum Politics (Winner-Take-All):** In presidential contests, 50.1% wins 100% of executive power; losers are completely shut out of governance for 4-6 years, heightening systemic political polarization.
3. **Dual Democratic Legitimacy & Deadlock:** When the presidency is held by one party and the legislature by another, and they disagree fundamentally on policy, the constitution provides no institutional mechanism to resolve the deadlock, inviting military or extra-constitutional intervention.""",
            "readings": [
              {"label": "Juan J. Linz, The Perils of Presidentialism, Journal of Democracy (1990)", "url": "https://www.journalofdemocracy.org/articles/the-perils-of-presidentialism/"},
              {"label": "Arend Lijphart, Patterns of Democracy (Yale University Press)", "url": "https://yalebooks.yale.edu/book/9780300172027/patterns-of-democracy/"}
            ],
            "quiz": [
              {
                "q": "According to Juan Linz, why do presidential systems exhibit greater institutional vulnerability to democratic breakdown than parliamentary systems?",
                "options": [
                  "Because presidents are appointed by supreme courts rather than voters.",
                  "Because dual democratic legitimacy creates irreconcilable gridlock between executive and legislative majorities with no constitutional mechanism to break the impasse.",
                  "Because parliamentary systems have no written constitutions.",
                  "Because presidential cabinets are too large to make swift decisions."
                ],
                "answer": 1,
                "why": "Linz argued that when an independently elected president confronts a hostile legislature with its own democratic mandate, neither has constitutional supremacy over the other, frequently precipitating constitutional crises."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "pol-democratic-backsliding",
    "title": "Democratic Backsliding, Institutional Capture & Populism",
    "category": "Politics",
    "subcategory": "Democracy and governance",
    "level": "Undergraduate",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "An urgent inquiry into the contemporary crisis of liberal democracy. Moving beyond classical military coups, this course explores how elected leaders dismantle constitutional checks from within—weaponizing the law, capturing supreme courts, curtailing independent media, and exploiting cultural grievances through populist rhetoric.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Distinguish between classical authoritarian breakdowns (coups d'état) and incremental democratic erosion.",
      "Analyze the 'autocratic legalism' playbook: court packing, electoral law revision, and tax investigations.",
      "Examine Cas Mudde's ideational definition of populism (pure people vs corrupt elite).",
      "Evaluate institutional and civil society safeguards that foster democratic resilience."
    ],
    "modules": [
      {
        "title": "Module 1: How Modern Democracies Erode from Within",
        "lessons": [
          {
            "id": "pol-back-l1",
            "title": "Autocratic Legalism and the Erosion of Unwritten Democratic Norms",
            "body": """### The Subversion of Democratic Institutions

In the 20th century, democracies predominantly died at the hands of men with guns: violent military coups (*golpes de estado*), tanks surrounding presidential palaces, and martial law decrees.

In the 21st century, as Harvard political scientists Steven Levitsky and Daniel Ziblatt demonstrate in *How Democracies Die* (2018), democratic backsliding occurs at the ballot box. Elected leaders use the very instruments of democracy to subvert it slowly, legally, and invisibly:

#### The Three Tactics of 'Autocratic Legalism'
1. **Capturing the Referees:** Packing constitutional courts, appointing partisan loyalists to supreme auditing bodies, and purging public prosecutors to ensure that government corruption goes unpunished while political opponents face immediate criminal scrutiny.
2. **Sidelining Opponents and the Press:** Rather than outright banning opposition parties or shutting down television stations, illiberal governments use state advertising revenues, tax audits, and regulatory licenses to starve independent media, while subsidizing friendly oligarchs to buy up news networks.
3. **Tilting the Playing Field:** Rewriting electoral rules, redrawing constituencies, and controlling campaign financing so that even when opposition parties win a majority of popular votes, they cannot win a legislative majority.

#### The Unwritten Guardrails of Democracy
Constitutions alone cannot protect democracy. Written laws must be reinforced by two vital unwritten democratic norms:
1. **Mutual Toleration:** The agreement that political rivals are not existential enemies or traitors, but legitimate political competitors who have an equal right to govern if they win elections.
2. **Institutional Forbearance:** The self-restraint of political actors from exercising legal powers to the absolute legal maximum when doing so would subvert the underlying spirit of the democratic order (avoiding 'constitutional hardball').""",
            "readings": [
              {"label": "Steven Levitsky & Daniel Ziblatt, How Democracies Die (Crown, 2018)", "url": "https://www.penguinrandomhouse.com/books/562246/how-democracies-die-by-steven-levitsky-and-daniel-ziblatt/"},
              {"label": "Kim Lane Scheppele, Autocratic Legalism, 85 University of Chicago Law Review (2018)", "url": "https://lawreview.uchicago.edu/print-archive/autocratic-legalism"}
            ],
            "quiz": [
              {
                "q": "What is 'autocratic legalism' as defined by contemporary constitutional scholars?",
                "options": [
                  "A sudden military overthrow of an elected government.",
                  "The process whereby elected leaders use formally legal and constitutional procedures to incrementally hollow out democratic checks and balances.",
                  "The voluntary dissolution of a supreme court by its chief justice.",
                  "A transition from a monarchy to an anarchic commune."
                ],
                "answer": 1,
                "why": "Autocratic legalism occurs when authoritarians use existing legal statutes, constitutional amendments, and administrative regulations to consolidate power without ever overtly breaking the formal law."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "pol-electoral-systems",
    "title": "Electoral Systems, Gerrymandering & Representation",
    "category": "Politics",
    "subcategory": "Elections and political institutions",
    "level": "Pre-university",
    "duration": "5 weeks (3 hours/week)",
    "instructor": faculty,
    "description": "An investigation of the mathematical and institutional mechanics of elections. This course explores how different voting systems (First-Past-The-Post, Proportional Representation, Ranked Choice / Single Transferable Vote) translate citizen preferences into legislative seats, alongside the spatial mechanics of partisan gerrymandering and voter suppression.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Contrast Single-Member Plurality (FPTP) with Party-List Proportional Representation and STV.",
      "Explain Duverger's Law and the mechanical and psychological factors shaping party systems.",
      "Analyze techniques of partisan gerrymandering: Packing and Cracking.",
      "Calculate measures of partisan asymmetry such as the Efficiency Gap."
    ],
    "modules": [
      {
        "title": "Module 1: Electoral Mechanics and Duverger's Law",
        "lessons": [
          {
            "id": "pol-elec-l1",
            "title": "Plurality vs Proportionality: Duverger's Law and Seat Allocation",
            "body": """### The Political Consequences of Electoral Systems

Electoral systems are the institutional translation engines of democracy: they convert votes cast by citizens into seats won by parties and politicians.

#### 1. Majoritarian / Plurality Systems (First-Past-The-Post / FPTP)
In single-member district plurality systems (e.g., US House, UK House of Commons, India's Lok Sabha):
- The territory is divided into discrete geographic districts, each electing one representative.
- The candidate who wins a plurality (the most votes, even if far short of an absolute majority) wins the entire seat.
- All votes cast for losing candidates are mathematically discarded.

#### 2. Proportional Representation (PR)
In proportional systems (e.g., Netherlands, Sweden, Israel):
- Multi-member districts or a single national district are used.
- Seats are awarded in close proportion to the total percentage of the national popular vote won by each party list, subject to an electoral threshold (e.g., 5% in Germany).

#### Duverger's Law
Formulated by French sociologist Maurice Duverger in the 1950s, this is one of the most famous empirical regularities in political science:
> *"The simple-majority single-ballot system favours the two-party system."*

Duverger demonstrated that this occurs through two compounding effects:
1. **The Mechanical Effect:** Plurality systems severely penalize third parties whose vote share is distributed evenly across the country, denying them seats unless their vote is concentrated geographically.
2. **The Psychological Effect:** Voters realize that voting for their preferred third-party candidate is likely a 'wasted vote', leading them to strategically defect to the lesser of two viable evils. Politicians, in turn, choose to organize within the two major broad-tent parties.""",
            "readings": [
              {"label": "Maurice Duverger, Political Parties: Their Organization and Activity (1954)", "url": "https://www.britannica.com/topic/Duvergers-law"},
              {"label": "ACE Electoral Knowledge Network, Comparative Electoral Systems Guide", "url": "https://aceproject.org/ace-en/topics/es"}
            ],
            "quiz": [
              {
                "q": "What two mechanisms drive Duverger's Law towards a two-party system under First-Past-The-Post?",
                "options": [
                  "A constitutional ban on third parties and mandatory voter registration.",
                  "The mechanical penalization of third parties under plurality seat rules and the psychological strategic voting that avoids wasting votes on non-viable candidates.",
                  "Universal proportional quotas and presidential veto power.",
                  "Compulsory voting and hereditary legislative appointments."
                ],
                "answer": 1,
                "why": "Duverger identified the mechanical hurdle of winning a plurality in single-member districts combined with the psychological reluctance of voters to throw away their vote on uncompetitive third parties."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "pol-totalitarianism-power",
    "title": "Totalitarianism & Ideological Power: The Thought of Hannah Arendt",
    "category": "Politics",
    "subcategory": "Political philosophy",
    "level": "Undergraduate",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "A close philosophical examination of 20th-century political catastrophe through the seminal works of Hannah Arendt. Students analyze The Origins of Totalitarianism, the destruction of the public sphere, the manipulation of loneliness and atomization, Eichmann in Jerusalem and the 'banality of evil', and Arendt's vision of political action in The Human Condition.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Distinguish totalitarianism from classical tyranny and authoritarian military dictatorship.",
      "Analyze the psychological preconditions of totalitarian rule: Loneliness, atomization, and terror.",
      "Deconstruct Arendt's controversial thesis on the 'Banality of Evil' regarding Adolf Eichmann.",
      "Synthesize Arendt's concept of the vita activa: Labor, Work, and Action in the public sphere."
    ],
    "modules": [
      {
        "title": "Module 1: The Totalitarian Phenomenon and the Banality of Evil",
        "lessons": [
          {
            "id": "pol-ar-l1",
            "title": "Ideology, Terror, and the Banality of Evil",
            "body": """### The Novel Form of Modern Tyranny

In *The Origins of Totalitarianism* (1951), Hannah Arendt argued that Nazi Germany and Stalinist Soviet Union were not mere continuations of classical despotism. Classical tyrants sought to monopolize political power while leaving social, artistic, and private life largely unmolested. Totalitarianism seeks total subjugation of the entire human being:

1. **The Destruction of the Common World:** Totalitarian regimes weaponize all-encompassing ideological fictions that replace complex factual reality with a single pseudo-scientific narrative (e.g., racial struggle in Nazism; historical dialectical materialism in Stalinism).
2. **Loneliness and Atomization:** Totalitarianism requires the systematic destruction of all secondary associations—churches, independent trade unions, civic clubs, and even the family unit. Once isolated, atomized individuals lose the capacity for critical common-sense judgment.
3. **Terror as the Essence of the Regime:** Terror is not merely an instrument to eliminate political opponents; it is the permanent operational principle of the state, used to enforce total ideological conformity even when all actual opposition has ceased.

#### The Banality of Evil (1963)
Covering the 1961 trial of Nazi bureaucrat Adolf Eichmann in Jerusalem for *The New Yorker*, Arendt was struck not by a monstrous demonic sadist, but by an utterly ordinary, mediocre bureaucrat who spoke in stock phrases and clichés:
- Eichmann had surrendered the fundamental human capacity to **think**—to pause and imagine reality from the perspective of another person.
- Evil on an industrial scale was performed by men whose primary motive was organizational diligence, career advancement, and obedience to administrative routine.
- Hence Arendt's haunting conclusion: the most catastrophic evil in history was committed by thoughtless bureaucrats who had abdicated moral conscience.""",
            "readings": [
              {"label": "Hannah Arendt, The Origins of Totalitarianism (1951)", "url": "https://www.penguinrandomhouse.com/books/299690/the-origins-of-totalitarianism-by-hannah-arendt/"},
              {"label": "Hannah Arendt, Eichmann in Jerusalem: A Report on the Banality of Evil (1963)", "url": "https://www.penguinrandomhouse.com/books/299689/eichmann-in-jerusalem-by-hannah-arendt/"},
              {"label": "Stanford Encyclopedia of Philosophy, Hannah Arendt", "url": "https://plato.stanford.edu/entries/arendt/"}
            ],
            "quiz": [
              {
                "q": "What did Hannah Arendt mean by the phrase 'the banality of evil' in her report on Adolf Eichmann?",
                "options": [
                  "That the Holocaust was not a serious crime.",
                  "That catastrophic evil can be carried out by ordinary, thoughtless individuals who mechanically execute bureaucratic orders without critical moral reflection.",
                  "That only low-level soldiers were responsible for war crimes.",
                  "That evil is an unavoidable biological instinct in all human societies."
                ],
                "answer": 1,
                "why": "Arendt's thesis was that Eichmann was not a fanatical demonic monster, but a terrifyingly normal bureaucrat whose evil stemmed from an utter failure to think from the standpoint of others."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "pol-political-ideologies",
    "title": "Political Ideologies: Liberalism, Conservatism, Socialism & Nationalism",
    "category": "Politics",
    "subcategory": "Political ideologies",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "A systematic survey of the major ideological worldviews that have defined the modern political landscape. Students deconstruct the core axioms, views on human nature, conceptions of freedom, and policy visions of Classical and Modern Liberalism, Traditional and Social Conservatism, Democratic Socialism, and Civic versus Ethnic Nationalism.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Compare classical liberalism (Locke, Smith) with modern welfare liberalism (Rawls, Keynes).",
      "Analyze the conservative emphasis on tradition, social order, and organic community (Edmund Burke).",
      "Deconstruct democratic socialism and social democracy's critique of unregulated capitalism.",
      "Distinguish between inclusive civic nationalism and exclusionary ethnic/cultural nationalism."
    ],
    "modules": [
      {
        "title": "Module 1: The Spectrum of Political Ideologies",
        "lessons": [
          {
            "id": "pol-ideo-l1",
            "title": "Liberalism vs Conservatism: Individual Autonomy vs Organic Social Order",
            "body": """### The Ideological Architecture of the West

Political ideologies are coherent sets of normative ideas and values that provide a worldview, diagnose social injustices, and prescribe a program of political action.

#### 1. The Liberal Tradition
Liberalism places the moral primacy of the **individual** at the center of political life:
- **Classical Liberalism:** Championed by John Locke, Adam Smith, and J.S. Mill. It insists on negative liberty (freedom from state interference), private property, free markets, and the night-watchman state (*laissez-faire*).
- **Modern / Social Liberalism:** Developed in the late 19th and 20th centuries by T.H. Green, Leonard Hobhouse, and John Rawls. It recognizes that poverty, disease, and unregulated monopolies restrict real human freedom just as severely as state censorship. It embraces positive liberty: the state must guarantee baseline education, social welfare, and healthcare so that all citizens possess the substantive capability to flourish.

#### 2. The Conservative Tradition
Modern conservatism emerged in Edmund Burke's *Reflections on the Revolution in France* (1790) as a critique of radical abstract utopianism:
- Society is not a mechanical machine that can be dismantled and reconstructed overnight according to abstract intellectual theories.
- Society is an organic contract between three generations: *the dead, the living, and those yet to be born*.
- Burke warned that destroying ancient institutions (churches, traditions, common-law habits) unleashes anarchy and military despotism. Conservatism values custom, prudence, social order, and gradual evolutionary reform (*reform in order to preserve*).""",
            "readings": [
              {"label": "Edmund Burke, Reflections on the Revolution in France (1790)", "url": "https://www.gutenberg.org/ebooks/15679"},
              {"label": "John Stuart Mill, On Liberty (1859)", "url": "https://www.gutenberg.org/ebooks/34901"}
            ],
            "quiz": [
              {
                "q": "What was Edmund Burke's central critique of the French Revolution in Reflections on the Revolution in France?",
                "options": [
                  "The French monarchs were too lenient on tax evasion.",
                  "Radical revolutionaries rashly destroyed complex, organic social institutions and inherited traditions in the name of abstract intellectual theories, inevitably paving the way for tyranny.",
                  "Private property should be abolished completely.",
                  "France should have adopted an American presidential constitution."
                ],
                "answer": 1,
                "why": "Burke argued that societies are delicate organic fabrics built across generations; sweeping away established customs in pursuit of abstract perfection results in social collapse and military rule."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "pol-political-economy",
    "title": "Political Economy: States, Markets & the Welfare State",
    "category": "Politics",
    "subcategory": "Political economy",
    "level": "Undergraduate",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "An investigation of the deep interplay between politics and economics. This course examines how state authority structures markets, the historical rise and retreat of the welfare state, Gøsta Esping-Andersen's 'Three Worlds of Welfare Capitalism', and the comparative institutional analysis of Liberal Market Economies (LMEs) vs Coordinated Market Economies (CMEs).",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Analyze the foundational debates between mercantilism, classical economics, and Keynesianism.",
      "Deconstruct Gøsta Esping-Andersen's typology: Liberal, Corporatist/Conservative, and Social Democratic welfare regimes.",
      "Compare Varieties of Capitalism: Hall and Soskice's LMEs vs CMEs.",
      "Evaluate the political determinants of income inequality and labor union density."
    ],
    "modules": [
      {
        "title": "Module 1: The Architecture of Welfare Capitalism",
        "lessons": [
          {
            "id": "pol-pe-l1",
            "title": "Esping-Andersen's Three Worlds of Welfare Capitalism",
            "body": """### De-Commodification and Social Stratification

In *The Three Worlds of Welfare Capitalism* (1990), Danish sociologist Gøsta Esping-Andersen fundamentally reshaped political economy by arguing that the welfare state cannot be measured simply by how much money a government spends. Instead, welfare states must be evaluated by **de-commodification**: the degree to which a citizen can freely maintain a socially acceptable livelihood independent of direct participation in the labor market.

#### The Three Welfare Regime Clusters
1. **The Liberal Welfare Regime (e.g., United States, United Kingdom, Australia):**
   - Dominance of the free market; commodification remains high.
   - Means-tested assistance targeting only the demonstrably destitute.
   - Low benefit levels accompanied by stigma; encouragement of private market solutions (private pensions, employer-sponsored health insurance).
2. **The Corporatist / Conservative Regime (e.g., Germany, France, Austria, Italy):**
   - State-organized social insurance programs tied directly to occupational employment history and status.
   - Benefits are earnings-related rather than universal; designed to maintain existing status differentials and social hierarchies.
   - Built on the principle of *subsidiarity*: the state intervenes only when the traditional male-breadwinner family unit fails.
3. **The Social Democratic Regime (e.g., Sweden, Norway, Denmark, Finland):**
   - Highest degree of de-commodification; universalist principles applied to all citizens as a basic social right.
   - Universal healthcare, state child-care, elder-care, and heavily subsidized higher education.
   - Pursues equality of the highest standard rather than minimal safety nets, actively pre-empting market inequalities.""",
            "readings": [
              {"label": "Gøsta Esping-Andersen, The Three Worlds of Welfare Capitalism (Princeton University Press, 1990)", "url": "https://press.princeton.edu/books/paperback/9780691028576/the-three-worlds-of-welfare-capitalism"},
              {"label": "Peter A. Hall & David Soskice, Varieties of Capitalism (Oxford University Press, 2001)", "url": "https://academic.oup.com/book/7403"}
            ],
            "quiz": [
              {
                "q": "What does Gøsta Esping-Andersen mean by 'de-commodification' in welfare state analysis?",
                "options": [
                  "The privatization of state-owned manufacturing companies.",
                  "The extent to which an individual can survive at a decent standard of living independently of their immediate participation in the labor market.",
                  "The elimination of paper currency in favor of barter trade.",
                  "The total deregulation of agricultural commodity futures."
                ],
                "answer": 1,
                "why": "De-commodification measures the degree of freedom citizens have from market dependence for their fundamental survival (e.g. through sickness benefits, parental leave, universal healthcare, and unemployment insurance)."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "pol-revolutions-movements",
    "title": "Revolutions, Social Movements & Collective Action",
    "category": "Politics",
    "subcategory": "Democracy and governance",
    "level": "Pre-university",
    "duration": "5 weeks (3 hours/week)",
    "instructor": faculty,
    "description": "An investigation into how mass political change occurs outside formal electoral channels. Students analyze structural theories of social revolution (Theda Skocpol), Mancur Olson's collective action dilemma, Erica Chenoweth's empirical study of nonviolent civil resistance, and the dynamics of digital social movements.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Evaluate Theda Skocpol's structural theory of state breakdown in France, Russia, and China.",
      "Analyze Mancur Olson's free-rider problem in collective mobilization.",
      "Compare the strategic efficacy of nonviolent civil resistance versus violent armed insurgency (Chenoweth & Stephan).",
      "Deconstruct contemporary decentralized protest movements (Arab Spring, Black Lives Matter, Euromaidan)."
    ],
    "modules": [
      {
        "title": "Module 1: The Dynamics of Revolution and Civil Resistance",
        "lessons": [
          {
            "id": "pol-rev-l1",
            "title": "Why Civil Resistance Works: The 3.5% Rule of Erica Chenoweth",
            "body": """### The Strategic Power of Nonviolent Action

For decades, political science assumed that toppling an entrenched authoritarian regime required armed force or external military invasion. In *Why Civil Resistance Works* (2011), political scientists Erica Chenoweth and Maria J. Stephan conducted a landmark empirical study of 323 major violent and nonviolent campaigns between 1900 and 2006.

#### The Core Empirical Findings
1. **Nonviolent Campaigns are Twice as Likely to Succeed:** Nonviolent campaigns succeeded in achieving their primary goals 53% of the time, compared to only 26% for violent armed insurgencies.
2. **The 3.5% Threshold:** Chenoweth discovered that no government in the historical dataset was able to withstand a nonviolent campaign that mobilized active, sustained participation from **3.5% of the national population** at its peak (e.g., the People Power Revolution in the Philippines in 1986).

#### Why Nonviolence Outperforms Violence
1. **Lower Barriers to Participation:** Armed rebellion requires physical youth, military training, weaponry, and willingness to kill. Nonviolent resistance (strikes, boycotts, mass marches, civil disobedience) allows participation across genders, ages, and socioeconomic backgrounds.
2. **Encouraging Security Force Defections:** When an insurgency uses violence, regime police and soldiers rally around the government out of self-defense. When protesters remain strictly nonviolent in the face of brutal state violence (*the backfire effect*), military commanders and ordinary conscripts increasingly refuse orders to open fire, fracturing the regime's coercive apparatus from within.""",
            "readings": [
              {"label": "Erica Chenoweth & Maria J. Stephan, Why Civil Resistance Works (Columbia University Press, 2011)", "url": "https://cup.columbia.edu/book/why-civil-resistance-works/9780231156820"},
              {"label": "Theda Skocpol, States and Social Revolutions (Cambridge University Press, 1979)", "url": "https://www.cambridge.org/core/books/states-and-social-revolutions/465B409E513DBCE547F5D4807BA76BD0"}
            ],
            "quiz": [
              {
                "q": "What primary strategic advantage explains why nonviolent civil resistance campaigns historically achieve higher success rates than violent armed insurgencies?",
                "options": [
                  "They have access to heavier military weapons.",
                  "They have far lower barriers to broad public participation, enabling mass mobilization that induces loyalty shifts and defections among state security forces.",
                  "They are always supported by foreign covert agencies.",
                  "They operate entirely in secret without public demonstrations."
                ],
                "answer": 1,
                "why": "Chenoweth & Stephan show that mass participation creates leverage across the entire economy and society, making security force defections far more likely when protesters remain disciplined and nonviolent."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "pol-propaganda-public-opinion",
    "title": "Propaganda, Information Warfare & Public Opinion",
    "category": "Politics",
    "subcategory": "Democracy and governance",
    "level": "Pre-university",
    "duration": "5 weeks (3 hours/week)",
    "instructor": faculty,
    "description": "A critical examination of how mass persuasion, psychological operations, and algorithmic information environments shape democratic politics. Students study Walter Lippmann's Public Opinion, Herman and Chomsky's Manufacturing Consent, and the contemporary crisis of generative AI disinformation, deepfakes, and computational propaganda.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Analyze Walter Lippmann's critique of the 'omnicompetent citizen' and the role of stereotypes in media.",
      "Deconstruct Herman & Chomsky's 'Propaganda Model' and its five editorial filters.",
      "Evaluate the mechanics of computational propaganda: Bot networks, algorithmic microtargeting, and echo chambers.",
      "Design regulatory and educational strategies for democratic resilience against synthetic disinformation."
    ],
    "modules": [
      {
        "title": "Module 1: Media, Power, and the Manufacturing of Consent",
        "lessons": [
          {
            "id": "pol-prop-l1",
            "title": "Lippmann, Chomsky, and the Construction of Political Reality",
            "body": """### Public Opinion in Mass Democracy

In *Public Opinion* (1922), veteran journalist Walter Lippmann diagnosed an uncomfortable reality for democratic theory. The classical ideal of the democratic citizen assumes an 'omnicompetent' individual who reads public bills, studies foreign trade balances, and casts an informed rational ballot.

In modern mass society, however, the real environment is too large, too complex, and too fleeting for direct human acquaintance. Instead, citizens construct a **pseudo-environment** inside their minds, mediated by simplified symbols, stereotypes, and media narratives:
> *"The world that we have to deal with politically is out of sight, out of mind, out of touch. It has to be explored, reported, and imagined."*

#### The Propaganda Model of Herman & Chomsky
In *Manufacturing Consent* (1988), Edward S. Herman and Noam Chomsky formulated the **Propaganda Model**, arguing that corporate mass media operates through structural institutional filters rather than overt state censorship:
1. **Size, Ownership, and Profit Orientation:** Major media outlets are large corporate enterprises tied to multinational parent corporations.
2. **Advertising as Primary Revenue:** Media firms do not sell news to consumers; they sell consumer attention to corporate advertisers.
3. **Sourcing of Mass Media News:** Overreliance on official government and corporate public relations briefings as cheap, authoritative sources.
4. **Flak:** Organized legal, political, and commercial retaliation against journalists who challenge elite consensus.
5. **Ideological Control:** Defining an external existential enemy to enforce patriotic conformity.""",
            "readings": [
              {"label": "Walter Lippmann, Public Opinion (1922)", "url": "https://www.gutenberg.org/ebooks/6456"},
              {"label": "Edward S. Herman & Noam Chomsky, Manufacturing Consent (Pantheon Books, 1988)", "url": "https://www.penguinrandomhouse.com/books/79659/manufacturing-consent-by-edward-s-herman-and-noam-chomsky/"}
            ],
            "quiz": [
              {
                "q": "According to Herman & Chomsky's Propaganda Model, what is the fundamental product sold by commercial mass media?",
                "options": [
                  "Objective investigative truth sold to citizens.",
                  "Audiences of consumers sold to commercial corporate advertisers.",
                  "Secret government documents sold to foreign intelligence agencies.",
                  "Printed books sold directly to public libraries."
                ],
                "answer": 1,
                "why": "Under commercial media economics, the primary business model is packaging reader and viewer demographics and selling their attention to advertisers."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "pol-feminist-gender-theory",
    "title": "Feminist Political Theory & the Politics of Gender",
    "category": "Politics",
    "subcategory": "Political philosophy",
    "level": "Pre-university",
    "duration": "5 weeks (3 hours/week)",
    "instructor": faculty,
    "description": "An exploration of feminist critiques of classical political theory and public policy. Students examine the historical waves of feminism, the deconstruction of the public/private divide ('the personal is political'), Kimberlé Crenshaw's theory of intersectionality, and the institutional design of gender parity in national parliaments.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Differentiate between liberal, radical, Marxist, and intersectional feminist theories.",
      "Deconstruct the classical public/private dichotomy in political thought (Susan Moller Okin).",
      "Apply Kimberlé Crenshaw's analytical framework of intersectionality to legal and political discrimination.",
      "Evaluate electoral gender quotas (reserved seats vs candidate list quotas) globally."
    ],
    "modules": [
      {
        "title": "Module 1: Challenging the Canonical Political Tradition",
        "lessons": [
          {
            "id": "pol-fem-l1",
            "title": "The Personal is Political: Dismantling the Public/Private Divide",
            "body": """### The Feminist Critique of Traditional Political Theory

From Aristotle and Locke to Rousseau and John Rawls, classical political philosophy consistently rested upon a profound foundational omission: the strict demarcation between the **Public Sphere** (the realm of citizenship, contracts, law, and politics) and the **Private Sphere** (the domestic home, family, reproduction, and care work).

Traditional theorists assumed that justice applies only in the public sphere, treating the family as a natural, pre-political hierarchy outside the jurisdiction of justice.

#### 1. Susan Moller Okin: Justice, Gender, and the Family (1989)
Okin challenged this foundational assumption, demonstrating that:
- The private family is not a natural haven free of power; it is an economic and social institution constructed and sustained by state laws (marriage statutes, divorce rules, tax codes, child custody).
- If the family is structured around unequal gendered division of unpaid labor, women cannot participate as equal citizens in the public sphere. Therefore: **A just society cannot exist without a just family**.

#### 2. Kimberlé Crenshaw: The Theory of Intersectionality (1989)
In a ground-breaking 1989 article, legal scholar Kimberlé Crenshaw introduced **intersectionality** (*DeGraffenreid v. General Motors*):
- Antidiscrimination law conceptualized discrimination as either solely racial or solely gender-based.
- Black women suffered unique, compound forms of marginalization that fell between the cracks of traditional civil rights frameworks.
- Intersectionality provides a crucial analytical lens to understand how race, gender, class, disability, and nationality interact to create interlocking systems of power and oppression.""",
            "readings": [
              {"label": "Susan Moller Okin, Justice, Gender, and the Family (Basic Books, 1989)", "url": "https://www.perseusbooks.com/titles/susan-moller-okin/justice-gender-and-the-family/9780465037032/"},
              {"label": "Kimberlé Crenshaw, Demarginalizing the Intersection of Race and Sex (1989)", "url": "https://chicagounbound.uchicago.edu/uclf/vol1989/iss1/8/"}
            ],
            "quiz": [
              {
                "q": "What was the central argument of Susan Moller Okin regarding the classical public/private divide in political theory?",
                "options": [
                  "The state should completely take over all childcare duties by decree.",
                  "The domestic family is an institutional creation shaped by state laws and gendered division of labor; true political justice cannot exist while treating the family as an exempt private sanctuary.",
                  "Women should solely participate in local municipal elections.",
                  "The family has no connection to political economy."
                ],
                "answer": 1,
                "why": "Okin demonstrated that inequalities inside the home (unpaid labor, domestic power) directly dictate and restrict women's public opportunities, meaning justice must apply inside the family as well as the state."
              }
            ]
          }
        ]
      }
    ]
  }
]

print("Politics courses compiled: 10/10")
