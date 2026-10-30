# Public Policy & Economics Courses (31-40) for The Paper Crane Academy
faculty = "Faculty of Public Policy and Economics, The Paper Crane Academy"

econ_courses = [
  {
    "id": "econ-micro-market-failures",
    "title": "Principles of Microeconomics: Price Theory, Externalities & Market Failures",
    "category": "Public Policy & Economics",
    "subcategory": "Microeconomics",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "A rigorous foundation in microeconomic theory and welfare economics. Explores consumer optimization, producer behavior, competitive equilibrium, elasticity, and the fundamental welfare theorems, before systematically investigating the causes and remedies for market failures: externalities, public goods, common-pool resources, and asymmetric information.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Model supply and demand equilibria, price elasticity, and deadweight loss from market distortions.",
      "Analyze the First and Second Fundamental Theorems of Welfare Economics.",
      "Evaluate corrective policy instruments for negative externalities: Pigouvian taxes versus Coaseian property rights bargaining.",
      "Distinguish public goods and common-pool resources using rivalry and excludability matrices."
    ],
    "modules": [
      {
        "title": "Module 1: Competitive Equilibrium, Welfare Theorems, and Externalities",
        "lessons": [
          {
            "id": "econ-mic-l1",
            "title": "Welfare Economics and Market Failures: Pigou vs Coase",
            "body": """### The Efficiency of Markets and When They Fail

In classical microeconomics, competitive markets allocate scarce resources efficiently. Under the **First Fundamental Theorem of Welfare Economics**, every competitive equilibrium is **Pareto optimal**: no individual can be made better off without making at least one individual worse off, provided there are complete markets, perfect information, and no externalities.

However, real-world markets frequently fail to achieve Pareto efficiency. The four primary sources of market failure are:
1. **Market Power (Monopoly/Oligopoly):** Firms set prices above marginal cost (`P > MC`), causing underproduction and deadweight loss.
2. **Externalities:** Uncompensated impacts of production or consumption on third parties.
3. **Public Goods & Common-Pool Resources:** Non-excludability leads to free-riding or tragedy of the commons.
4. **Information Asymmetries:** Adverse selection and moral hazard disrupt trade.

```
Goods Classification Matrix:
                   Excludable                    Non-Excludable
            +-----------------------------+-----------------------------+
Rivalrous   | Private Goods               | Common-Pool Resources       |
            | (Food, housing, clothing)   | (Fish stocks, clean water)  |
            +-----------------------------+-----------------------------+
Non-Rival   | Club Goods / Natural Monop. | Public Goods                |
            | (Cable television, patents) | (National defense, air)     |
            +-----------------------------+-----------------------------+
```

#### 1. Negative Externalities and Pigouvian Taxation (Arthur Pigou, 1920)
When a factory emits sulfur dioxide while manufacturing steel, it incurs a private marginal cost (*PMC*), but imposes an uncompensated environmental cost on society (*Marginal External Cost, MEC*).
- **The Market Outcome:** `Price = PMC`. Because `PMC < SMC` (Social Marginal Cost), the market produces **too much steel at too low a price**, generating deadweight welfare loss.
- **The Pigouvian Solution:** The government levies a corrective per-unit tax exactly equal to the marginal damage at the socially optimal output: `Tax = MEC`. This "internalizes the externality", aligning private incentives with social welfare.

#### 2. The Coase Theorem (Ronald Coase, *The Problem of Social Cost*, 1960)
Nobel laureate Ronald Coase demonstrated an alternative to state regulation:
- **The Theorem:** If property rights are clearly defined and enforceable, and **transaction costs are zero (or negligible)**, private parties will negotiate efficiently to resolve externalities without government intervention, regardless of how property rights are initially assigned.
- **The Caveat:** In the real world, transaction costs (lawyers, coordination among millions of affected citizens) are almost never zero, which explains why statutory regulation remains essential for widespread public harms like atmospheric pollution.""",
            "readings": [
              {"label": "Ronald H. Coase, The Problem of Social Cost (Journal of Law and Economics, 1960)", "url": "https://www.jstor.org/stable/724810"},
              {"label": "Arthur C. Pigou, The Economics of Welfare (Macmillan, 1920)", "url": "https://www.econlib.org/library/NPDBooks/Pigou/pgEW.html"},
              {"label": "Hal R. Varian, Intermediate Microeconomics: A Modern Approach (W.W. Norton, 9th ed.)", "url": "https://wwnorton.com/books/9780393123968"}
            ],
            "quiz": [
              {
                "q": "Under the Coase Theorem, what condition must be satisfied for private parties to negotiate an efficient solution to an externality without government taxation?",
                "options": [
                  "The government must set minimum price floors on all manufactured products.",
                  "Property rights must be clearly assigned, and transaction costs must be zero or negligible.",
                  "Both parties must belong to the same labor union.",
                  "The industry must be a state-owned natural monopoly."
                ],
                "answer": 1,
                "why": "Coase showed that with zero transaction costs and well-defined property rights, parties will bargain to the Pareto-efficient allocation regardless of initial entitlement distribution."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "econ-macro-central-banking",
    "title": "Macroeconomic Policy, Inflation & Central Banking: Monetary Transmission & Multipliers",
    "category": "Public Policy & Economics",
    "subcategory": "Macroeconomics",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "An advanced exploration of macroeconomic stabilization, monetary policy transmission channels, and fiscal policy. Covers central bank balance sheet mechanics, quantitative easing, interest rate policy (the Taylor Rule), the Phillips Curve trade-off, inflation targeting, and sovereign debt sustainability.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Analyze the monetary transmission mechanism: how changes in policy rates affect commercial credit, exchange rates, and aggregate demand.",
      "Evaluate the Taylor Rule and inflation-targeting frameworks used by modern independent central banks.",
      "Understand the mechanics of unconventional monetary policy: Quantitative Easing (QE) and forward guidance.",
      "Calculate fiscal multipliers and evaluate Keynesian stimulus versus debt sustainability constraints."
    ],
    "modules": [
      {
        "title": "Module 1: Central Banking, Monetary Transmission, and the Inflation Fight",
        "lessons": [
          {
            "id": "econ-mac-l1",
            "title": "Central Bank Operations, Monetary Policy Transmission, and the Taylor Rule",
            "body": """### The Architecture of Modern Macroeconomic Stabilization

Modern central banks—such as the Federal Reserve, the European Central Bank, and the Bank of England—serve as the monetary authorities of their economies. They operate primarily through open market operations to steer short-term benchmark interest rates, aiming to maintain price stability and full employment.

```
Monetary Transmission Mechanism:
[Central Bank Policy Rate] 
       ↓ (Changes interbank overnight rates)
[Commercial Bank Lending Rates / Mortgage Rates / Bond Yields]
       ↓ (Influences corporate borrowing & household spending)
[Aggregate Demand (Consumption + Investment)]
       ↓
[Output Gap & Inflation Pressure]
```

#### 1. Central Bank Tools: Conventional vs Unconventional
- **Conventional Tools:**
  - *Short-Term Policy Rate (e.g., Federal Funds Rate):* The rate commercial banks pay to borrow reserves overnight.
  - *Reserve Requirements & Standing Facilities:* Corridor systems determining floor and ceiling rates.
- **Unconventional Tools (Post-2008 & Post-2020):**
  - *The Zero Lower Bound (ZLB):* When the policy rate hits ~0%, central banks cannot stimulate further through conventional rate cuts alone.
  - *Quantitative Easing (QE):* The large-scale purchase of long-dated government bonds and mortgage-backed securities using newly created central bank reserves. QE compresses long-term yields, lowers mortgage costs, and boosts asset valuations.
  - *Forward Guidance:* Explicit communication regarding the future path of interest rates to anchor market expectations.

#### 2. The Taylor Rule (John B. Taylor, 1993)
A foundational monetary policy rule that models how central banks should adjust nominal interest rates in response to changes in inflation and economic output:

`i = r* + π + 0.5(π - π*) + 0.5(y - y*)`

Where:
- `i` = Target nominal policy interest rate.
- `r*` = Neutral real interest rate.
- `π` = Current inflation rate; `π*` = Central bank's target inflation rate (typically 2%).
- `y - y*` = Output gap (percent deviation of actual GDP from potential GDP).

**The Taylor Principle:** When inflation rises by 1%, the central bank must raise the nominal interest rate by *more than 1%* (a coefficient > 1.0) so that the *real interest rate* (`r = i - π`) rises, curbing borrowing and aggregate demand to cool inflation.""",
            "readings": [
              {"label": "John B. Taylor, Discretion versus Policy Rules in Practice (Carnegie-Rochester Conference Series, 1993)", "url": "https://www.sciencedirect.com/science/article/abs/pii/016722319390009L"},
              {"label": "Ben S. Bernanke, The Courage to Act: A Memoir of a Crisis and Its Aftermath (W.W. Norton, 2015)", "url": "https://wwnorton.com/books/9780393247213"},
              {"label": "Mervyn King, The End of Alchemy: Money, Banking, and the Future of the Global Economy (2016)", "url": "https://wwnorton.com/books/9780393247022"}
            ],
            "quiz": [
              {
                "q": "What is the critical insight of the 'Taylor Principle' in central banking monetary policy?",
                "options": [
                  "The central bank should always keep nominal interest rates at exactly zero percent.",
                  "When inflation rises by 1 percentage point, the central bank must raise the nominal policy rate by more than 1 percentage point so that the real interest rate increases, effectively restraining aggregate demand.",
                  "Central banks should purchase corporate stocks whenever foreign currencies appreciate.",
                  "Commercial banks must hold 100% of deposits in physical gold."
                ],
                "answer": 1,
                "why": "If the central bank raises nominal rates by less than the increase in inflation, the real interest rate actually falls, perversely stimulating borrowing and accelerating inflation."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "econ-policy-analysis",
    "title": "The Public Policy Process: Problem Definition, Cost-Benefit Analysis & Implementation",
    "category": "Public Policy & Economics",
    "subcategory": "Public policy analysis",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "A comprehensive practical methodology for public policy design and evaluation. Teaches Bardach's Eightfold Path, quantitative cost-benefit analysis (discount rates, net present value, value of a statistical life), regulatory impact assessments, policy feedback loops, and implementation hurdles.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Master Eugene Bardach's Eightfold Path for practical policy formulation.",
      "Execute rigorous Cost-Benefit Analysis (CBA) including discounting, Net Present Value (NPV), and sensitivity analysis.",
      "Understand the ethical and statistical methodologies for estimating the Value of a Statistical Life (VSL).",
      "Analyze street-level bureaucracy and the common causes of policy implementation failure."
    ],
    "modules": [
      {
        "title": "Module 1: The Policy Cycle and Quantitative Cost-Benefit Analysis",
        "lessons": [
          {
            "id": "econ-pol-l1",
            "title": "Bardach's Eightfold Path and the Mechanics of Cost-Benefit Analysis",
            "body": """### The Policy Analyst's Craft

Public policy analysis is the systematic evaluation of technical, political, and economic options to address pressing societal problems. 

#### 1. Eugene Bardach's Eightfold Path
Developed at UC Berkeley's Goldman School of Public Policy, this framework provides the industry standard workflow for policy analysts:
1. **Define the Problem:** Formulate the problem in terms of deficits and excesses (e.g., *"Too many children under five lack immunization in rural district X"* rather than a preconceived solution).
2. **Assemble Evidence:** Collect quantitative data, statutes, and academic evaluations.
3. **Construct the Alternatives:** Formulate 3–4 viable policy alternatives (including the baseline *"do nothing"*).
4. **Select the Criteria:** Choose evaluative metrics (efficiency, equity, political feasibility, administrative simplicity).
5. **Project the Outcomes:** Forecast the impacts of each alternative over a 5–20 year horizon.
6. **Confront the Trade-Offs:** Clarify what society gains and forfeits when choosing Alternative A over B.
7. **Stop, Focus, Narrow, Deepen, Decide:** Make an explicit recommendation.
8. **Tell Your Story:** Deliver a concise executive memorandum for decision-makers.

#### 2. Cost-Benefit Analysis (CBA) and Discounting
Government agencies use CBA to determine whether the aggregate social benefits of a regulation exceed its costs:
- **Net Present Value (NPV):** Future costs and benefits must be converted into present-day dollars using a social discount rate (`r`):
  `NPV = ∑ [ (Benefit_t - Cost_t) / (1 + r)^t ]`
  - A higher discount rate undervalues long-term future benefits (e.g., climate change mitigation 50 years from now).
- **The Value of a Statistical Life (VSL):** In transportation safety, environmental protection, and healthcare, policies reduce mortality risk. VSL is not the price of a human life; it is society's willingness to pay for small risk reductions aggregated across a population.
  - *Example:* If individuals are willing to pay $100 on average to reduce their annual risk of dying in a transit accident by 1 in 100,000, then `VSL = $100 / (1/100,000) = $10,000,000`.""",
            "readings": [
              {"label": "Eugene Bardach and Eric M. Patashnik, A Practical Guide for Policy Analysis: The Eightfold Path (CQ Press, 6th ed. 2019)", "url": "https://us.sagepub.com/en-us/nam/a-practical-guide-for-policy-analysis/book266014"},
              {"label": "Anthony E. Boardman et al., Cost-Benefit Analysis: Concepts and Practice (Cambridge, 5th ed. 2018)", "url": "https://www.cambridge.org/core/books/costbenefit-analysis/9F5594DA14C0334CA0953EE3C0A983E3"},
              {"label": "U.S. Office of Management and Budget (OMB), Circular A-4: Regulatory Analysis", "url": "https://www.whitehouse.gov/omb/information-regulatory-affairs/circulars/"}
            ],
            "quiz": [
              {
                "q": "In regulatory Cost-Benefit Analysis, what happens to the projected present value of long-term environmental benefits 50 years into the future when an agency uses a very high discount rate?",
                "options": [
                  "The present value of those future benefits dramatically shrinks, making long-term investments appear economically unviable.",
                  "The present value of future benefits approaches infinity.",
                  "The discount rate has zero mathematical effect on net present value.",
                  "It forces private firms to double their dividend payments."
                ],
                "answer": 0,
                "why": "Because future values are divided by (1 + r)^t, a high discount rate 'r' exponentially reduces the present value of benefits realized in distant future decades."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "econ-inequality-capital",
    "title": "Wealth Distribution, Inequality & Capital in the 21st Century: The Piketty Thesis",
    "category": "Public Policy & Economics",
    "subcategory": "Economic inequality",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "An empirical and theoretical examination of income and wealth distribution in modern economies. Dissects Thomas Piketty's r > g thesis, the Kuznets curve, the labor share of national income, super-managers and executive compensation, intergenerational wealth transfers, and progressive tax policy.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Critically evaluate Thomas Piketty's fundamental inequality law: r > g (return on capital exceeds economic growth).",
      "Analyze the historical evolution of the Gini coefficient, Palma ratio, and wealth deciles over two centuries.",
      "Examine the drivers of wage polarization: skill-biased technological change vs institutional erosion (union density, minimum wage).",
      "Debate wealth tax proposals, inheritance taxation, and global corporate minimum tax agreements."
    ],
    "modules": [
      {
        "title": "Module 1: The Dynamics of Capital Accumulation and Wealth Concentration",
        "lessons": [
          {
            "id": "econ-in-l1",
            "title": "Piketty's r > g and the Structural Dynamics of Wealth Concentration",
            "body": """### Capital, Inequality, and Historical Dynamics

In 2013, French economist Thomas Piketty published *Capital in the Twenty-First Century*, synthesizing three centuries of tax records across twenty countries. His work transformed economic discourse by refuting the mid-20th century **Kuznets Curve hypothesis** (which claimed that industrial development naturally leads first to rising inequality, and then automatically to egalitarian compression).

```
The Kuznets Curve (Disproved by late 20th-century data):
Inequality
    ^         /---\\
    |        /     \\
    |       /       \\   ← (Kuznets hypothesized inequality falls automatically)
    |      /         \\
    +------------------------> Economic Development
```

Instead, Piketty demonstrated that the egalitarian compression observed between 1914 and 1970 was an anomalous historical accident caused by the physical destruction of capital in World Wars I and II, bankruptcies during the Great Depression, and confiscatory wartime taxation—not natural market equilibrium.

#### 1. The Fundamental Inequality Law: `r > g`
Piketty posits that when the **rate of return on capital (`r`)** significantly exceeds the **rate of economic growth (`g`)**, wealth concentration intensifies automatically:
- **`r` (Return on Capital):** The average annual yield on real estate, stocks, corporate bonds, dividends, and interest (historically around 4%–5%).
- **`g` (Economic Growth):** The annual rate of output growth from population increase and technological productivity (typically 1%–2% in mature economies).
- **The Implication:** Inherited wealth accumulates much faster than output and wages. Fortunes grow exponentially through compounding returns, causing society to revert to a **patrimonial capitalism** dominated by inherited dynasties rather than meritocratic talent.

#### 2. Measuring Economic Inequality
- **The Gini Coefficient:** A metric ranging from 0 (perfect equality: everyone earns the exact same) to 1 (perfect inequality: one person owns all national wealth).
- **The Palma Ratio:** The ratio of the richest 10% of the population's share of gross national income divided by the poorest 40%'s share.
- **Top 1% Wealth Share:** Reflects extreme concentration at the apex of the pyramid.""",
            "readings": [
              {"label": "Thomas Piketty, Capital in the Twenty-First Century (Harvard University Press, 2014)", "url": "https://www.hup.harvard.edu/books/9780674979857"},
              {"label": "Emmanuel Saez and Gabriel Zucman, The Triumph of Injustice: How the Rich Dodge Taxes and How to Make Them Pay (W.W. Norton, 2019)", "url": "https://wwnorton.com/books/9781324004042"},
              {"label": "World Inequality Report 2022 (World Inequality Lab)", "url": "https://wir2022.wid.world/"}
            ],
            "quiz": [
              {
                "q": "What is the economic consequence when the rate of return on capital (r) consistently exceeds the rate of economic growth (g), according to Thomas Piketty?",
                "options": [
                  "Wealth inequality naturally and automatically vanishes without any policy changes.",
                  "Inherited wealth grows significantly faster than wages and economic output, leading to increasing concentration of wealth and the rise of patrimonial capitalism.",
                  "All corporations immediately declare bankruptcy.",
                  "Consumer inflation declines to negative fifty percent."
                ],
                "answer": 1,
                "why": "When r > g, inherited wealth compounds faster than the economy creates new output, concentrating national wealth in the hands of capital holders at the expense of wage earners."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "econ-financial-crises",
    "title": "Financial Crises, Systemic Risk & Banking Regulation: From 1929 to Basel III",
    "category": "Public Policy & Economics",
    "subcategory": "Financial regulation",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "An in-depth inquiry into banking architecture, systemic financial crises, and macroprudential regulation. Covers the anatomy of bank runs, maturity transformation, the shadow banking system, securitization, Minsky's Financial Instability Hypothesis, Dodd-Frank, and the Basel capital accords.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Model maturity transformation and bank runs using the Diamond-Dybvig framework.",
      "Analyze Hyman Minsky's Financial Instability Hypothesis (Hedge, Speculative, and Ponzi finance).",
      "Deconstruct the structural causes of the 2008 Global Financial Crisis: subprime securitization, CDOs, and CDS swaps.",
      "Evaluate regulatory solutions: capital adequacy ratios (Basel III), stress tests, and resolution mechanisms ('living wills')."
    ],
    "modules": [
      {
        "title": "Module 1: The Anatomy of Bank Runs and Systemic Fragility",
        "lessons": [
          {
            "id": "econ-fc-l1",
            "title": "The Diamond-Dybvig Model, Minsky Moments, and Basel Regulations",
            "body": """### The Inherent Fragility of Banking

Commercial banks perform a vital economic function known as **maturity transformation**: they accept short-term, liquid deposits (which depositors can withdraw on demand) and transform them into long-term, illiquid loans (30-year mortgages, corporate project financing).

```
Maturity Transformation:
[Liquid, Short-Term Liabilities] ──→ [Bank Balance Sheet] ──→ [Illiquid, Long-Term Assets]
(Demand deposits, wholesale repo)                                 (Mortgages, commercial loans)
```

#### 1. The Diamond-Dybvig Model of Bank Runs (1983)
Nobel laureates Douglas Diamond and Philip Dybvig demonstrated that maturity transformation exposes banks to self-fulfilling panic:
- Because the bank's assets are illiquid and cannot be liquidated instantly at full value, if all depositors believe *other* depositors are going to withdraw their money, it is individually rational for everyone to run to the bank first.
- **Institutional Solutions:**
  - *Deposit Insurance (FDIC):* Guarantees retail deposits up to a statutory limit, removing the panic incentive.
  - *Lender of Last Resort (Bagehot's Dictum):* The central bank lends freely to solvent institutions against good collateral at a penalty rate during liquidity panics.

#### 2. Minsky's Financial Instability Hypothesis
Economist Hyman Minsky demonstrated that *"stability breeds instability"*:
- Long periods of economic tranquility lead banks, investors, and borrowers to underestimate risk and take on excessive debt leverage.
- Debt financing progresses through three stages:
  1. **Hedge Finance:** Cash flows cover both principal and interest payments.
  2. **Speculative Finance:** Cash flows cover only interest; principal must be rolled over.
  3. **Ponzi Finance:** Cash flows cannot even cover interest; the debtor relies on endless asset price inflation to refinance.
- **The Minsky Moment:** Asset prices stop rising, Ponzi borrowers default, leverage unwinds catastrophically, and liquidity freezes across the entire interbank system.

#### 3. Post-Crisis Architecture: Basel III Capital Requirements
To prevent systemic collapse without relying on taxpayer bailouts:
- **Common Equity Tier 1 (CET1):** Banks must maintain high-quality equity capital equal to at least 4.5%–7% of risk-weighted assets.
- **Liquidity Coverage Ratio (LCR):** Banks must hold enough High-Quality Liquid Assets (cash, sovereign debt) to withstand a 30-day acute liquidity stress scenario.
- **Capital Conservation & Counter-Cyclical Buffers:** Requiring banks to build extra equity cushions during economic booms that can be drawn down during recessions.""",
            "readings": [
              {"label": "Douglas W. Diamond and Philip H. Dybvig, Bank Runs, Deposit Insurance, and Liquidity (JPE, 1983)", "url": "https://www.jstor.org/stable/1837095"},
              {"label": "Hyman P. Minsky, Stabilizing an Unstable Economy (Yale University Press, 1986)", "url": "https://www.worldcat.org/title/stabilizing-an-unstable-economy/oclc/12808796"},
              {"label": "Bank for International Settlements (BIS), Basel III: International Regulatory Framework for Banks", "url": "https://www.bis.org/bcbs/basel3.htm"}
            ],
            "quiz": [
              {
                "q": "What fundamental structural vulnerability does the Diamond-Dybvig model identify in commercial banking?",
                "options": [
                  "Banks hold too much physical currency in their safes.",
                  "Maturity transformation: banks fund long-term illiquid loans with short-term demand deposits, creating the risk of self-fulfilling panic runs.",
                  "Banks are legally prohibited from lending money to private corporations.",
                  "Central banks only operate during daylight hours."
                ],
                "answer": 1,
                "why": "Because banks cannot immediately liquidate long-term loans without fire-sale losses, a sudden surge in demand for liquidity can trigger catastrophic insolvency in otherwise solvent banks."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "econ-behavioral-economics",
    "title": "Behavioral Economics, Choice Architecture & Nudge Theory: Heuristics & Policy",
    "category": "Public Policy & Economics",
    "subcategory": "Behavioral science",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "An empirical exploration of how human psychology shapes economic decision-making. Contrasts traditional rational-choice *Homo economicus* with cognitive realities: prospect theory, loss aversion, hyperbolic discounting, and heuristics. Explores behavioral policy interventions, default rules, and nudge units.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Contrast the neoclassical rational-actor model with Daniel Kahneman and Amos Tversky's Prospect Theory.",
      "Analyze cognitive biases: loss aversion, framing effects, availability heuristic, and present bias.",
      "Master the principles of Choice Architecture and Libertarian Paternalism (Thaler & Sunstein).",
      "Evaluate the ethics and efficacy of government 'Nudge Units' in organ donation, retirement savings, and tax compliance."
    ],
    "modules": [
      {
        "title": "Module 1: Cognitive Biases, Prospect Theory, and Choice Architecture",
        "lessons": [
          {
            "id": "econ-be-l1",
            "title": "Prospect Theory, Loss Aversion, and Choice Architecture",
            "body": """### Beyond Homo Economicus

Neoclassical economic models assume *Homo economicus*: perfectly rational agents with limitless computational capacity, fully ordered preferences, and absolute self-control. Behavioral economics, pioneered by psychologists Daniel Kahneman and Amos Tversky and economist Richard Thaler, replaces this fiction with empirical observations of actual human cognition.

#### 1. Kahneman & Tversky's Prospect Theory (1979)
Prospect theory models how individuals actually evaluate risk and uncertainty:
- **Reference Dependence:** People do not evaluate outcomes based on absolute wealth, but as **gains or losses relative to an arbitrary psychological reference point**.
- **Loss Aversion:** The psychological pain of losing $100 is roughly **twice as intense** as the pleasure of gaining $100.
- **Diminishing Sensitivity & Probability Weighting:** People are risk-averse when facing potential gains (preferring a sure $500 over a 50% chance of $1,000), but become risk-seeking when facing potential losses (preferring a 50% gamble of losing $1,000 over a sure loss of $500).

```
Prospect Theory Value Function:
      Value (Pleasure)
             ^
             |          /-- (Diminishing sensitivity for gains)
             |        /
             |      /
- Losses <---+---> Gains
           / |
          /  | (Loss aversion: steeper curve for losses)
         /   |
        v
    Value (Pain)
```

#### 2. Choice Architecture and Nudge Theory (Thaler & Sunstein, 2008)
Because human decisions are sensitive to context, how choices are presented—**Choice Architecture**—fundamentally dictates behavior:
- **Libertarian Paternalism:** Interventions should steer choices in directions that make choosers better off (paternalistic), while preserving freedom of choice and allowing individuals to opt out easily at zero cost (libertarian).
- **The Power of Defaults:** When automatic enrollment in retirement 401(k) plans replaced opt-in enrollment (employees are enrolled by default and must click to opt out), participation jumped from 37% to 86%. Similar default rules transform organ donor registration rates across European nations.""",
            "readings": [
              {"label": "Daniel Kahneman, Thinking, Fast and Slow (Farrar, Straus and Giroux, 2011)", "url": "https://us.macmillan.com/books/9780374533557/thinkingfastandslow"},
              {"label": "Richard H. Thaler and Cass R. Sunstein, Nudge: The Final Edition (Penguin, 2021)", "url": "https://www.penguinrandomhouse.com/books/673801/nudge-by-richard-h-thaler-and-cass-r-sunstein/"},
              {"label": "Amos Tversky and Daniel Kahneman, Prospect Theory: An Analysis of Decision under Risk (Econometrica, 1979)", "url": "https://www.jstor.org/stable/1914185"}
            ],
            "quiz": [
              {
                "q": "What is the defining psychological finding of 'loss aversion' in Kahneman and Tversky's Prospect Theory?",
                "options": [
                  "People are completely indifferent between financial profits and losses.",
                  "The psychological pain of suffering a monetary loss is roughly twice as intense as the pleasure experienced from an equivalent monetary gain.",
                  "Individuals only make financial decisions based on astrological calculations.",
                  "People will always choose the most expensive health insurance plan."
                ],
                "answer": 1,
                "why": "Empirical experiments demonstrate that losses loom larger than gains: losing $100 causes approximately twice the psychological displeasure as winning $100 causes pleasure."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "econ-antitrust-tech",
    "title": "Antitrust Policy & the Regulation of Big Tech: Networks, Monopsony & Competition",
    "category": "Public Policy & Economics",
    "subcategory": "Industrial organization",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "A critical examination of competition policy in digital platform markets. Examines the history of antitrust from the Sherman Act (1890) to the Chicago School consumer welfare standard, network effects, two-sided platform markets, data lock-in, predatory acquisitions, and the New Brandeisian regulatory revival.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Trace the statutory foundation of competition law: Sherman Act Sections 1 and 2, and Clayton Act Section 7.",
      "Critique Robert Bork's Chicago School 'Consumer Welfare Standard' in zero-price digital platform markets.",
      "Analyze Lina Khan's 'Amazon's Antitrust Paradox' and the New Brandeis school of competition policy.",
      "Evaluate regulatory remedies: structural breakups, data portability, interoperability mandates, and the EU Digital Markets Act (DMA)."
    ],
    "modules": [
      {
        "title": "Module 1: The Evolution of Antitrust: From Standard Oil to Digital Platforms",
        "lessons": [
          {
            "id": "econ-at-l1",
            "title": "The Consumer Welfare Standard vs The New Brandeis Movement",
            "body": """### Competition Policy in the Age of Digital Monopolies

Antitrust law protects competitive market structures from monopolistic abuses. In the United States, modern antitrust rests on the **Sherman Antitrust Act of 1890** (**Section 1** banning conspiracies in restraint of trade; **Section 2** prohibiting monopolization and attempts to monopolize).

#### 1. The Rise and Limits of the Chicago School (Robert Bork, 1978)
For four decades, American antitrust was dominated by Robert Bork's **Consumer Welfare Standard**:
- An arrangement violates antitrust laws **only if it harms consumers through higher prices, reduced output, or diminished quality**.
- If a merger lowers production costs or delivers lower prices to shoppers, it is presumed pro-competitive, regardless of how many small competitors are crushed.

#### 2. Lina Khan and 'Amazon's Antitrust Paradox' (2017)
In a revolutionary *Yale Law Journal* article, legal scholar Lina Khan (later Chair of the Federal Trade Commission) exposed the blind spots of the Consumer Welfare Standard in modern digital platform markets:
- **The Zero-Price Conundrum:** Many tech giants provide products for free to consumers (search, social media, navigation) or subsidize prices below cost for years to capture market share. Under Bork's price-centric standard, a firm offering free services appears incapable of causing antitrust harm.
- **Structural Hazards of Two-Sided Platforms:**
  - *Network Effects:* As more users join a platform, the platform becomes exponentially more valuable, creating a "winner-take-all" tipping dynamic.
  - *Dual Role (Platform Host + Merchant Competitor):* Platforms control the marketplace infrastructure while simultaneously competing against third-party merchants whose data they observe and exploit.
  - *Killer Acquisitions:* Incumbents acquire nascent startup rivals before they can evolve into competitive threats (e.g., acquisitions of Instagram and WhatsApp).

```
Platform Dual Role Conflict:
[ Digital Platform Marketplace ] ── Controls algorithms, ranking & user data
        ├── Hosts 10,000 independent merchant vendors
        └── Sells platform's own copycat private-label brands (Promoted to top)
```

#### 3. New Regulatory Tools: Interoperability and the EU DMA
In response, policymakers designed proactive *ex-ante* regulations:
- **The EU Digital Markets Act (DMA):** Designates systemic platforms as "gatekeepers", prohibiting self-preferencing and mandating interoperability for core messaging services.""",
            "readings": [
              {"label": "Lina M. Khan, Amazon's Antitrust Paradox (Yale Law Journal, 2017)", "url": "https://www.yalelawjournal.org/article/amazons-antitrust-paradox"},
              {"label": "Robert H. Bork, The Antitrust Paradox: A Policy at War with Itself (Basic Books, 1978)", "url": "https://www.worldcat.org/title/antitrust-paradox/oclc/3843516"},
              {"label": "European Commission, The Digital Markets Act: Ensuring Fair and Open Digital Markets", "url": "https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/europe-fit-digital-age/digital-markets-act-ensuring-fair-and-open-digital-markets_en"}
            ],
            "quiz": [
              {
                "q": "Why does Lina Khan argue that Robert Bork's traditional 'Consumer Welfare Standard' fails to address antitrust harms in digital tech platforms like Amazon or Google?",
                "options": [
                  "Because tech companies only operate in Antarctica.",
                  "Because the standard focuses narrowly on short-term consumer price increases, rendering it blind to predatory pricing, market lock-in, and anti-competitive platform dominance where consumer services are provided at zero monetary price.",
                  "Because antitrust statutes were legally repealed in 1980.",
                  "Because online shopping has no economic value."
                ],
                "answer": 1,
                "why": "When platforms offer free or heavily subsidized services, a standard that only looks for consumer price spikes fails to detect systemic anti-competitive conduct like predatory exclusion, lock-in, and self-preferencing."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "econ-ubi-automation",
    "title": "Universal Basic Income, Automation & the Future of Social Welfare",
    "category": "Public Policy & Economics",
    "subcategory": "Social policy",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "A rigorous policy analysis of labor market automation, artificial intelligence, and welfare state redesign. Explores Universal Basic Income (UBI), negative income taxes, job guarantees, labor share decline, and the fiscal mechanics of funding unconditional social transfers.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Analyze the economics of Universal Basic Income (UBI): universality, unconditionality, and cash delivery.",
      "Compare Milton Friedman's Negative Income Tax (NIT) with universal progressive basic income models.",
      "Evaluate empirical evidence from UBI pilot trials (Finland, Stockton California, Kenya GiveDirectly).",
      "Model fiscal financing mechanisms: sovereign wealth funds, carbon dividends, and automation/data taxation."
    ],
    "modules": [
      {
        "title": "Module 1: Automation, Labor Displacement, and the Economics of Cash Transfers",
        "lessons": [
          {
            "id": "econ-ubi-l1",
            "title": "The Mechanics of Universal Basic Income and the Future of Work",
            "body": """### Redefining Social Security for the 21st Century

The 20th-century welfare state was designed around the premise of formal, stable, full-time wage labor, where social protections (pensions, disability insurance, unemployment benefits) were tied to employment. The rise of artificial intelligence, robotic automation, and the platform "gig" economy has challenged this model, sparking intense global policy debate over **Universal Basic Income (UBI)**.

#### 1. Defining Universal Basic Income
A true Universal Basic Income is defined by five non-negotiable criteria:
1. **Periodic:** Paid at regular intervals (e.g., monthly), not as a one-time grant.
2. **Cash Payment:** Delivered in liquid currency, allowing recipients full consumer sovereignty (unlike food stamps or housing vouchers).
3. **Individual:** Paid to each individual adult, rather than calculated per household.
4. **Universal:** Paid to all citizens without means-testing or income eligibility cutoffs.
5. **Unconditional:** Paid without work requirements, job search verification, or moral conditionalities.

```
Targeted Means-Tested Welfare vs Universal Basic Income:
[Traditional Welfare] ── Strict means tests ──→ Creates "Poverty Trap"
                                                  (Lose benefits if you take a low-wage job)

[Universal Basic Income] ── Given to all unconditionally ──→ Always better off working
                                                             (Earned wages add to UBI floor)
```

#### 2. The 'Poverty Trap' and Effective Marginal Tax Rates
Traditional means-tested welfare suffers from a severe structural flaw: the **welfare cliff**.
- When a low-income recipient finds a job earning $1,000/month, the government terminates their subsidized housing, food stamps, and Medicaid.
- The effective marginal tax rate can exceed **80%–100%**: every dollar earned from honest labor is canceled by lost welfare benefits.
- UBI eliminates this trap: because the baseline check is never revoked when you take a job, every dollar of work directly increases net household income.

#### 3. Fiscal Realities and Financing Models
The central challenge of UBI is gross budgetary cost. A payment of $1,000/month to 250 million adult citizens in the US requires $3 trillion annually (~12% of GDP). Proposed financing mechanisms include:
- **Carbon Dividends:** Levying a tax on carbon emissions and redistributing 100% of the revenue equally to every citizen.
- **Sovereign Wealth Funds (The Alaska Permanent Fund model):** Capitalizing state resource windfalls or public equity stakes into an investment fund that yields annual citizen dividends.
- **Land Value Taxes & Value Added Taxes (VAT).**""",
            "readings": [
              {"label": "Philippe Van Parijs and Yannick Vanderborght, Basic Income: A Radical Proposal for a Free Society (Harvard, 2017)", "url": "https://www.hup.harvard.edu/books/9780674052284"},
              {"label": "Milton Friedman, Capitalism and Freedom (Chapter 12 on Negative Income Tax, 1962)", "url": "https://press.uchicago.edu/ucp/books/book/chicago/C/bo3643764.html"},
              {"label": "GiveDirectly, The Universal Basic Income Experiment in Kenya (Research Overview)", "url": "https://www.givedirectly.org/research-on-cash-transfers/"}
            ],
            "quiz": [
              {
                "q": "How does an unconditional Universal Basic Income (UBI) structurally eliminate the 'poverty trap' inherent in traditional means-tested welfare systems?",
                "options": [
                  "By making it illegal for low-income citizens to seek employment.",
                  "Because UBI is paid unconditionally to all citizens and is never revoked when an individual gets a job, every dollar of wage income directly increases their net total income.",
                  "By converting all cash payments into non-transferable food coupons.",
                  "By privatizing all public transportation systems."
                ],
                "answer": 1,
                "why": "Means-tested welfare claws back benefits as soon as a recipient earns wages, creating an effective marginal tax rate near 100%. UBI provides an unbreakable floor that is never clawed back."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "econ-environmental-economics",
    "title": "Environmental Economics & the Global Energy Transition: Carbon Pricing & Markets",
    "category": "Public Policy & Economics",
    "subcategory": "Environmental policy",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "An analytical study of climate economics, market-based environmental instruments, and energy transitions. Explores the social cost of carbon, cap-and-trade systems (ETS) versus carbon taxation, border carbon adjustments, green industrial policy, and William Nordhaus's DICE integrated assessment model.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Calculate the Social Cost of Carbon (SCC) and evaluate the role of discount rates in climate models.",
      "Compare Cap-and-Trade emissions trading systems with uniform Carbon Taxes using Weitzman's 'Prices vs Quantities' framework.",
      "Analyze Carbon Border Adjustment Mechanisms (CBAM) to prevent carbon leakage in international trade.",
      "Evaluate modern clean technology subsidies and green industrial policies."
    ],
    "modules": [
      {
        "title": "Module 1: Carbon Pricing Mechanics: Carbon Taxes vs Cap-and-Trade",
        "lessons": [
          {
            "id": "econ-env-l1",
            "title": "Pricing Carbon: Weitzman's Prices vs Quantities and Carbon Leakage",
            "body": """### The Economics of Climate Change

Climate change represents what economist Nicholas Stern famously termed *"the greatest market failure the world has ever seen"*. Greenhouse gas emissions are an unpriced global externality: emitters enjoy the full private benefit of cheap fossil fuel energy while dispersing the catastrophic planetary costs across the entire global population and future generations.

#### 1. The Two Market-Based Instruments
Economists advocate putting a transparent price on carbon to let market incentives drive decarbonization:
- **Carbon Tax (Price Instrument):**
  - The government fixes the price per metric ton of CO2 emissions (e.g., $50/ton).
  - The market determines the resulting quantity of emission reductions.
  - *Advantage:* Price certainty for businesses planning clean energy capital investments.
- **Cap-and-Trade / Emissions Trading System (Quantity Instrument):**
  - The government caps the total allowable volume of emissions (e.g., 500 million tons/year) and issues a matching number of tradable allowances.
  - Emitters must surrender one allowance per ton emitted. Those that can abate emissions cheaply sell surplus allowances to those facing high abatement costs.
  - *Advantage:* Environmental certainty that aggregate emissions will not exceed the physical cap (e.g., EU Emissions Trading System, EU ETS).

```
Carbon Policy Comparison:
Carbon Tax:       Government sets [PRICE]    ──→ Market chooses [QUANTITY]
Cap-and-Trade:    Government sets [QUANTITY] ──→ Market discovers [PRICE]
```

#### 2. Martin Weitzman's 'Prices vs Quantities' (1974)
Under conditions of scientific and economic uncertainty:
- If the **Marginal Damage curve is steep** (e.g., hitting irreversible climate tipping points), a **Quantity instrument (Cap-and-Trade)** is welfare-superior because catastrophic damage must be physically avoided.
- If the **Marginal Abatement Cost curve is steep**, a **Price instrument (Carbon Tax)** is superior because it protects the economy from wild cost spikes.

#### 3. Carbon Leakage and Border Adjustments (CBAM)
If Jurisdiction A imposes a stringent carbon price while Jurisdiction B imposes zero carbon costs, domestic industries in Jurisdiction A may relocate production to Jurisdiction B—exporting emissions and domestic jobs without reducing global warming (*carbon leakage*).
- **The Solution:** A **Carbon Border Adjustment Mechanism (CBAM)** levies an import tariff on energy-intensive goods (steel, cement, aluminum) entering from countries without equivalent carbon pricing, leveling the playing field.""",
            "readings": [
              {"label": "William D. Nordhaus, The Climate Casino: Risk, Uncertainty, and Economics for a Warming World (Yale, 2013)", "url": "https://yalebooks.yale.edu/book/9780300212648/the-climate-casino/"},
              {"label": "Martin L. Weitzman, Prices vs. Quantities (Review of Economic Studies, 1974)", "url": "https://www.jstor.org/stable/2296698"},
              {"label": "European Commission, Carbon Border Adjustment Mechanism (CBAM) Overview", "url": "https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en"}
            ],
            "quiz": [
              {
                "q": "What is the primary economic purpose of a Carbon Border Adjustment Mechanism (CBAM)?",
                "options": [
                  "To confiscate foreign transport ships entering domestic harbors.",
                  "To prevent 'carbon leakage' by leveling the playing field between domestic producers subject to carbon pricing and foreign competitors in jurisdictions without equivalent climate regulations.",
                  "To eliminate all international trade in consumer electronics.",
                  "To subsidize coal mining in developing economies."
                ],
                "answer": 1,
                "why": "A CBAM imposes an import carbon tariff on incoming goods, ensuring that domestic firms are not undercut by foreign rivals emitting carbon for free in unregulated foreign markets."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "econ-health-systems",
    "title": "Health Systems, Healthcare Financing Models & Pandemic Governance",
    "category": "Public Policy & Economics",
    "subcategory": "Health policy",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "A comparative macroeconomic and institutional analysis of global health systems and healthcare economics. Dissects Arrow's foundational insights on medical uncertainty, the Beveridge vs Bismarck vs National Health Insurance models, pharmaceutical pricing, and pandemic surveillance governance.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Master Kenneth Arrow's seminal 1963 economic framework on the unique market characteristics of healthcare.",
      "Compare the four major international healthcare models: Beveridge, Bismarck, National Health Insurance, and Out-of-Pocket.",
      "Analyze adverse selection, moral hazard, and risk-pooling mechanisms in private versus public insurance.",
      "Evaluate global pandemic surveillance, vaccine nationalism, and WHO International Health Regulations (IHR)."
    ],
    "modules": [
      {
        "title": "Module 1: Healthcare Economics and Comparative Health Systems",
        "lessons": [
          {
            "id": "econ-hs-l1",
            "title": "Arrow's Healthcare Economics and Comparative Financing Models",
            "body": """### Why Healthcare Cannot Be Treated as an Ordinary Market

In 1963, Nobel laureate Kenneth Arrow published *"Uncertainty and the Welfare Economics of Medical Care"*, establishing health economics as a distinct discipline. Arrow proved that healthcare violates virtually all assumptions of standard competitive markets:
- **Severe Asymmetry of Information:** Patients cannot self-diagnose complex pathologies or judge surgical treatments; they depend entirely on physician-providers who act simultaneously as their expert advisors and commercial sellers.
- **Extreme Uncertainty:** The incidence of catastrophic illness is unpredictable, catastrophic in cost, and completely involuntary.
- **Externalities:** Infectious diseases mean one person's health choices (vaccination, masking, antibiotics) directly protect or endanger the rest of the community.

```
Four Classical Healthcare Systems:
1. The Beveridge Model (UK NHS, Scandinavia):
   - Healthcare is provided and financed by the government through general progressive taxation. Hospitals are publicly owned, doctors are public employees.
2. The Bismarck Model (Germany, France, Japan):
   - Universal insurance financed jointly by employers and employees via non-profit sickness funds. Providers remain private.
3. The National Health Insurance Model (Canada, Taiwan):
   - Single-payer government insurance pays for healthcare delivered by private doctors and hospitals.
4. The Out-of-Pocket / Market Model (Developing nations / Uninsured US):
   - Medical care is purchased like a private commodity; individuals without funds receive no care.
```

#### 1. Adverse Selection and the Insurance Death Spiral
In an unregulated private health insurance market:
- Individuals with pre-existing conditions and high expected medical costs buy comprehensive insurance.
- Healthy young people opt out to save money.
- The insurer's risk pool deteriorates, forcing the insurer to raise premiums.
- Higher premiums cause the next tier of relatively healthy people to drop out.
- **The Death Spiral:** The cycle repeats until the insurance market collapses entirely or premiums become unaffordable for anyone.
- **The Regulatory Solution:** Universal coverage mandates, community rating (charging sick and healthy the same premium), and risk equalization subsidies.""",
            "readings": [
              {"label": "Kenneth J. Arrow, Uncertainty and the Welfare Economics of Medical Care (AER, 1963)", "url": "https://www.jstor.org/stable/1812044"},
              {"label": "T.R. Reid, The Healing of America: A Global Quest for Better, Cheaper, and Fairer Health Care (Penguin, 2010)", "url": "https://www.penguinrandomhouse.com/books/301140/the-healing-of-america-by-t-r-reid/"},
              {"label": "World Health Organization (WHO), World Health Report: Health Systems Financing", "url": "https://www.who.int/publications/i/item/9789241564052"}
            ],
            "quiz": [
              {
                "q": "What causes the 'Insurance Death Spiral' in an unregulated voluntary private health insurance market?",
                "options": [
                  "Hospitals run out of pharmaceutical supplies.",
                  "Healthy individuals opt out of insurance, causing the average risk and claims of the remaining pool to rise, driving up premiums and causing further healthy people to drop out until the market collapses.",
                  "Doctors are prohibited from billing patients directly.",
                  "Central banks raise national interest rates."
                ],
                "answer": 1,
                "why": "Adverse selection causes healthy individuals to exit high-cost pools, concentrating risk, raising premiums, and causing the entire risk-sharing pool to unravel unless universally mandated."
              }
            ]
          }
        ]
      }
    ]
  }
]

print(f"Public Policy & Economics courses compiled: {len(econ_courses)}/10")
