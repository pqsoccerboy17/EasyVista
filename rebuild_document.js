const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, ShadingType, convertInchesToTwip, Header, Footer } = require("docx");
const fs = require("fs");

// Create the document
const doc = new Document({
  sections: [
    {
      properties: {
        page: {
          margins: {
            top: convertInchesToTwip(1),
            bottom: convertInchesToTwip(1),
            left: convertInchesToTwip(1),
            right: convertInchesToTwip(1),
          },
        },
      },
      headers: {
        default: new Header({
          children: [
            new Paragraph({
              text: "EasyVista — BDR Manager Communication",
              alignment: AlignmentType.CENTER,
              children: [
                new TextRun({
                  text: "EasyVista — BDR Manager Communication",
                  font: "Arial",
                  size: 24,
                  color: "808080", // Gray
                  bold: false,
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
            }),
          ],
        }),
      },
      children: [
        // Subject Line
        new Paragraph({
          children: [
            new TextRun({
              text: "ACTION REQUIRED: Lemlist AI Automation — Your BDR Team's New Superpower",
              font: "Arial",
              size: 24,
              bold: true,
            }),
          ],
          alignment: AlignmentType.LEFT,
          spacing: {
            after: 200,
          },
        }),

        // Greeting
        new Paragraph({
          children: [
            new TextRun({
              text: "Hi [Regional BDR Manager Name],",
              font: "Arial",
              size: 24,
            }),
          ],
          alignment: AlignmentType.LEFT,
          spacing: {
            after: 200,
          },
        }),

        // Intro paragraph
        new Paragraph({
          children: [
            new TextRun({
              text: "I'm writing to introduce you to Lemlist, a new AI-powered LinkedIn automation platform we're rolling out across our global BDR organization. This is an enterprise-grade investment approved by leadership to give your team a meaningful productivity boost.",
              font: "Arial",
              size: 24,
            }),
          ],
          alignment: AlignmentType.LEFT,
          spacing: {
            after: 200,
          },
        }),

        // The Bottom Line section
        new Paragraph({
          children: [
            new TextRun({
              text: "The Bottom Line:",
              bold: true,
              font: "Arial",
              size: 24,
            }),
            new TextRun({
              text: " Same effort, bigger results. Your BDRs will go from generating 15-20 opportunities per quarter to 25-30 — without adding headcount or increasing their workload. Lemlist automates the repetitive parts of prospecting (sequencing, follow-ups, personalization) so your team can focus on what matters: building relationships and closing deals.",
              font: "Arial",
              size: 24,
            }),
          ],
          alignment: AlignmentType.LEFT,
          spacing: {
            after: 200,
          },
        }),

        // Key Dates heading
        new Paragraph({
          children: [
            new TextRun({
              text: "Key Dates:",
              bold: true,
              font: "Arial",
              size: 24,
            }),
          ],
          spacing: {
            after: 100,
          },
        }),

        // Pilot Launch bullet
        new Paragraph({
          text: "Pilot Launch: February 20, 2026 (Friday)",
          level: 0,
          style: "List Bullet",
          spacing: {
            after: 100,
          },
          children: [
            new TextRun({
              text: "Pilot Launch: February 20, 2026 (Friday)",
              font: "Arial",
              size: 24,
            }),
          ],
        }),

        // Office Hours Kickoff bullet with yellow highlight
        new Paragraph({
          children: [
            new TextRun({
              text: "Office Hours Kickoff: TBD — scheduling details to follow",
              font: "Arial",
              size: 24,
              shading: {
                type: ShadingType.CLEAR,
                fill: "FFFF00",
              },
            }),
          ],
          level: 0,
          style: "List Bullet",
          spacing: {
            after: 200,
          },
        }),

        // What We Need From You heading
        new Paragraph({
          children: [
            new TextRun({
              text: "What We Need From You:",
              bold: true,
              font: "Arial",
              size: 24,
            }),
          ],
          spacing: {
            after: 100,
          },
        }),

        // Numbered list items
        new Paragraph({
          text: "Identify 2-3 BDRs from your region for the pilot group",
          level: 0,
          style: "List Number",
          spacing: {
            after: 100,
          },
          children: [
            new TextRun({
              text: "Identify 2-3 BDRs from your region for the pilot group",
              font: "Arial",
              size: 24,
            }),
          ],
        }),

        new Paragraph({
          text: "Block 1 hour during the week of Feb 10 for a platform walkthrough",
          level: 0,
          style: "List Number",
          spacing: {
            after: 100,
          },
          children: [
            new TextRun({
              text: "Block 1 hour during the week of Feb 10 for a platform walkthrough",
              font: "Arial",
              size: 24,
            }),
          ],
        }),

        new Paragraph({
          text: "Review the adoption guide (link below) before the kickoff",
          level: 0,
          style: "List Number",
          spacing: {
            after: 200,
          },
          children: [
            new TextRun({
              text: "Review the adoption guide (link below) before the kickoff",
              font: "Arial",
              size: 24,
            }),
          ],
        }),

        // Resources heading
        new Paragraph({
          children: [
            new TextRun({
              text: "Resources:",
              bold: true,
              font: "Arial",
              size: 24,
            }),
          ],
          spacing: {
            after: 100,
          },
        }),

        new Paragraph({
          text: "Adoption Guide: [Link to guides site]",
          level: 0,
          style: "List Bullet",
          spacing: {
            after: 100,
          },
          children: [
            new TextRun({
              text: "Adoption Guide: [Link to guides site]",
              font: "Arial",
              size: 24,
            }),
          ],
        }),

        new Paragraph({
          text: "ROI Calculator: [Link to ROI calculator]",
          level: 0,
          style: "List Bullet",
          spacing: {
            after: 100,
          },
          children: [
            new TextRun({
              text: "ROI Calculator: [Link to ROI calculator]",
              font: "Arial",
              size: 24,
            }),
          ],
        }),

        new Paragraph({
          text: "Lemlist University (free training): https://university.lemlist.com/",
          level: 0,
          style: "List Bullet",
          spacing: {
            after: 200,
          },
          children: [
            new TextRun({
              text: "Lemlist University (free training): https://university.lemlist.com/",
              font: "Arial",
              size: 24,
            }),
          ],
        }),

        // Why This Matters heading
        new Paragraph({
          children: [
            new TextRun({
              text: "Why This Matters for Your Team:",
              bold: true,
              font: "Arial",
              size: 24,
            }),
          ],
          spacing: {
            after: 100,
          },
        }),

        new Paragraph({
          text: "AI-powered personalization at scale — every outreach feels handcrafted",
          level: 0,
          style: "List Bullet",
          spacing: {
            after: 100,
          },
          children: [
            new TextRun({
              text: "AI-powered personalization at scale — every outreach feels handcrafted",
              font: "Arial",
              size: 24,
            }),
          ],
        }),

        new Paragraph({
          text: "Multi-touch LinkedIn + email sequences that run on autopilot",
          level: 0,
          style: "List Bullet",
          spacing: {
            after: 100,
          },
          children: [
            new TextRun({
              text: "Multi-touch LinkedIn + email sequences that run on autopilot",
              font: "Arial",
              size: 24,
            }),
          ],
        }),

        new Paragraph({
          text: "Real-time analytics so you can coach your team with data, not guesses",
          level: 0,
          style: "List Bullet",
          spacing: {
            after: 100,
          },
          children: [
            new TextRun({
              text: "Real-time analytics so you can coach your team with data, not guesses",
              font: "Arial",
              size: 24,
            }),
          ],
        }),

        new Paragraph({
          text: "50+ hours/month saved per BDR on repetitive prospecting tasks",
          level: 0,
          style: "List Bullet",
          spacing: {
            after: 200,
          },
          children: [
            new TextRun({
              text: "50+ hours/month saved per BDR on repetitive prospecting tasks",
              font: "Arial",
              size: 24,
            }),
          ],
        }),

        // Closing paragraph
        new Paragraph({
          children: [
            new TextRun({
              text: "I'll be scheduling a brief kickoff call with all regional managers next week. In the meantime, if you have questions, don't hesitate to reach out.",
              font: "Arial",
              size: 24,
            }),
          ],
          alignment: AlignmentType.LEFT,
          spacing: {
            after: 200,
          },
        }),

        // Sign-off
        new Paragraph({
          children: [
            new TextRun({
              text: "Best regards,",
              font: "Arial",
              size: 24,
            }),
          ],
          alignment: AlignmentType.LEFT,
          spacing: {
            after: 100,
          },
        }),

        new Paragraph({
          children: [
            new TextRun({
              text: "[Your Name]",
              font: "Arial",
              size: 24,
            }),
          ],
          alignment: AlignmentType.LEFT,
          spacing: {
            after: 50,
          },
        }),

        new Paragraph({
          children: [
            new TextRun({
              text: "EasyVista AI Sales Enablement",
              font: "Arial",
              size: 24,
            }),
          ],
          alignment: AlignmentType.LEFT,
          spacing: {
            after: 200,
          },
        }),
      ],
    },
  ],
});

// Generate the document
Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync(
    "/sessions/gracious-practical-meitner/mnt/EasyVista/BDR_Manager_Lemlist_Rollout_Template.docx",
    buffer
  );
  console.log("Document generated successfully!");
});
