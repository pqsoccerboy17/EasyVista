const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  HeadingLevel,
  AlignmentType,
  ShadingType,
  convertInchesToTwip,
  Header,
  Footer,
} = require("docx");
const fs = require("fs");

// Helper function to create yellow highlighted text
function yellowHighlight(text, isBold = false) {
  return new TextRun({
    text: text,
    bold: isBold,
    font: "Arial",
    size: 24, // 12pt
    shading: {
      type: ShadingType.CLEAR,
      fill: "FFFF00",
    },
  });
}

// Helper function to create normal text
function normalText(text, isBold = false) {
  return new TextRun({
    text: text,
    bold: isBold,
    font: "Arial",
    size: 24, // 12pt
  });
}

const doc = new Document({
  sections: [
    {
      properties: {
        page: {
          margins: {
            top: convertInchesToTwip(1),
            right: convertInchesToTwip(1),
            bottom: convertInchesToTwip(1),
            left: convertInchesToTwip(1),
          },
        },
      },
      headers: {
        default: new Header({
          children: [
            new Paragraph({
              text: "EasyVista, BDR Manager Communication",
              alignment: AlignmentType.CENTER,
              children: [
                new TextRun({
                  text: "EasyVista, BDR Manager Communication",
                  font: "Arial",
                  size: 24,
                  color: "808080",
                }),
              ],
            }),
          ],
        }),
      },
      footers: {
        default: new Footer({
          children: [
            new Paragraph({
              text: "",
              alignment: AlignmentType.CENTER,
              children: [
                new TextRun({
                  text: "Page ",
                  font: "Arial",
                  size: 24,
                }),
              ],
            }),
          ],
        }),
      },
      children: [
        // Subject line
        new Paragraph({
          text: "ACTION REQUIRED: Lemlist AI Automation for Your BDR Team",
          heading: HeadingLevel.HEADING_1,
          alignment: AlignmentType.LEFT,
          spacing: {
            after: 400,
          },
          children: [
            new TextRun({
              text: "ACTION REQUIRED: Lemlist AI Automation for Your BDR Team",
              bold: true,
              font: "Arial",
              size: 24,
            }),
          ],
        }),

        // Body paragraph 1
        new Paragraph({
          text: "",
          spacing: {
            after: 200,
          },
          children: [
            normalText("Hi [Regional BDR Manager Name],\n\n"),
            normalText(
              "I'm reaching out to introduce Lemlist, a new AI powered LinkedIn automation platform we're rolling out across our entire global BDR organization. This is an investment approved by leadership to give your team a meaningful productivity boost starting this quarter."
            ),
          ],
        }),

        // The Bottom Line section
        new Paragraph({
          text: "",
          spacing: {
            after: 200,
          },
          children: [
            normalText("The Bottom Line: ", true),
            normalText(
              "Same effort, bigger results. Your BDRs will go from generating 15 to 20 opportunities per quarter to 25 to 30, without adding headcount or increasing their workload. Lemlist automates the repetitive parts of prospecting (sequencing, follow ups, personalization) so your team can focus on what matters: building relationships and closing deals."
            ),
          ],
        }),

        // Key Dates section header
        new Paragraph({
          text: "",
          spacing: {
            after: 200,
          },
          children: [
            normalText("Key Dates:", true),
          ],
        }),

        // Key Dates bullet points with yellow highlight on entire line
        new Paragraph({
          text: "",
          spacing: {
            after: 100,
            before: 0,
          },
          children: [
            yellowHighlight("Platform Walkthrough: Week of February 9"),
          ],
        }),

        new Paragraph({
          text: "",
          spacing: {
            after: 100,
            before: 0,
          },
          children: [
            yellowHighlight("Pilot Launch: Friday, February 20, 2026"),
          ],
        }),

        new Paragraph({
          text: "",
          spacing: {
            after: 200,
            before: 0,
          },
          children: [
            yellowHighlight("Office Hours Kickoff: TBD, scheduling details to follow"),
          ],
        }),

        // What We Need From You section header
        new Paragraph({
          text: "",
          spacing: {
            after: 200,
          },
          children: [
            normalText("What We Need From You:", true),
          ],
        }),

        // Numbered list items
        new Paragraph({
          text: "",
          spacing: {
            after: 100,
            before: 0,
          },
          children: [
            yellowHighlight("1. Block 1 hour during the week of Feb 9 for a platform walkthrough"),
          ],
        }),

        new Paragraph({
          text: "",
          spacing: {
            after: 100,
            before: 0,
          },
          children: [
            normalText("2. Ensure your full BDR team is aware and ready to participate"),
          ],
        }),

        new Paragraph({
          text: "",
          spacing: {
            after: 200,
            before: 0,
          },
          children: [
            normalText("3. Review the adoption guide and resources below before the kickoff"),
          ],
        }),

        // Resources section header
        new Paragraph({
          text: "",
          spacing: {
            after: 200,
          },
          children: [
            normalText("Resources:", true),
          ],
        }),

        // Resources bullet points with hyperlinks
        new Paragraph({
          text: "",
          spacing: {
            after: 100,
            before: 0,
          },
          children: [
            normalText("EasyVista AI Sales Enablement Portal: "),
            new TextRun({
              text: "https://yelin-io.github.io/EasyVista/portal/index.html",
              font: "Arial",
              size: 24,
              color: "0563C1",
              underline: {},
            }),
          ],
        }),

        new Paragraph({
          text: "",
          spacing: {
            after: 200,
            before: 0,
          },
          children: [
            normalText("Lemlist University (free training): "),
            new TextRun({
              text: "https://university.lemlist.com/",
              font: "Arial",
              size: 24,
              color: "0563C1",
              underline: {},
            }),
          ],
        }),

        // Why This Matters for Your Team section header
        new Paragraph({
          text: "",
          spacing: {
            after: 200,
          },
          children: [
            normalText("Why This Matters for Your Team:", true),
          ],
        }),

        // Why This Matters bullet points
        new Paragraph({
          text: "",
          spacing: {
            after: 100,
            before: 0,
          },
          children: [
            normalText(
              "AI powered personalization at scale so every outreach feels handcrafted"
            ),
          ],
        }),

        new Paragraph({
          text: "",
          spacing: {
            after: 100,
            before: 0,
          },
          children: [
            normalText("Multi touch LinkedIn and email sequences that run on autopilot"),
          ],
        }),

        new Paragraph({
          text: "",
          spacing: {
            after: 100,
            before: 0,
          },
          children: [
            normalText("Real time analytics so you can coach your team with data, not guesses"),
          ],
        }),

        new Paragraph({
          text: "",
          spacing: {
            after: 200,
            before: 0,
          },
          children: [
            normalText("50+ hours per month saved per BDR on repetitive prospecting tasks"),
          ],
        }),

        // Closing paragraph
        new Paragraph({
          text: "",
          spacing: {
            after: 200,
          },
          children: [
            normalText(
              "We're moving quickly on this. I'll be scheduling a kickoff call with all regional managers this week. If you have questions in the meantime, don't hesitate to reach out."
            ),
          ],
        }),

        // Signature
        new Paragraph({
          text: "",
          spacing: {
            after: 100,
            before: 0,
          },
          children: [
            normalText("Best regards,"),
          ],
        }),

        new Paragraph({
          text: "",
          spacing: {
            after: 0,
            before: 0,
          },
          children: [
            normalText("[Your Name]"),
          ],
        }),

        new Paragraph({
          text: "",
          spacing: {
            after: 0,
            before: 0,
          },
          children: [
            normalText("EasyVista AI Sales Enablement"),
          ],
        }),
      ],
    },
  ],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync(
    "/sessions/gracious-practical-meitner/mnt/EasyVista/BDR_Manager_Lemlist_Rollout_Template.docx",
    buffer
  );
  console.log(
    "Document created successfully at /sessions/gracious-practical-meitner/mnt/EasyVista/BDR_Manager_Lemlist_Rollout_Template.docx"
  );
});
