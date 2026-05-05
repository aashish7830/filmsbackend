// 1. Saare blogs ka data ek object mein
const blogs = {
    "saas-stack": {
        title: "The Complete SaaS Tech Stack for 2026",
        subtitle: "A founder's guide to scalable technology.",
        category: "SaaS • Tech",
        date: "18 Mar 2026",
        author: "Manish Verma",
        image: "images/success-story/Elon.png",
        content: `<h2>Choosing the Right Stack</h2>
            <p>In 2026, efficiency is everything. Use React for frontend and Node.js for backend...</p>`
    },
    "technical-strategy": {
        title: "Technical Strategy for Non-Technical Founders",
        subtitle: "A practical guide to help non-technical founders make tech decisions.",
        category: "AI Strategy",
        date: "18 Mar 2026",
        author: "Manish Verma",
        image: "images/success-story/Elon.png",
        content: `<section class="audience-info">
                <p><strong>Target Audience:</strong> SaaS Founders • CTOs • Operations Heads</p>
            </section>
            <h2>Introduction</h2>
            <p>Non-technical founders often face challenges when making decisions about software development...</p>
            <h2>Step 1: Define Your Product Vision</h2>
            <ul>
                <li>Clearly articulate the problem your SaaS product solves</li>
                <li>Set measurable business goals</li>
            </ul>
            <h2>Conclusion</h2>
            <p>Platforms like jenerix.ai make it easier to manage development.</p>`
    },
    "custom-software": {
        title: "When to Build Custom Software vs Existing Tools",
        subtitle: "Decide between custom development and off-the-shelf solutions.",
        category: "Development",
        date: "18 Mar 2026",
        author: "Manish Verma",
        image: "images/success-story/Elon.png",
        content: `<section class="audience-info">
                <p><strong>Target Audience:</strong> SaaS Founders • CTOs • Operations Heads</p>
            </section>
            <h2>Introduction</h2>
            <p>Non-technical founders often face challenges when making decisions about software development...</p>
            <h2>Step 1: Define Your Product Vision</h2>
            <ul>
                <li>Clearly articulate the problem your SaaS product solves</li>
                <li>Set measurable business goals</li>
            </ul>
            <h2>Conclusion</h2>
            <p>Platforms like jenerix.ai make it easier to manage development.</p>`
    }
};

// 2. URL se ID nikalne ka logic
const urlParams = new URLSearchParams(window.location.search);
const blogId = urlParams.get('id');

// 3. Page content update karna
if (blogId && blogs[blogId]) {
    const data = blogs[blogId];
    document.getElementById('blog-title').innerText = data.title;
    document.getElementById('blog-subtitle').innerText = data.subtitle;
    document.getElementById('blog-category').innerText = data.category;
    document.getElementById('blog-date').innerText = `Published: ${data.date}`;
    document.getElementById('blog-author').innerText = `Author: ${data.author}`;
    document.getElementById('blog-image').src = data.image;
    document.getElementById('blog-content').innerHTML = data.content;
} else {
    document.getElementById('blog-title').innerText = "Blog Not Found";
}