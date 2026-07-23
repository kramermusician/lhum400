# Spreadsheets, from the first click
## A text-only walkthrough for LHUM 400

This is the plain-text version of the hands-on spreadsheet walkthrough. The interactive page (lhum400-spreadsheet-walkthrough.html) lets you practice in live grids; this version works anywhere, including with a screen reader or a printout. To follow along, open a blank spreadsheet at sheets.google.com and build each example as you read.

The working idea for the whole guide: a spreadsheet puts light on a question, so the action you take next is a smarter one. Data first, decision second.

---

## Level 0: What is this thing?

A spreadsheet is a grid of boxes. Each box can hold a word or a number. And any box can do math using the other boxes.

People kept grids like this on paper for centuries: one row per thing, one column per fact about it. Rent here, groceries there, total at the bottom. The digital version keeps the same shape and adds one superpower: when a number changes, every total that depends on it updates itself. Instantly. Without being asked.

If you have never opened a spreadsheet in your life, you are in exactly the right place. This guide assumes nothing.

## Level 0: Why bother?

Your head can hold maybe four numbers before they start trading places. A grid holds all of them, in daylight, at once.

But the math is not really the point. The point is the question underneath it. Can I afford this move? Which gig is actually worth my Saturday? Where does my money go every month? Questions like these feel foggy when they live in your head. Put the numbers in a grid and the fog lifts: the question becomes something you can look at, poke, and answer.

---

## Step 1: Every box has an address

Columns are letters (A, B, C). Rows are numbers (1, 2, 3). A box's address is column plus row, like B2. Think of a seat at a show: section B, row 2. The address is how you find one box among many, and later it is how formulas find each other.

When you click a box, its address appears in the small name box at the top left, and its contents appear in the formula bar next to it.

## Step 2: Type your first number

1. Click cell B1.
2. Type 42 and press Enter.

Two things happened. The number got saved into the box, and the selection dropped down one row, ready for the next entry. That little hop is why data entry in a spreadsheet goes fast.

Now click A1 and type the word Coffee. Notice the grid treats it differently: words sit on the left edge of the box, numbers sit on the right. The grid already knows which is which.

Made a mess? Click any box and press Delete to clear it, or just retype. Nothing here is precious.

## Step 3: A box does one of three jobs

1. Label: words that name things, like Rent or Total. No math.
2. Input: a number you type and can change.
3. Formula: a calculation that starts with the equals sign.

Every spreadsheet you will ever build, no matter how large, is these three jobs arranged on a grid.

## Step 4: Formulas start with =

The equals sign tells a box to calculate instead of just holding what you typed. Here is what happens, in slow motion, when you press Enter on =B1+B2:

1. The box reads the recipe: go get B1, go get B2, add them.
2. It fetches those values and does the math.
3. It shows the result, and it remembers the recipe.

That last part matters. The box does not store the answer. It stores the recipe, and re-cooks it any time an ingredient changes.

The four basics:

    =B1+B2   adds
    =B1-B2   subtracts
    =B1*3    multiplies
    =B1/2    divides

Try it: put 8 in B1, put 5 in B2, then in B3 type =B1+B2 and press Enter. B3 shows 13. Now change B1 and watch B3 follow.

Point, don't type. =8+5 also gives 13, but it is a dead end: change your numbers and it sits there, wrong. =B1+B2 points at the boxes, so it stays true no matter what you put in them. Pointing is the whole trick.

## Step 5: Add a whole column with a range

A range is a run of boxes. B1:B3 means B1 through B3. Feed it to SUM:

    =SUM(B1:B3)

Try it: put 10, 20, 30 in B1, B2, B3. In C1 type =SUM(B1:B3). You should get 60.

## Step 6: Ask a column some questions

SUM has cousins, and each one answers a different question about the same pile of numbers:

    =AVERAGE(B1:B5)   what's typical?
    =MIN(B1:B5)       what's the worst?
    =MAX(B1:B5)       what's the best?
    =COUNT(B1:B5)     how many entries?

Try it with minutes of practice, Monday through Friday: 20, 45, 0, 30, 25 in B1 through B5. The average is 24. Now change Wednesday's 0 to 60 and watch the average jump. One unusual day can drag a whole average around. That is worth knowing before you trust any average, including the ones in headlines.

## Step 7: Teach a box to decide with IF

IF asks a yes-or-no question and shows one answer or the other:

    =IF(test, answer if yes, answer if no)

The test uses comparison signs: > more than, < less than, >= at least, <= at most. Words inside a formula go in straight double quotes.

Try it: put 250 in B1 (what's left of a budget). In C1 type:

    =IF(B1>=0, "OK", "OVER")

Then change B1 to -40 and watch the verdict flip. A box that watches a number and raises a flag when it crosses a line: that is the seed of every dashboard you have ever seen.

---

# The ladder

Everything below is a real question someone in this course could be asking this semester. Each one starts foggy and ends as a number you can act on. Climb until one of them bites. For each scenario: labels go in column A, numbers and formulas in column B (and C when comparing two options).

## Scenario 1: What can the band afford?

Rows: Players, Hours, Dollars per player per hour, Total earned, Pizzas at 18 dollars.

1. Inputs: B1 = 4 players, B2 = 1 hour, B3 = 15 per player per hour.
2. B4 (total earned): =B1*B2*B3
3. B5 (pizzas): =B4/18

Target: 60 dollars earned, about 3.33 pizzas. Now change Hours to 3. Both answers jump, and nobody redid any math.

## Scenario 2: Where does the month actually go?

Rows: Income, Rent, Food, Spent, Left over.

1. Inputs: B1 = 1200, B2 = 700, B3 = 250.
2. B4 (spent): =SUM(B2:B3)
3. B5 (left over): =B1-B4

Target: spent 950, left over 250. Left over reads from Spent, which reads from the expenses. Change Rent and the change flows all the way down. Chains like this are how big models are built: each box asks the one before it.

## Scenario 3: When can I actually have the gear?

Rows: Save per week, Weeks, Saved so far, Goal, Still need.

1. Inputs: B1 = 40, B2 = 12, B4 = 600.
2. B3 (saved so far): =B1*B2
3. B5 (still need): =B4-B3

Target: saved 480, still need 120. Change Weeks until Still need hits 0. You just ran a forecast: same grid, pointed at the future instead of the past.

## Scenario 4: What do the little monthly charges really cost?

Rows: Streaming, Cloud storage, Sample packs, Per month, Per year.

1. Inputs: B1 = 12, B2 = 3, B3 = 10.
2. B4 (per month): =SUM(B1:B3)
3. B5 (per year): =B4*12

Target: 25 per month, 300 per year. 300 dollars is a decent microphone. Delete one row's number and watch the year shrink. If you just felt a little tug about which one to cut, notice what happened: the data asked you a question you were not asking yourself.

## Scenario 5: Which gig actually pays better?

Gig A pays 120 dollars for a 3-hour night, door to door. Gig B pays 200 but eats 6 hours with the drive. Put each option in its own column and ask the same question of both.

Rows: Pay, Hours door to door, Per hour. Column B is Gig A, column C is Gig B.

1. Inputs: B1 = 120, C1 = 200, B2 = 3, C2 = 6.
2. B3: =B1/B2 and C3: =C1/C2

Target: Gig A 40 per hour, Gig B about 33.33. The bigger check lost. The flat fee was hiding the drive, and the per-hour number put light on it. This is the pattern for comparing anything: apartments, laptops, tour routings. One column per option, one row per fact, one formula asked of every column.

## Scenario 6: How many tickets until the show pays for itself?

You are thinking about renting a room for a show. The room holds 40 people.

Rows: Room, Sound tech, Ticket price, Total cost, Tickets to break even, Verdict.

1. Inputs: B1 = 150, B2 = 90, B3 = 8.
2. B4 (total cost): =B1+B2
3. B5 (break even): =B4/B3
4. B6 (verdict): =IF(B5<=40, "GO", "RISKY")

Target: cost 240, break even at 30 tickets, verdict GO. Now raise the room to 250 and watch the verdict flip. The sheet is not deciding for you. It is showing you exactly where the line sits, so you can argue with the inputs instead of with your gut. Want the show to work? Now you know your levers: a cheaper room, a higher ticket, or a bigger venue.

## Scenario 7: Is the cheap one actually cheaper?

A 60-dollar audio interface that dies in 2 years, or a 180-dollar one that runs for 8? The sticker answers what leaves your pocket today. Cost per year answers what owning it really costs. Different question, sometimes a different winner.

Rows: Price, Years it lasts, Cost per year. Column B is the budget one, column C is the sturdy one.

1. Inputs: B1 = 60, C1 = 180, B2 = 2, C2 = 8.
2. B3: =B1/B2 and C3: =C1/C2

Target: budget one 30 per year, sturdy one 22.50 per year. The trick generalizes: cost per use, cost per gig, cost per student, cost per mile. Whenever two options refuse to compare, divide both by the thing you actually care about and they will.

---

## Sandbox: Ask your own question

Pick a question you actually have and rough it out. Some starters:

1. What would moving to a cheaper place really save in a year?
2. What does my coffee habit cost per semester?
3. How many lessons do I need to teach before the new amp is paid off?
4. Which of two summer plans leaves me with more in September?

Shape to aim for: labels down the left, inputs you can change, formulas that point at them, and if you want a straight answer, an IF verdict at the bottom.

## Example sheets: real spreadsheets to open and dissect

Reading other people's spreadsheets is how you get good, the same way listening is how you learn to play. Everything below is free, lives in (or copies into) Google Sheets, and asks for no signup. Open one and go hunting for the three jobs: labels, inputs, formulas.

Simple:

1. Google's own Monthly Budget template. Open sheets.google.com, click Template gallery, choose Monthly budget. Mission: click the big total on the summary tab and read its formula. Where does the number actually come from?
2. Spreadsheet Class template library at spreadsheetclass.com/templates. Two dozen small free templates. Mission: copy one, break it on purpose, fix it.

Intermediate:

3. The Measure of a Plan budget tracking tool at themeasureofaplan.com/budget-tracking-tool. A genuinely free tracker with a self-building dashboard. Mission: trace one chart back to the cells it reads.

Advanced:

4. Aspire Budgeting at aspirebudget.com. A full zero-based budgeting system in one Google Sheet. Mission: figure out why it is split across tabs, and what each tab is allowed to know about the others.
5. Vertex42 loan amortization schedule at vertex42.com/ExcelTemplates/loan-amortization-schedule.html. Mission: find the PMT function, change one input, and explain why the payoff date moved.

Not sure which tier is yours? The level quiz (lhum400-spreadsheet-level-quiz.html) points you at a starting line.

## Next: powers the real thing adds

Once your model works, Google Sheets (or Excel, or Numbers) gives you more:

1. Charts: select your numbers, then Insert > Chart, and the picture updates with the data.
2. Sorting and filtering, for when your rows number in the hundreds.
3. Sharing, so a bandmate or roommate can argue with your inputs instead of your conclusions.

Same three jobs, same equals sign, same colon for ranges. Sheets, Excel, and Numbers are one grid in different clothes.

A box can label, hold, or calculate. That's the whole secret. The rest is asking better questions.

---

Prof. Kramer Gibson - Berklee College of Music
