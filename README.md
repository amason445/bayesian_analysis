# Bayesian Analysis - User Access Groups

## Summary and Results

A friend mentioned he was performing Bayesian Analysis on user access groups at his job. He has to answer the question, "Given a user is a member of a group, do they have access to any individual file?" I thought their problem was interesting and I was coincidentally studying Bayes' Formula this weekend so I decided to write a Python script for a similar problem I thought of. I created a CSV of imaginary users, their job titles and imginary user access groups they belong to.

![alt_text](https://github.com/amason445/bayesian_analysis/blob/main/UserAccessList.png)

After normalizing this data, I calculated prior and posterior probabilities using Bayes' Formula with the below results. An example interpretation would read that a user has an 18% chance of being a member of the sales access group given that they are a member of the executive group.

![!alt_text](https://github.com/amason445/bayesian_analysis/blob/main/output.png)

## References
- [Bayes' Formula](https://en.wikipedia.org/wiki/Bayes%27_theorem)


 
