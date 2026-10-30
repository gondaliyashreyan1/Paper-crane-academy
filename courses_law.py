# Law Courses (1-10) for The Paper Crane Academy
faculty = "Faculty of Law, The Paper Crane Academy"

law_courses = [
  {
    "id": "law-constitutional",
    "title": "Constitutional Law: Principles, Separation of Powers & Judicial Review",
    "category": "Law",
    "subcategory": "Constitutional law",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "A comprehensive foundational study of modern constitutionalism. This course examines how written charters establish, divide, and constrain government authority, exploring separation of powers, the doctrine of checks and balances, the counter-majoritarian difficulty of judicial review, and the procedural boundaries of executive power.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Distinguish between parliamentary supremacy, judicial supremacy, and popular constitutionalism.",
      "Analyze the doctrinal foundations of judicial review established in Marbury v. Madison (1803) and comparative international frameworks.",
      "Evaluate the constitutional mechanisms of executive orders, war powers, and legislative oversight.",
      "Synthesize constitutional interpretation methods, comparing originalism, textualism, and living constitutionalism."
    ],
    "modules": [
      {
        "title": "Module 1: Foundations of Constitutionalism & Written Charters",
        "lessons": [
          {
            "id": "law-c1-l1",
            "title": "The Nature of Fundamental Law: Written Constitutions vs Parliamentary Sovereignty",
            "body": """### Fundamental Law and the Constitutional Compact

A constitution is not merely another statute passed by a legislature; it is the fundamental law (*lex fundamentalis*) from which all ordinary legislation derives its legitimacy. In constitutional theory, a fundamental tension exists between two primary architectures of state power:

1. **The Model of Parliamentary Supremacy (The Westminster Model):** Under the British constitutional tradition articulated by A.V. Dicey, Parliament holds supreme legal authority. It can make or unmake any law whatever; no person or body is recognized by the law as having a right to override or set aside the legislation of Parliament.
2. **The Model of Constitutional Supremacy:** Exemplified by the United States, post-war Germany (*Grundgesetz*), and South Africa (1996 Constitution), the written constitution sits at the apex of the legal hierarchy. Every branch of government—including the legislative majority—is legally subordinate to the text of the constitution.

#### Constitutional Legitimacy and Constituent Power
The distinction rests on the concept of **constituent power** (*pouvoir constituant*), first systematically articulated by Emmanuel-Joseph Sieyès during the French Revolution. Ordinary legislators possess only *constituted power* (*pouvoir constitué*); they act within the framework established by the sovereign people. Therefore, an ordinary act of parliament that contradicts the fundamental compact of the people is void *ab initio*.

```
Hierarchy of Laws (Kelsenian Stufenbaulehre):
[Grundnorm / Fundamental Constitution]
       ↓
[Organic & Constitutional Statutes]
       ↓
[Ordinary Parliamentary Legislation]
       ↓
[Executive Decrees, Administrative Rules & Bylaws]
```

#### Rigid vs Flexible Constitutions
Constitutions further bifurcate according to amendment difficulty (Lord Bryce's taxonomy). Flexible constitutions can be altered through ordinary legislative majorities (e.g., New Zealand). Rigid constitutions enforce heightened thresholds—such as supermajorities, state referenda, or regional ratification (e.g., Article V of the U.S. Constitution or Article 79(3) of Germany's Basic Law, which contains an immutable 'eternity clause' protecting democracy and human dignity from any amendment).""",
            "readings": [
              {"label": "A.V. Dicey, Introduction to the Study of the Law of the Constitution (1885)", "url": "https://www.gutenberg.org/ebooks/57519"},
              {"label": "U.S. National Archives, The Constitution of the United States", "url": "https://www.archives.gov/founding-docs/constitution"},
              {"label": "Federal Constitutional Court of Germany, Basic Law Overview", "url": "https://www.bundesverfassungsgericht.de/EN/Das-Gericht/Grundgesetz/grundgesetz_node.html"}
            ],
            "quiz": [
              {
                "q": "What distinguishes constituent power (pouvoir constituant) from constituted power (pouvoir constitué)?",
                "options": [
                  "Constituted power creates the constitution; constituent power passes ordinary taxes.",
                  "Constituent power resides in the sovereign authority to create a constitutional framework, whereas constituted power is the delegated authority exercising governance under that framework.",
                  "Constituent power is exclusive to monarchies, while constituted power applies only in federal democracies.",
                  "There is no distinction; both terms refer interchangeably to administrative rulemaking."
                ],
                "answer": 1,
                "why": "Constituent power is the primordial authority of the people to draft and enact a constitution, whereas constituted bodies (presidents, parliaments, courts) derive all their legitimate authority from that constitution."
              },
              {
                "q": "What is an 'eternity clause' (Ewigkeitsklausel) in constitutional law?",
                "options": [
                  "A clause granting judges lifetime tenure without any retirement age.",
                  "A provision stating that national elections must occur every four years indefinitely.",
                  "A constitutional provision that prohibits any amendment that would alter certain core principles, such as human dignity or the democratic state form.",
                  "A clause allowing international treaties to supersede domestic law permanently."
                ],
                "answer": 2,
                "why": "Article 79(3) of Germany's Basic Law is the classic example of an eternity clause: it places human dignity and the federal, democratic republic beyond the reach of any legislative amendment."
              }
            ]
          },
          {
            "id": "law-c1-l2",
            "title": "Separation of Powers: Functional Independence and Dynamic Checks",
            "body": """### The Architectural Separation of Powers

The doctrine of the separation of powers is rooted in Montesquieu's *De l'esprit des lois* (1748), which warned that political liberty is imperiled whenever legislative, executive, and judicial authorities are concentrated in a single magistrate or assembly:

> *"When the legislative and executive powers are united in the same person, or in the same body of magistrates, there can be no liberty; because apprehensions may arise, lest the same monarch or senate should enact tyrannical laws, to execute them in a tyrannical manner."*

#### Strict Separation vs Checks and Balances
Constitutional systems operationalize Montesquieu's principle in two divergent manners:
1. **Strict Tripartite Separation:** Each branch possesses a distinct constitutional sphere into which other branches cannot trespass.
2. **Checks and Balances (Madisonian Model):** As James Madison articulated in *Federalist No. 51*, ambition must be made to counteract ambition. The branches are deliberately interconnected so that each exercises constitutional defenses against the usurpations of the others:
   - The Executive holds a qualified veto over congressional legislation.
   - The Legislature controls the power of the purse and holds the power of impeachment.
   - The Judiciary interprets the laws and evaluates executive/legislative action against constitutional benchmarks.

#### The Doctrine of Non-Delegation
A crucial modern battlefield in separation of powers jurisprudence is the **non-delegation doctrine**. Derived from the maxim *delegata potestas non potest delegari* (no delegated power can be further delegated), it posits that when the constitution vests legislative power in a parliament or congress, that body cannot surrender its essential lawmaking function to executive regulatory agencies without providing an 'intelligible principle' to direct administrative discretion (*J.W. Hampton v. United States*, 1928).""",
            "readings": [
              {"label": "Montesquieu, The Spirit of Laws, Book XI (1748)", "url": "https://avalon.law.yale.edu/18th_century/montesquieu_11.asp"},
              {"label": "James Madison, Federalist No. 51: Checks and Balances (1788)", "url": "https://avalon.law.yale.edu/18th_century/fed51.asp"},
              {"label": "Cornell LII, Nondelegation Doctrine Overview", "url": "https://www.law.cornell.edu/wex/nondelegation_doctrine"}
            ],
            "quiz": [
              {
                "q": "What was James Madison's primary defense of the system of checks and balances in Federalist No. 51?",
                "options": [
                  "Government officials are naturally altruistic and require no institutional constraints.",
                  "Complete separation without mutual checks leads to one branch gradually encroaching upon and dominating the others.",
                  "The judiciary should command military forces to balance legislative spending.",
                  "Executive decrees must always supersede legislative statutes during economic emergencies."
                ],
                "answer": 1,
                "why": "Madison argued that parchment barriers are insufficient to prevent tyranny; each department must be given the constitutional means and personal motives to resist encroachments by the other departments."
              }
            ]
          }
        ]
      },
      {
        "title": "Module 2: Judicial Supremacy, Review & Constitutional Interpretation",
        "lessons": [
          {
            "id": "law-c1-l3",
            "title": "The Mechanics of Judicial Review: Marbury v. Madison to Modern Constitutional Courts",
            "body": """### The Genesis of Judicial Review

In *Marbury v. Madison* (1803), Chief Justice John Marshall confronted a perilous institutional crisis. Outgoing Federalist President John Adams had appointed William Marbury as a justice of the peace, but the commission was not delivered before Thomas Jefferson assumed office. Jefferson ordered Secretary of State James Madison to withhold the commission.

Marbury petitioned the Supreme Court directly for a writ of mandamus under Section 13 of the Judiciary Act of 1789.

#### Marshall's Judicial Masterstroke
Marshall faced a dilemma: if he ordered Madison to deliver the commission, the Jefferson administration would ignore the order, exposing the Court's complete lack of enforcement power (*The judiciary has 'neither force nor will, but merely judgment'*—Hamilton, *Federalist No. 78*). If he refused to act, the Court would appear timid and powerless.

Marshall escaped the trap by declaring that:
1. Marbury had a legal right to his commission.
2. The laws of the United States provided a remedy for the violation of that right.
3. However, Section 13 of the Judiciary Act of 1789, which purported to expand the Supreme Court's **original jurisdiction** to issue writs of mandamus to public officers, was unconstitutional because Article III of the Constitution explicitly limits the Court's original jurisdiction to ambassadors, public ministers, and cases in which a state is a party.

```
Article III, Section 2 (Constitutional Ceiling)
               vs
Section 13, Judiciary Act of 1789 (Statutory Expansion)
               ↓
Rule of Law: The Constitution controls any contrary legislative act.
```

By striking down a federal statute that gave his own Court power, Marshall established the irrevocable precedent:
> *"It is emphatically the province and duty of the judicial department to say what the law is. Those who apply the rule to particular cases, must of necessity expound and interpret that rule."*

#### Comparative Review: Diffuse vs Concentrated Models
- **Diffuse Review (American Model):** Any court of general jurisdiction can determine the constitutionality of a law in an active 'case or controversy'.
- **Concentrated Review (European / Kelsenian Model):** Pioneer by legal theorist Hans Kelsen in Austria (1920) and adopted across Europe, judicial review is centralized in a dedicated, specialized **Constitutional Court** (*Verfassungsgericht*), which often exercises abstract review without requiring an ongoing private lawsuit.""",
            "readings": [
              {"label": "Marbury v. Madison, 5 U.S. (1 Cranch) 137 (1803)", "url": "https://www.law.cornell.edu/supremecourt/text/5/137"},
              {"label": "Alexander Hamilton, Federalist No. 78 (1788)", "url": "https://avalon.law.yale.edu/18th_century/fed78.asp"},
              {"label": "Stanford Encyclopedia of Philosophy, Constitutionalism", "url": "https://plato.stanford.edu/entries/constitutionalism/"}
            ],
            "quiz": [
              {
                "q": "Why did Chief Justice John Marshall strike down Section 13 of the Judiciary Act of 1789 in Marbury v. Madison?",
                "options": [
                  "Because Marbury was not a citizen of the United States.",
                  "Because Congress had attempted to expand the Supreme Court's original jurisdiction beyond the boundaries defined in Article III of the Constitution.",
                  "Because the President possesses absolute immunity from all legal review.",
                  "Because the Judiciary Act was passed without a quorum in the Senate."
                ],
                "answer": 1,
                "why": "Article III specifies the limited categories of the Supreme Court's original jurisdiction; Congress could not add mandamus suits against executive officers to that list via ordinary statute."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "law-international",
    "title": "Public International Law: Sovereignty, Treaties & Customary Norms",
    "category": "Law",
    "subcategory": "International law",
    "level": "Undergraduate",
    "duration": "7 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "An advanced examination of the international legal order governing relations between sovereign states. Students analyze the Article 38 sources of international law, the doctrinal evolution of sovereign equality since the Peace of Westphalia, treaty interpretation under the Vienna Convention, state jurisdiction, immunity, and peaceful dispute resolution before the International Court of Justice.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Categorize and apply the Article 38(1) ICJ Statute sources: treaties, custom, general principles, and subsidiary means.",
      "Analyze the twin requirements of customary international law: state practice (usus) and opinio juris sive necessitatis.",
      "Interpret treaties using the Vienna Convention on the Law of Treaties (VCLT Articles 31-32).",
      "Evaluate jurisdictional doctrines: territoriality, nationality, passive personality, protective principle, and universal jurisdiction."
    ],
    "modules": [
      {
        "title": "Module 1: The Sources of International Law",
        "lessons": [
          {
            "id": "law-i1-l1",
            "title": "Article 38(1) ICJ Statute: Treaties, Customary Law, and General Principles",
            "body": """### The Architecture of Global Legal Obligation

Unlike domestic legal orders, international law lacks a centralized sovereign legislature, an executive police force with global jurisdiction, or mandatory universal adjudication. Instead, international legal obligations are founded upon state consent.

The canonical catalog of international legal sources is codified in **Article 38(1) of the Statute of the International Court of Justice (ICJ)**:

1. **International Conventions (Treaties):** Formal written agreements between states governed by international law (e.g., the UN Charter, Geneva Conventions, UNCLOS).
2. **International Custom (*Consuetudo*):** General practice accepted as law, constituted by two cumulative components:
   - *State Practice (diuturnitas / usus):* Extensive, consistent, and representative conduct by states over time.
   - *Opinio Juris Sive Necessitatis:* The psychological conviction that such practice is rendered obligatory by the existence of a rule of law requiring it (*North Sea Continental Shelf Cases*, ICJ 1969).
3. **General Principles of Law:** Norms recognized by civilized nations across domestic legal traditions (e.g., *good faith*, *res judicata*, *lex specialis derogat legi generali*).
4. **Subsidiary Means:** Judicial decisions and the teachings of the most highly qualified publicists (*teachings of the masters*).

```
          Article 38(1) ICJ Hierarchy:
            [Jus Cogens Norms] (Peremptory)
                   ↓
      [Treaties]  ↔  [Customary International Law]
                   ↓
         [General Principles of Law]
                   ↓
   [Judicial Decisions & Academic Commentary]
```

#### Jus Cogens: Peremptory Norms
Above ordinary treaty provisions and bilateral custom sit **jus cogens** (peremptory norms), defined under Article 53 of the Vienna Convention on the Law of Treaties as norms from which no derogation is permitted. Any treaty that conflicts with a peremptory norm (such as the prohibitions against aggressive war, genocide, slavery, and torture) is void *ab initio*.""",
            "readings": [
              {"label": "Statute of the International Court of Justice (Article 38)", "url": "https://www.icj-cij.org/statute"},
              {"label": "North Sea Continental Shelf Cases (Germany v. Denmark/Netherlands), ICJ 1969", "url": "https://www.icj-cij.org/case/51"},
              {"label": "Vienna Convention on the Law of Treaties (1969)", "url": "https://legal.un.org/ilc/texts/instruments/english/conventions/1_1_1969.pdf"}
            ],
            "quiz": [
              {
                "q": "What two elements must be proven to establish the existence of a rule of customary international law?",
                "options": [
                  "A formal treaty signing and a Security Council resolution.",
                  "Consistent and general state practice (usus), accompanied by the belief that the practice is legally obligatory (opinio juris).",
                  "A ruling by the International Criminal Court and approval by the UN Secretary-General.",
                  "Uniform domestic statutes across all member states of the G20."
                ],
                "answer": 1,
                "why": "Under settled ICJ jurisprudence, customary law requires both objective widespread state practice and the subjective conviction (opinio juris) that the conduct is mandatory under international law."
              }
            ]
          }
        ]
      },
      {
        "title": "Module 2: State Jurisdiction and Sovereign Immunity",
        "lessons": [
          {
            "id": "law-i1-l2",
            "title": "Territoriality, Nationality, and Universal Jurisdiction",
            "body": """### The Bases of State Jurisdiction

Jurisdiction in international law refers to a state's sovereign competence to prescribe, adjudicate, and enforce rules of law. Under the foundational **SS Lotus Case** (PCIJ 1927), a sovereign state possesses wide discretion to exercise jurisdiction within its own territory and may extend its laws extraterritorially unless prohibited by an explicit prohibitive rule of international law.

#### The Five Recognized Heads of Jurisdiction
1. **Territorial Principle:** Jurisdiction over acts committed on the state's sovereign soil, internal waters, or registered ships/aircraft (Subjective territoriality: where the act begins; Objective/Effects doctrine: where the act produces substantial harm).
2. **Nationality Principle (Active Personality):** Jurisdiction over offenses committed by the state's own citizens anywhere in the world.
3. **Passive Personality Principle:** Jurisdiction based on the nationality of the *victim* of the crime (widely utilized in counter-terrorism statutes).
4. **Protective Principle:** Jurisdiction over acts committed abroad by foreigners that directly threaten the state's national security, currency, or core government integrity (e.g., espionage, counterfeiting official currency).
5. **Universal Jurisdiction:** Jurisdiction over crimes of such heinous universal concern that any state may prosecute the offender regardless of nationality or location of the offense (e.g., piracy on the high seas, genocide, crimes against humanity, war crimes).""",
            "readings": [
              {"label": "SS Lotus Case (France v. Turkey), PCIJ Series A No. 10 (1927)", "url": "https://www.icj-cij.org/pcij-series-a"},
              {"label": "Arrest Warrant of 11 April 2000 (DRC v. Belgium), ICJ 2002", "url": "https://www.icj-cij.org/case/121"}
            ],
            "quiz": [
              {
                "q": "Which jurisdictional principle permits a state to prosecute an individual for crimes committed abroad with no connection to the prosecuting state's territory, citizens, or direct security?",
                "options": [
                  "The Protective Principle",
                  "Universal Jurisdiction",
                  "Passive Personality Principle",
                  "Active Nationality Principle"
                ],
                "answer": 1,
                "why": "Universal jurisdiction applies to offenses against the international community as a whole (hostis humani generis), such as piracy, war crimes, and genocide, allowing any competent domestic court to prosecute."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "law-criminal-justice",
    "title": "Criminal Jurisprudence: Actus Reus, Mens Rea & Penal Theory",
    "category": "Law",
    "subcategory": "Criminal justice",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "A rigorous theoretical and doctrinal exploration of substantive criminal law and penal philosophy. Students examine the anatomy of criminal liability—deconstructing the voluntary physical act (actus reus) and culpable mental state (mens rea)—before analyzing general affirmative defenses (duress, self-defense, insanity) and competing moral justifications of punishment.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Deconstruct the dual elements of criminal liability: Actus Reus and Mens Rea.",
      "Analyze the Model Penal Code culpable mental states: Purpose, Knowledge, Recklessness, and Negligence.",
      "Evaluate affirmative defenses distinguishing between justifications (self-defense) and excuses (insanity, duress).",
      "Critique competing theories of state punishment: Retributivism vs Consequentialist Deterrence."
    ],
    "modules": [
      {
        "title": "Module 1: The Core Structure of Criminal Liability",
        "lessons": [
          {
            "id": "law-cr-l1",
            "title": "Actus Reus: Voluntary Conduct, Omissions, and Causation",
            "body": """### The Physical Element of Criminal Offenses

The ancient Latin maxim *Actus non facit reum nisi mens sit rea*—the act is not culpable unless the mind is guilty—forms the bedrock of Anglo-American and continental criminal law. 

#### 1. The Voluntary Act Requirement
Criminal law punishes voluntary acts, not internal thoughts or involuntary spasms. Under Section 2.01 of the American Law Institute's Model Penal Code (MPC), bodily movements during sleepwalking, hypnosis, epileptic seizures, or involuntary reflexes are not voluntary acts.

#### 2. Liability for Omissions (Negative Acts)
As a general rule, Anglo-American common law imposes no duty to rescue a stranger in distress (*the 'Bad Samaritan' principle*). However, an omission generates criminal liability when a legal duty to act exists:
- **Status Relationship:** Parent to infant child; spouse to spouse.
- **Contractual Duty:** Lifeguard, train signal operator, or physician.
- **Statutory Mandate:** Duty to stop and render aid after a traffic accident; duty to file tax returns.
- **Creation of Peril:** If a person innocently or culpably creates a dangerous situation, they incur a legal duty to take reasonable steps to prevent harm (*R v Miller*, 1983).

#### 3. Principles of Causation
Where an offense requires a prohibited result (e.g., homicide), the prosecution must prove two distinct causation branches:
1. **Factual Causation (Cause-in-Fact):** Established through the *'but-for'* test (*sine qua non*): But for the defendant's act, would the prohibited harm have occurred when it did?
2. **Proximate / Legal Causation:** Was the result foreseeable and sufficiently related to the defendant's conduct, or was the causal chain broken by an unforeseeable intervening act (*novus actus interveniens*)?""",
            "readings": [
              {"label": "Model Penal Code, Selected Provisions (Section 2.01-2.03)", "url": "https://www.law.cornell.edu/wex/model_penal_code"},
              {"label": "Stanford Encyclopedia of Philosophy, Theories of Criminal Law", "url": "https://plato.stanford.edu/entries/criminal-law/"}
            ],
            "quiz": [
              {
                "q": "Under common law principles, when does an omission to act constitute the actus reus of a crime?",
                "options": [
                  "Whenever a bystander possesses the physical capacity to prevent a felony.",
                  "Only when the defendant was under a pre-existing legal duty to act created by statute, contract, relationship, or creation of peril.",
                  "In every scenario involving life-threatening danger.",
                  "Never; criminal law only punishes active physical commissions."
                ],
                "answer": 1,
                "why": "Unlike general moral obligations, criminal omission liability requires an explicit legal duty to act arising from contract, status relationship, statute, or the voluntary assumption of care/creation of peril."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "law-human-rights",
    "title": "International Human Rights Law: Treaties, Regional Courts & Enforcement",
    "category": "Law",
    "subcategory": "Human rights",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "An exhaustive analysis of the normative foundations and enforcement machinery of global human rights. Students study the Universal Declaration of Human Rights, the ICCPR, the ICESCR, the jurisprudence of the European Court of Human Rights in Strasbourg, and the mechanisms of international human rights reporting and sanctions.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Distinguish between civil and political rights (first generation) and economic, social, and cultural rights (second generation).",
      "Evaluate the proportionality test utilized by the European Court of Human Rights to evaluate rights restrictions.",
      "Analyze non-derogable rights under Article 4 of the International Covenant on Civil and Political Rights (ICCPR).",
      "Critique enforcement gaps and sovereign compliance mechanisms under UN treaty monitoring bodies."
    ],
    "modules": [
      {
        "title": "Module 1: The Universal Architecture of Human Rights",
        "lessons": [
          {
            "id": "law-hr-l1",
            "title": "The International Bill of Human Rights and the Proportionality Test",
            "body": """### The Triad of Universal Human Rights

Modern international human rights law emerged from the ashes of World War II, repudiating the Westphalian principle that a sovereign state's treatment of its own citizens is purely an internal domestic affair.

The foundational framework is known as the **International Bill of Human Rights**, comprising:
1. **Universal Declaration of Human Rights (UDHR, 1948):** Adopted by the UN General Assembly under the leadership of Eleanor Roosevelt; initially conceived as a non-binding moral manifesto, many of its core provisions are now acknowledged as customary international law.
2. **International Covenant on Civil and Political Rights (ICCPR, 1966):** Legally binding treaty guaranteeing negative rights—liberty from state interference, right to life, freedom from torture, fair trial, freedom of speech and assembly.
3. **International Covenant on Economic, Social and Cultural Rights (ICESCR, 1966):** Legally binding treaty mandating positive obligations—rights to education, healthcare, fair wages, and housing, subject to 'progressive realization'.

#### The Four-Stage Proportionality Framework
Most fundamental rights are qualified rather than absolute. When a government restricts a protected right (such as freedom of assembly or privacy), international and regional courts apply the rigorous **proportionality test**:

1. **Legality:** Is the restriction prescribed by accessible and clear law?
2. **Legitimate Aim:** Does the state pursue an authorized public objective (e.g., national security, public health, protection of the rights of others)?
3. **Suitability:** Is the restrictive measure logically capable of achieving the stated legitimate aim?
4. **Necessity & Proportionality Stricto Sensu:** Is this the least restrictive means available? Do the public benefits outweigh the severe intrusion on the fundamental right?""",
            "readings": [
              {"label": "Universal Declaration of Human Rights (UN, 1948)", "url": "https://www.un.org/en/about-us/universal-declaration-of-human-rights"},
              {"label": "International Covenant on Civil and Political Rights (OHCHR, 1966)", "url": "https://www.ohchr.org/en/instruments-mechanisms/instruments/international-covenant-civil-and-political-rights"},
              {"label": "European Court of Human Rights, Guide on Article 8 (Right to Privacy)", "url": "https://www.echr.coe.int/documents/d/echr/guide_art_8_eng"}
            ],
            "quiz": [
              {
                "q": "What is meant by the doctrine of 'progressive realization' under the ICESCR?",
                "options": [
                  "States can indefinitely ignore socio-economic rights without international review.",
                  "States acknowledge that economic and social rights require financial resources and commit to taking continuous, targeted steps to the maximum of their available resources to fully realize them over time.",
                  "Economic rights only apply to high-income OECD economies.",
                  "Courts must immediately enforce every social welfare claim as an absolute immediate injunction."
                ],
                "answer": 1,
                "why": "Article 2(1) of the ICESCR explicitly recognizes that realizing rights to health and education depends on state resource capacities, requiring progressive and deliberate advancement."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "law-humanitarian",
    "title": "International Humanitarian Law & the Law of Armed Conflict",
    "category": "Law",
    "subcategory": "International law",
    "level": "Undergraduate",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "A deep dive into the legal regimes governing warfare. This course deconstructs the Geneva Conventions of 1949, their Additional Protocols, the fundamental principles of distinction, military necessity, and proportionality, the categorization of armed conflicts (IAC vs NIAC), and the international accountability of combatants.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Distinguish between Jus ad Bellum (legality of resorting to war) and Jus in Bello (rules governing conduct during war).",
      "Apply the core cardinal principles: Distinction, Proportionality, Military Necessity, and Prohibition of Unnecessary Suffering.",
      "Categorize International Armed Conflicts (IACs) versus Non-International Armed Conflicts (NIACs).",
      "Evaluate combatant immunity and prisoner of war (POW) status under the Third Geneva Convention."
    ],
    "modules": [
      {
        "title": "Module 1: The Cardinal Principles of the Geneva Conventions",
        "lessons": [
          {
            "id": "law-ihl-l1",
            "title": "Distinction, Proportionality, and Military Necessity",
            "body": """### The Strict Independence of Jus in Bello

A foundational axiom of modern international humanitarian law (IHL) is the complete separation between **Jus ad Bellum** (the legality of entering armed conflict under Article 2(4) and 51 of the UN Charter) and **Jus in Bello** (the rules regulating how warfare is conducted, codified primarily in the Hague Regulations and the four Geneva Conventions of 1949).

Regardless of which side unlawfully initiated the conflict, both the aggressor and the defending state are bound identically by the laws of armed conflict.

#### The Three Core Pillars of IHL
1. **The Principle of Distinction (Article 48, Additional Protocol I):** Belligerents must at all times distinguish between the civilian population and combatants, and between civilian objects and military objectives. Attacks may only be directed against military objectives. Direct targeting of civilians is a grave breach and a war crime.
2. **The Principle of Proportionality (Article 51(5)(b), Additional Protocol I):** An attack against an otherwise legitimate military target is strictly unlawful if it is expected to cause incidental loss of civilian life, injury to civilians, or damage to civilian objects that would be *excessive in relation to the concrete and direct military advantage anticipated*.
3. **Military Necessity:** Belligerents may only apply the amount and kind of force necessary to achieve the legitimate military defeat of the enemy in the shortest time with the least expenditure of life and resources. It never justifies violations of positive peremptory IHL prohibitions.""",
            "readings": [
              {"label": "ICRC, The Geneva Conventions of 12 August 1949 Overview", "url": "https://www.icrc.org/en/war-and-law/treaties-customary-law/geneva-conventions"},
              {"label": "Protocol Additional to the Geneva Conventions (Protocol I, 1977)", "url": "https://ihl-databases.icrc.org/en/ihl-treaties/api-1977"}
            ],
            "quiz": [
              {
                "q": "Under the principle of proportionality in IHL, when is an attack on a legitimate military objective deemed unlawful?",
                "options": [
                  "Whenever any civilian casualty occurs, regardless of numbers.",
                  "When the expected incidental civilian harm is excessive in relation to the concrete and direct military advantage anticipated.",
                  "Only when high-ranking political officials are affected.",
                  "Never; legitimate military targets may be struck with unlimited force."
                ],
                "answer": 1,
                "why": "IHL does not ban all incidental civilian casualties, but it makes an attack criminal if the expected civilian harm is excessive in relation to the anticipated direct military gain."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "law-ocean-governance",
    "title": "The Law of the Sea & Global Maritime Governance (UNCLOS)",
    "category": "Law",
    "subcategory": "International law",
    "level": "Pre-university",
    "duration": "5 weeks (3 hours/week)",
    "instructor": faculty,
    "description": "An exhaustive examination of the 'Constitution for the Oceans': the United Nations Convention on the Law of the Sea (UNCLOS 1982). Students explore the delineation of maritime zones, baseline calculations, innocent passage through territorial seas, resource exploitation in the Exclusive Economic Zone (EEZ), the continental shelf, and maritime dispute arbitrations.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Calculate baselines and delineate the five major maritime zones under UNCLOS.",
      "Distinguish between sovereign territorial waters, the Exclusive Economic Zone, and the High Seas.",
      "Analyze navigation rights: Innocent passage vs transit passage through international straits.",
      "Evaluate landmark international maritime arbitrations (e.g., South China Sea Arbitration 2016)."
    ],
    "modules": [
      {
        "title": "Module 1: Maritime Zonation and Sovereign Rights",
        "lessons": [
          {
            "id": "law-los-l1",
            "title": "From Territorial Seas to the High Seas: The Five Zones of UNCLOS",
            "body": """### The Spatial Architecture of the Oceans

Signed in Montego Bay in 1982 after decades of negotiations, UNCLOS settled centuries of conflict between the doctrine of *Mare Liberum* (freedom of the seas, championed by Hugo Grotius) and *Mare Clausum* (enclosed sovereign sea claims).

UNCLOS establishes a sliding scale of sovereign control, measured in nautical miles (NM) from the coastal baseline (typically the low-water mark along the coast):

```
Land ← Baseline → 12 NM [Territorial Sea] → 24 NM [Contiguous Zone] → 200 NM [EEZ] → [High Seas]
Full Sovereignty       Innocent Passage       Customs/Fiscal Checks    Resource Rights  Global Commons
```

1. **Internal Waters:** Landward of the baseline (ports, rivers, bays). The coastal state exercises absolute, unconditional territorial sovereignty; foreign vessels have no automatic right of entry.
2. **Territorial Sea (Up to 12 NM):** Full state sovereignty extends to the waters, seabed, subsoil, and airspace. However, foreign vessels enjoy the universal right of **innocent passage**—passage that is continuous, expeditious, and not prejudicial to the peace, good order, or security of the coastal state.
3. **Contiguous Zone (Up to 24 NM):** Coastal states may exercise limited control necessary to prevent and punish infringement of its customs, fiscal, immigration, or sanitary laws committed within its territory or territorial sea.
4. **Exclusive Economic Zone (EEZ, Up to 200 NM):** The coastal state does not own the water column as sovereign territory, but possesses exclusive **sovereign rights for exploring and exploiting, conserving and managing natural resources** (fisheries, oil, gas, offshore wind) in the waters, seabed, and subsoil. Foreign states retain complete freedoms of navigation and overflight.
5. **The High Seas (Beyond 200 NM):** Open to all nations; no state may validly purport to subject any part of them to its sovereignty (*res communis* / common heritage of mankind).""",
            "readings": [
              {"label": "United Nations Convention on the Law of the Sea (UNCLOS, 1982)", "url": "https://www.un.org/depts/los/convention_agreements/texts/unclos/unclos_e.pdf"},
              {"label": "Permanent Court of Arbitration, South China Sea Award (2016)", "url": "https://pca-cpa.org/en/cases/7/"}
            ],
            "quiz": [
              {
                "q": "What rights does a coastal state exercise within its 200-nautical-mile Exclusive Economic Zone (EEZ)?",
                "options": [
                  "Complete territorial sovereignty including the right to prohibit foreign merchant ships from navigating.",
                  "Sovereign rights over natural resources (fishing, seabed minerals, energy), while other states retain freedom of navigation and overflight.",
                  "No special rights beyond those of any other nation on the high seas.",
                  "The power to annex foreign vessels without legal justification."
                ],
                "answer": 1,
                "why": "The EEZ is a sui generis regime: the coastal state controls economic resources, but foreign vessels retain freedom of navigation and overflight."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "law-environmental",
    "title": "International Environmental Law & Climate Litigation",
    "category": "Law",
    "subcategory": "Environmental law",
    "level": "Undergraduate",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "An in-depth study of the rapid evolution of international environmental law from transboundary pollution treaties to modern climate litigation. Students examine landmark principles including the precautionary principle, polluter pays, and common but differentiated responsibilities (CBDR), alongside domestic and international court battles holding governments and corporations accountable for greenhouse gas emissions.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Analyze the foundational Trail Smelter arbitration and the 'no-harm' principle in customary environmental law.",
      "Deconstruct the treaty architecture from the 1992 Rio Declaration to the 2015 Paris Agreement.",
      "Evaluate the application of the Precautionary Principle and the Polluter Pays Principle.",
      "Critique ground-breaking strategic climate lawsuits (e.g., Urgenda, Neubauer, Shell)."
    ],
    "modules": [
      {
        "title": "Module 1: Principles of Transboundary Environmental Responsibility",
        "lessons": [
          {
            "id": "law-env-l1",
            "title": "The No-Harm Rule, Precaution, and the Paris Agreement Architecture",
            "body": """### The Evolution from Nuisance to Global Commons

International environmental law originated with the seminal **Trail Smelter arbitration** (US v. Canada, 1938/1941), where sulfur dioxide fumes from a Canadian smelter damaged crops in Washington State. The arbitral tribunal formulated the bedrock **no-harm rule**:

> *"No state has the right to use or permit the use of its territory in such a manner as to cause injury by fumes in or to the territory of another or the properties or persons therein."*

#### Core Normative Principles (Rio 1992)
1. **The Precautionary Principle (Principle 15):** Where there are threats of serious or irreversible damage, lack of full scientific certainty shall not be used as a reason for postponing cost-effective measures to prevent environmental degradation.
2. **Common But Differentiated Responsibilities and Respective Capabilities (CBDR-RC):** Recognizes that while all states share a common duty to protect the planetary biosphere, developed states bear a historical responsibility for cumulative greenhouse gas emissions and possess greater financial/technological capacity to remediate harm.
3. **The Polluter Pays Principle:** The polluter should, in principle, bear the costs of pollution, ensuring that ecological externalities are internalised into industrial costs.

#### The Strategic Litigation Revolution
Frustrated by slow multilateral negotiations, non-governmental organizations and youth plaintiffs have launched pioneering rights-based climate litigation:
- **Urgenda Foundation v. State of the Netherlands (2019):** The Dutch Supreme Court held that the government's failure to reduce emissions by at least 25% by 2020 violated Articles 2 (Right to Life) and 8 (Right to Private and Family Life) of the European Convention on Human Rights.
- **Neubauer v. Germany (Federal Constitutional Court, 2021):** Struck down parts of Germany's Climate Protection Act because delaying major emission reductions past 2030 offloaded an unconstitutional burden of fundamental freedom restrictions onto the shoulders of future youth generations.""",
            "readings": [
              {"label": "Trail Smelter Arbitration (US v. Canada), 1938/1941", "url": "https://legal.un.org/riaa/cases/vol_III/1905-1982.pdf"},
              {"label": "Urgenda Foundation v. The State of the Netherlands (2019 Judgment)", "url": "https://www.urgenda.nl/en/climate-case/"},
              {"label": "UNFCCC, The Paris Agreement (2015)", "url": "https://unfccc.int/process-and-meetings/the-paris-agreement"}
            ],
            "quiz": [
              {
                "q": "What was the landmark legal precedent established by the Dutch Supreme Court in Urgenda v. State of the Netherlands?",
                "options": [
                  "States have no legal duty under human rights treaties to combat global warming.",
                  "A sovereign state owes a legally binding duty of care under human rights law (Articles 2 and 8 ECHR) to take adequate preventive measures against dangerous climate change.",
                  "Only international arbitral tribunals possess jurisdiction over carbon emissions.",
                  "Carbon taxes are unconstitutional under European Union single-market rules."
                ],
                "answer": 1,
                "why": "The Dutch Supreme Court confirmed that the positive obligations under Articles 2 and 8 of the ECHR require the state to protect citizens from the real and imminent threat of dangerous climate change."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "law-contract-civil",
    "title": "Contract Law & The Architecture of Civil Obligations",
    "category": "Law",
    "subcategory": "Legal systems and jurisprudence",
    "level": "Pre-university",
    "duration": "6 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "An analytical study of how legal systems enforce voluntary promises. This course investigates the core elements of contract formation (offer, acceptance, consideration, intention to create legal relations), vitiating factors that unravel agreements (misrepresentation, duress, undue influence, mistake), and the principles governing breach, damages, and specific performance.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Differentiate between valid offers and invitations to treat in commercial transactions.",
      "Apply the common law doctrine of consideration and promissory estoppel.",
      "Analyze vitiating factors: Fraudulent misrepresentation, economic duress, and mutual mistake.",
      "Calculate contractual expectation damages and explain the limits of remoteness (Hadley v Baxendale)."
    ],
    "modules": [
      {
        "title": "Module 1: Formation and the Doctrine of Consideration",
        "lessons": [
          {
            "id": "law-con-l1",
            "title": "Offer, Acceptance, and the Exchange of Consideration",
            "body": """### The Legal Enforceability of Promises

In private law, a contract is a legally enforceable agreement that generates mutual rights and obligations (*vinculum juris*). 

#### 1. Offer vs Invitation to Treat
An offer is an expression of willingness to contract on specified terms, made with the intention that it shall become binding as soon as it is accepted. It must be distinguished from an **invitation to treat** (*invitatio ad offerendum*)—an invitation for the other party to make an offer. 
- Displays of goods on shop shelves or in shop windows are merely invitations to treat (*Pharmaceutical Society of Great Britain v Boots Chemists*, 1953).
- Advertisements are generally invitations to treat, unless they make a clear unilateral promise intended to be legally binding upon performance (*Carlill v Carbolic Smoke Ball Co*, 1893).

#### 2. The Doctrine of Consideration
The distinctive feature of common law contracts (unlike civil law systems based on French *cause* or German *Rechtsgeschäft*) is **consideration**: something of value in the eye of the law given in exchange for a promise (*quid pro quo*).
- Consideration must be *sufficient* (have economic value), but need not be *adequate* (courts will not inquire whether you made a foolish bargain; a peppercorn is good consideration).
- **Past consideration is no consideration:** An act performed before a promise is made cannot serve as legal consideration for that subsequent promise (*Roscorla v Thomas*, 1842).
- **Promissory Estoppel:** Where a party makes a clear promise not to enforce strict legal rights, intending the other party to rely on it, equity prevents the promisor from reneging on that promise where it would be inequitable (*Central London Property Trust v High Trees House*, 1947).""",
            "readings": [
              {"label": "Carlill v Carbolic Smoke Ball Co [1893] 1 QB 256", "url": "https://www.bailii.org/ew/cases/EWCA/Civ/1892/1.html"},
              {"label": "Cornell LII, Contract Law Overview", "url": "https://www.law.cornell.edu/wex/contract"}
            ],
            "quiz": [
              {
                "q": "Why was the advertisement in Carlill v Carbolic Smoke Ball Co held to be a binding contract rather than a mere sales puff?",
                "options": [
                  "Because it was published in a major newspaper.",
                  "Because the company explicitly stated it had deposited £1,000 in the Alliance Bank to demonstrate its sincerity, creating a unilateral offer to anyone who performed the conditions.",
                  "Because Mrs. Carlill had signed a physical deed prior to using the product.",
                  "Because all commercial advertisements are automatically enforceable warranties."
                ],
                "answer": 1,
                "why": "The deposit of £1,000 in the bank proved objective legal intent to be bound, converting the advertisement into an enforceable unilateral offer accepted by performance."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "law-tort-liability",
    "title": "Tort Law: Negligence, Strict Liability & Civil Wrongs",
    "category": "Law",
    "subcategory": "Legal systems and jurisprudence",
    "level": "Pre-university",
    "duration": "5 weeks (3 hours/week)",
    "instructor": faculty,
    "description": "An inquiry into the law of private civil wrongs. Students study the four elements of actionable negligence (duty of care, breach, causation, and remoteness), the neighbor principle formulated in Donoghue v Stevenson, vicarious liability, product liability, and the economic policy functions of tort law in allocating accidental losses.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Deconstruct the four pillars of negligence: Duty of Care, Breach, Causation, and Remoteness of Damage.",
      "Apply the 'Neighbor Principle' from Donoghue v Stevenson and the Caparo tripartite test.",
      "Analyze the objective standard of the reasonable person and the Learned Hand formula (B < PL).",
      "Evaluate strict liability doctrines under Rylands v Fletcher and statutory consumer product liability."
    ],
    "modules": [
      {
        "title": "Module 1: The Modern Tort of Negligence",
        "lessons": [
          {
            "id": "law-tort-l1",
            "title": "The Neighbor Principle and the Duty of Care",
            "body": """### The Genesis of Modern Negligence

Until the 1930s, English and Commonwealth tort law was fractured into separate categories based on specific privity of contract or recognized relationships.

In **Donoghue v Stevenson** [1932] AC 562, Mrs. Donoghue drank ginger beer from an opaque bottle manufactured by Stevenson. Unknown to her, a decomposed snail was inside the bottle. She suffered severe gastroenteritis and nervous shock. Because her friend had bought the drink, Donoghue had no contract with either the cafe owner or the manufacturer.

#### Lord Atkin's Neighbor Principle
Lord Atkin formulated a universal moral and legal standard:
> *"The rule that you are to love your neighbour becomes in law, you must not injure your neighbour... You must take reasonable care to avoid acts or omissions which you can reasonably foresee would be likely to injure your neighbour. Who, then, in law is my neighbour? The answer seems to be—persons who are so closely and directly affected by my act that I ought reasonably to have them in contemplation as being so affected."*

#### The Learned Hand Formula of Breach
Once a duty of care is established, the plaintiff must prove that the defendant **breached** that duty by falling below the standard of the reasonable person. In *United States v Carroll Towing Co* (1947), Judge Learned Hand expressed this through an algebraic economic formula:

$$\\text{Liability exists if: } B < P \\times L$$

Where:
- **$B$ (Burden):** The cost of taking adequate precautions against the risk.
- **$P$ (Probability):** The likelihood that the harm will occur if precautions are not taken.
- **$L$ (Loss / Gravity):** The severity of the injury if the risk materializes.

If the financial or practical burden ($B$) of eliminating the risk is less than the expected harm ($P \\times L$), failure to take the precaution constitutes actionable negligence.""",
            "readings": [
              {"label": "Donoghue v Stevenson [1932] UKHL 100", "url": "https://www.bailii.org/uk/cases/UKHL/1932/100.html"},
              {"label": "United States v. Carroll Towing Co., 159 F.2d 169 (2d Cir. 1947)", "url": "https://casetext.com/case/united-states-v-carroll-towing-co"}
            ],
            "quiz": [
              {
                "q": "Under the Learned Hand formula (B < PL), when has a defendant breached their duty of care?",
                "options": [
                  "Whenever an accident occurs, regardless of cost.",
                  "When the burden (B) of taking precautions is less than the probability (P) multiplied by the gravity of the resulting harm (L).",
                  "Only when the defendant intentionally intended to harm the plaintiff.",
                  "When the plaintiff was partially responsible for their own misfortune."
                ],
                "answer": 1,
                "why": "The Learned Hand formula balances economic efficiency and reasonable care: if a modest precaution could prevent a severe, likely danger, failing to take it is negligent."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "law-jurisprudence",
    "title": "Jurisprudence: Natural Law, Legal Positivism & Critical Legal Studies",
    "category": "Law",
    "subcategory": "Legal systems and jurisprudence",
    "level": "Undergraduate",
    "duration": "7 weeks (4 hours/week)",
    "instructor": faculty,
    "description": "An inquiry into the philosophy of law. This course engages the eternal debate between Natural Law theorists (who insist on a necessary moral threshold for legal validity) and Legal Positivists (who insist on the separation of law as it is from law as it ought to be). Students examine Aquinas, John Austin, H.L.A. Hart, Ronald Dworkin, Lon Fuller, and modern Critical Legal Studies.",
    "passMark": 75,
    "certificate": True,
    "objectives": [
      "Distinguish between Natural Law Theory (Lex iniusta non est lex) and Legal Positivism.",
      "Analyze H.L.A. Hart's Concept of Law: Primary rules, secondary rules, and the Rule of Recognition.",
      "Evaluate Lon Fuller's internal morality of law and the procedural demands of legal order.",
      "Critique Ronald Dworkin's 'interpretive turn' and the thesis of one right legal answer."
    ],
    "modules": [
      {
        "title": "Module 1: The Hart-Fuller Debate and the Separation Thesis",
        "lessons": [
          {
            "id": "law-jur-l1",
            "title": "The Separation of Law and Morality: H.L.A. Hart vs Lon Fuller",
            "body": """### What Is Law? The Central Question of Jurisprudence

Jurisprudence addresses the philosophical foundations of legal systems. The pivotal divide in 20th-century legal philosophy was fought between Oxford legal positivist **H.L.A. Hart** and Harvard natural law scholar **Lon L. Fuller** in the pages of the 1958 *Harvard Law Review*.

#### 1. Legal Positivism and the Separation Thesis
Legal positivism insists upon the **Separation Thesis**: there is no necessary conceptual connection between the law as it *is* and the law as it *ought to be*.
- In *The Concept of Law* (1961), Hart refuted John Austin's older 'command theory' (law as orders backed by threats of a sovereign).
- Instead, Hart showed that a legal system is an intricate union of:
  - **Primary Rules:** Rules that mandate or prohibit conduct (e.g., criminal prohibitions against theft or violence).
  - **Secondary Rules:** Rules about rules, enabling the system to evolve:
    - *Rules of Change:* How new laws are enacted or repealed.
    - *Rules of Adjudication:* Empowering judges to resolve disputes.
    - *The Rule of Recognition:* The ultimate empirical social rule accepted by legal officials that identifies which standards count as valid law.

#### 2. Natural Law and Fuller's 'Internal Morality of Law'
Fuller argued that law is the enterprise of subjecting human conduct to the governance of rules. To count as a legal system at all, a legal order must satisfy eight procedural moral virtues:
1. Generality (rules must not be ad hoc).
2. Promulgation (rules must be publicized).
3. Non-retroactivity (laws must look forward, not punish past acts).
4. Clarity (intelligibility).
5. Non-contradiction.
6. Possibility of compliance (no commanding the impossible).
7. Constancy through time.
8. Congruence between official action and declared rule.""",
            "readings": [
              {"label": "H.L.A. Hart, Positivism and the Separation of Law and Morals (1958)", "url": "https://www.jstor.org/stable/1338225"},
              {"label": "Lon L. Fuller, Positivism and Fidelity to Law: A Reply to Professor Hart (1958)", "url": "https://www.jstor.org/stable/1338226"},
              {"label": "Stanford Encyclopedia of Philosophy, Legal Positivism", "url": "https://plato.stanford.edu/entries/legal-positivism/"}
            ],
            "quiz": [
              {
                "q": "What is the core claim of the 'Separation Thesis' in Legal Positivism?",
                "options": [
                  "Courts must be physically located away from legislative assemblies.",
                  "There is no necessary conceptual connection between the legal validity of a rule and its moral righteousness.",
                  "Religious statutes are superior to international treaties.",
                  "Laws can only be enacted by direct popular referenda."
                ],
                "answer": 1,
                "why": "The separation thesis asserts that an iniquitous or immoral statute may still be legally valid if it meets the formal procedural criteria of the legal system's Rule of Recognition."
              }
            ]
          }
        ]
      }
    ]
  }
]

print("Law courses compiled: 10/10")
